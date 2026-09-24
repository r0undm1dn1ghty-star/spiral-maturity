# -*- coding: utf-8 -*-
"""Реализация Spiral Maturity для skillkit. Правила — из SKILL.md/docs методики.
Вход: {"org": {"<индикатор>": value, ...}} или свободный текст с маркерами."""
import re

SKILL_NAME = "spiral-maturity"
SKILL_VERSION = "2.2.0"
SKILL_DESCRIPTION = ("Диагностика зрелости организации для внедрения ИИ-агентов: уровень 1-7 "
                     "и ступень A0-A4, формат внедрения и первый шаг.")
INPUT_SCHEMA = {"type": "object", "properties": {
    "input": {"type": "object", "description": "{индикатор: значение} или {text: \"...\"}"}},
    "required": ["input"]}
OUTPUT_SCHEMA = {"type": "object", "properties": {
    "level": {"type": ["integer", "null"], "minimum": 1, "maximum": 7,
              "description": "null = не наблюдаю (НЕ «уровень 1»)"},
    "level_observed": {"type": "boolean"},
    "stage": {"type": "string", "pattern": "^A[0-4]$"},
    "stage_observed": {"type": "boolean"},
    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    "format": {"type": "string"}, "first_step": {"type": "string"},
    "gaps": {"type": "array", "items": {"type": "string"}}}}
SYSTEM_PROMPT = """Ты — диагност Spiral Maturity. По признакам организации определи:
(1) уровень ценностей 1-7, (2) ступень агентной зрелости A0-A4, (3) формат внедрения, (4) первый шаг.
ОБЯЗАТЕЛЬНО: укажи уверенность (high/medium/low) и какие индикаторы отсутствуют.
Никогда не выставляй уровень по одному признаку. Не выдумывай данные — если признаков мало, confidence=low."""

# лестница A0-A4 (источник: docs/methodology-ru.md)
LADDER = [
    ("A0", ("нет", "не используем", "вручную", "никакого"), "Ручной режим",
     "Выбрать один повторяемый процесс и описать его шаги"),
    ("A1", ("chatgpt", "пробуем", "иногда", "эксперимент", "любопытство"), "Инструмент-помощник",
     "Зафиксировать 2-3 сценария, где ИИ уже помогает, и замерить время"),
    ("A2", ("регламент", "инструкция", "стандарт", "обучение", "промпты", "пробуем"), "Регламентированное использование",
     "Записать промпты и правила в один документ команды"),
    ("A3", ("интеграц", "api", "автоматизац", "в процессе", "воронк", "встроен", "в процессах", "агенты встроены"), "Встроенные агенты",
     "Выбрать процесс со связанными шагами и подключить агента к данным"),
    ("A4", ("автоном", "оркестр", "агенты работают", "само", "метрик"), "Автономные агенты + оркестрация",
     "Замерить эффект агентов в деньгах/часах и расширить на смежный процесс"),
]
LEVEL_PAT = [(1, ("выжива", "хаос", "ручн", "нет процессов")),
             (2, ("контроль", "учёт", "регламент появился", "стабильность")),
             (3, ("прибыль", "эффективность", "оптимизац", "KPI")),
             (4, ("клиент", "сервис", "NPS", "забота")),
             (5, ("команда", "люди", "развитие", "обучение сотрудников")),
             (6, ("миссия", "ценности", "партнёрство", "экосистема")),
             (7, ("влияние", "отрасль", "сообщество", "наследие"))]


NEG_PREFIX = ("нет ", "не ", "никак", "отсутств", "не используем", "вручную", "без ")


NEG_WORDS = ("нет", "не", "никак", "отсутствует", "отсутствуют", "без", "вручную", "никогда")


_ALL_MARKERS = sorted({x for _c, ws, _f, _s in LADDER for x in ws} |
                      {x for _n, ws in LEVEL_PAT for x in ws}, key=len, reverse=True)


def _positive(blob, window=18):
    """Возвращает текст, где маркеры ПОД ОТРИЦАНИЕМ помечены как `~<маркер>`.

    Простое удаление «нет » не работает: «нет регламентов» -> «регламентов» всё ещё
    содержит маркер «регламент». Поэтому идём по маркерам и смотрим, есть ли
    отрицание в окне window символов перед ним.
    """
    out = blob
    for marker in _ALL_MARKERS:
        idx = 0
        while True:
            i = out.find(marker, idx)
            if i < 0:
                break
            left = out[max(0, i - window):i]
            if any(w in left for w in NEG_WORDS):
                out = out[:i] + "~" + out[i:]      # ~маркер = негативный контекст
                idx = i + len(marker) + 1
            else:
                idx = i + len(marker)
    return out


def _has(blob, marker):
    """Маркер присутствует И не помечен отрицанием."""
    return marker in blob and ("~" + marker) not in blob


def run(input_value=None, **kw):
    text = input_value
    if isinstance(text, dict):
        blob = " ".join(str(v) for v in text.values()).lower()
        present = [k for k, v in text.items() if v not in (None, "", False, 0)]
    else:
        blob = str(text or "").lower()
        present = []
    blob = _positive(blob)
    stages = [(c, w, f, s) for c, w, f, s in LADDER if any(_has(blob, x) for x in w)]
    levels = [(n, ) for n, w in LEVEL_PAT if any(_has(blob, x) for x in w)]
    stage_known = bool(stages)
    stage = stages[-1] if stages else LADDER[0]
    level_known = bool(levels)
    level = max(n for (n,) in levels) if levels else None
    gaps = []
    if not present and len(blob.split()) < 25:
        gaps.append("мало наблюдаемых маркеров — нужна диагностика по 16 индикаторами")
    if not level_known:
        gaps.append("уровень ценностей не наблюдаем по входным данным: не угадывать — "
                    "запросить признаки (что важнее: выживание/контроль/прибыль/клиент/команда/миссия/влияние)")
    if stage[0] in ("A0", "A1") and level is not None and level >= 4:
        gaps.append("разрыв: организация зрелая, агенты не используются — быстрый выигрыш")
    if not stage_known:
        gaps.append("ступень агентной зрелости не наблюдаема: нет маркеров использования ИИ")
    # Уверенность выводим из ПОЛНОТЫ наблюдений, а не из длины текста
    conf = "high" if (stage_known and level_known and len(stages) >= 1 and len(levels) >= 1) else \
           ("medium" if (stage_known or level_known) else "low")
    return {"level": level, "level_observed": level_known,
            "stage": stage[0], "stage_observed": stage_known,
            "format": stage[2], "first_step": stage[3],
            "confidence": conf, "gaps": gaps,
            "matched": {"stages": [s[0] for s in stages], "levels": [n for (n,) in levels]},
            "note": ("Оценка по маркерам текста. level=null означает «не наблюдаю уровень» — "
                     "это НЕ «уровень 1». Полная диагностика — 16 индикаторов (SKILL.md).")}
