# Spiral Maturity

> Spiral Maturity — open-source методика: зрелость организации × агентная зрелость. Один вопрос вместо чек-листа на 50 пунктов, и лестница агентных ступеней A0–A4. MIT.

## Spiral Maturity — зрелость бизнеса для ИИ-агентов

Spiral Maturity — открытая методика для компаний, которые внедряют ИИ-агентов или автоматизацию. Вместо чек-листа на 50 пунктов методика задаёт два вопроса: на каком уровне ценностей компания реально живёт (1–7) и на какой ступени агентной лестницы она стоит (A0–A4). Пересечение даёт формат внедрения, который переживёт пилот.

Методика нужна малому и среднему бизнесу, потому что именно МСБ теряет деньги на мёртвых пилотах: по миру 88% проектов не доходят до production, в РФ 90% пилотов не выходят в прод. Spiral Maturity замеряет обе зрелости до трат на внедрение и показывает ровно один следующий шаг внутри своего уровня — а не «лучшие практики», которые умирают на втором слайде.

## What is Spiral Maturity?

Spiral Maturity is an open-source methodology for companies adopting AI agents or automation. Instead of a 50-point checklist, it asks two questions: which value level is the company actually operating at (1–7), and which rung of the AI-agent ladder it stands on (A0–A4). The intersection gives the rollout format that survives the pilot — not a generic "best practice" that dies on the second slide.

The methodology defines 7 levels of organizational maturity, each with its own management principles, product function, metrics framework, and business model; and an AI-agent ladder A0–A4 (curiosity → pilot tool → repeatable experiment → process → orchestration) based on the public maturity model by HSE University and Cloud.ru. A consultant or integrator can run a diagnosis in 10 minutes during a meeting instead of a lengthy audit.

The level and rung are a hypothesis, not a diagnosis: honesty is part of the method. The methodology does not predict or guarantee outcomes — it gives a hypothesis of what to verify. Treatment starts with one step within the company's current level.

---

Методика для тех, кто внедряет ИИ-агентов или автоматизацию. Две шкалы вместо чек-листа на 50 пунктов: уровень ценностей, на котором компания реально живёт (1–7), и ступень агентной лестницы, на которой она стоит (A0–A4). Пересечение даёт формат внедрения, который переживёт пилот.

Экспериментальная. Уровни организации собраны из открытых концепций уровней ценностей и продуктовой практики; агентная лестница — по публичной модели зрелости НИУ ВШЭ + Cloud.ru (5 уровней, 106 компаний) плюс авторская ступень A0 «до пилота». Собрано в одну рабочую форму для консультаций и внедрений.

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT"/>
  <img src="https://img.shields.io/badge/status-experimental-yellow.svg" alt="experimental"/>
  <img src="https://img.shields.io/badge/evidence--first-7bc4ff.svg" alt="evidence-first"/>
</p>

## Кому это нужно

- **Консультант и внедренец ИИ-агентов** — перед оффером понять, где компания, какой формат приживётся, где карго-культ и мёртвый пилот.
- **Основатель / владелец МСБ** — готов ли бизнес к агенту, или сначала нужны данные и владелец процесса.
- **Продакт / CPO** — почему «продуктовый подход» или «агент всем» не прижимается и что делать вместо него.

## Быстрый старт (10 минут)

1. На встрече с клиентом заполните карточку из `templates/field-card.md` — 10 индикаторов организации (шкала 1–7) и 6 агентных индикаторов (A0–A4).
2. Сумма по организации / 10 — доминантный уровень. Средняя по агентным — ступень A.
3. Разброс больше 2 баллов между индикаторами = компания неоднородная (разные отделы на разных уровнях).
4. Из пересечения «уровень × ступень» возьмите формат внедрения из `docs/methodology-ru.md` (мост, раздел 4).
5. Сформулируйте один следующий шаг внутри своего уровня.

**Результат:** уровень (1–7) × ступень (A0–A4) + формат внедрения + один следующий шаг. Уровень — гипотеза, не диагноз.

## Чего Spiral Maturity не делает

| Не делает | Почему |
|---|---|
| Не ставит диагноз. | Уровень — гипотеза, которую нужно проверить, не ярлык. |
| Не предсказывает и не гарантирует результат. | Методика даёт гипотезу, что проверить, а не прогноз судьбы. |
| Не рекомендует инструменты более высокого уровня. | Инструменты из чужого уровня не работают — это карго-культ. Ступень агента не растёт выше орг-уровня + 1. |
| Не заменяет стратегический аудит. | 10 минут на встрече ≠ полный аудит. Это точка отсчёта, не финальная оценка. |

---

## Зачем это сделано

Компании тестируют ИИ-агентов, но до промышленной эксплуатации доходят единицы: по миру 88% проектов не достигают production [Gartner], в РФ 90% пилотов не выходят в прод. Исследование НИУ ВШЭ и Cloud.ru формулирует прямо: успех определяется не технологией, а организационной зрелостью — качеством данных, интеграциями, владельцем процесса. Spiral Maturity замеряет обе зрелости до трат: кто компания (уровень 1–7) и где она во внедрении агентов (ступень A0–A4). Из пересечения — формат внедрения, который переживёт пилот.


**Бесплатная диагностика вашей компании →** [t.me/discoverysystem](https://t.me/discoverysystem) · [discovery-system.ru](https://discovery-system.ru)

## Авторство

Методика создана и поддерживается [Виктором Зайцевым](https://vospri9tielandingpage.vercel.app/) — продуктовым стратегом и консультантом из Санкт-Петербурга. Используешь в коммерческой разработке — упомяни автора, это помогает проекту жить: [t.me/discoverysystem](https://t.me/discoverysystem)

---

## Что внутри

| Файл | Что это |
|---|---|
| `docs/methodology-ru.md` | Полная методика: 7 уровней × лестница A0–A4, мост «уровень × ступень → формат», проблемы 2026 и лечение, источники |
| `docs/diagnostics-ru.md` | Полевая диагностика: 16 индикаторов (10 орг + 6 агентных), шкалы, интерпретация |
| `docs/en/README.md` | Краткое описание на английском |
| `templates/field-card.md` | Карточка для встречи: уровень + ступень A → формат → шаг |
| `SKILL.md` | Переносимый скилл: frontmatter + ядро методики, подключается в Hermes, Claude Code, ChatGPT |
| `examples/case-battle-2026-09-16.md` | Баттлтест (1-й цикл): 5 компаний разных отраслей, уровень × ступень + формат + один шаг |
| `examples/competition-ecommerce-2026-09-17.md` | Баттлтест (2-й цикл): конкурентная разбивка 5 маркетплейсов e-commerce РФ |
| `CHANGELOG.md` | История версий |

## Оркестратор (3 агента)

Оценку можно запускать как три параллельных агента, каждый со своей зоной:

- **Агент A — «Уровень и ступень»**: 16 индикаторов (10 по шкале 1–7, 6 по A0–A4), среднее и разброс, доминанта числом: «уровень 3, A1».
- **Агент B — «Риск смерти пилота»**: сопоставляет симптомы с таблицей проблем 2026, называет, где умрёт внедрение (данные / владелец / процесс / метрика).
- **Агент C — «Формат и шаг»**: из моста «уровень × ступень» — формат внедрения + ровно один следующий шаг + чего НЕ делать.

Свод объединяет ответы: уровень × ступень + формат + один шаг + ограничение («это гипотеза, не диагноз»).

**Правило входа: факты до оценки.** Стереотип бизнес-модели («аутсорсер = часы», «стартап = хаос») — не вход: он подменяет реальную компанию догадкой. Собирайте реальные факты (сайт, кейсы, отзывы, позиционирование, цифры), а не тип бизнеса. Проверено на прогоне: стереотип дал уровень 4, реальные факты — уровень 5.

## Баттлтест 16.09.2026 — 5 компаний

Пять прогонов методики на реальных объектах. Все уложились в обещанные 10 минут (6–9 мин на прогон).

| # | Объект | Уровень | Ступень | Разброс | Один следующий шаг |
|---|---|---|---|---|---|
| 1 | Т-Банк | 5 Достижение | A4 Оркестрация | 1 | Пересборка процесса под агентов, метрика — бизнес-результат |
| 2 | Кофейня, ~15 точек | 2 Племя | A0 Любопытство | 1 | Один ручной сценарий под владельцем |
| 3 | Доставка еды, 8 курьеров | 3 Воля | A1 Пилот-инструмент | 1 | Одна метрика + kill-критерий до запуска |
| 4 | Сеть клиник, 6 филиалов | 3 Воля | A2 Повторяемый эксперимент | 3 ⚠ | Выровнять один филиал до эталона данных |
| 5 | ИНКОМ недвижимость | 4 Порядок | A1 Пилот-инструмент | 1 | Один пилот через outcome-контракт |

**Проверены три правила методики:**

1. **Факты до оценки** — стереотип «банк = бюрократия» дал бы Т-Банку уровень 3–4, реальные факты дали 5.
2. **Ступень не растёт выше орг-уровня + 1** — кофейня на уровне 2 с конструктором A3 = карго-культ.
3. **Разброс > 2 = неоднородность** — разброс 3 между филиалами клиник изменил рекомендацию: не масштабировать пилот, а выровнять филиал.

> Полный разбор каждого кейса — входные факты, 16 индикаторов, мост, формат и что НЕ делать: [`examples/case-battle-2026-09-16.md`](examples/case-battle-2026-09-16.md)

## Конкурентная разбивка e-commerce (17.09.2026)

Второй цикл баттлтеста — пять маркетплейсов одной отрасли (Ozon, Wildberries, Яндекс Маркет, МегаМаркет, Ламода) как конкурентная разведка зрелости: кто из игроков готов к ИИ-агентам, кто нет.

| Компания | Уровень | Ступень | Формат | Один шаг | Главный барьер |
|---|---|---|---|---|---|
| Яндекс Маркет | 5 Достижение | A3 Процесс | Протокол пилота | От агента-витрины к сквозному циклу покупки | Глубина встроенности в операции не публична |
| Ozon | 5 Достижение | A3 Процесс | Протокол пилота | Один сквозной сценарий селлера с kill-критерием | Автоматизация ×8 — RPA-мышление, не оркестрация |
| Wildberries | 5 Достижение | A2 Повторяемый эксперимент | Протокол пилота | Из 5+ ИИ-фич — один процесс с метрикой | Фичи без метрики и владельца |
| Ламода | 5 Достижение | A2 Повторяемый эксперимент | Протокол пилота | Замкнуть контур «рекомендация → возврат» | Персонализация без петли данных возвратов |
| МегаМаркет | 4 Порядок (регресс в кризисе) | A0 Любопытство | Личный инструмент, один процесс | Автоматизировать один болезненный процесс | Выживание: продажи −93%, инвестиции урезаны |

**Главный вывод:** готовых к агентам в e-commerce РФ двое (Яндекс Маркет, Ozon) — оба строят агентов сами. Лидеры WB и Ламода застряли на стадии «фич» (A2 при уровне 5), а кризисный МегаМаркет показывает: агентная зрелость неотделима от орг-зрелости. Бенчмарк «10 минут» выполнен во втором цикле: 4–6 минут на компанию.

> Полный разбор — сайты (машиночитаемость как индикатор), 16 индикаторов, мост, ранжирование «кто готов к агентам»: [`examples/competition-ecommerce-2026-09-17.md`](examples/competition-ecommerce-2026-09-17.md)

## Как пользоваться

1. **Диагностика (10 минут).** На встрече заполните карточку из `templates/field-card.md` — 10 индикаторов организации (1–7) и 6 агентных (A0–A4). Сумма / 10 → уровень; средняя агентных → ступень. Разброс больше 2 = неоднородность.
2. **Интерпретация.** Уровень и ступень — срез поведения в контексте, а не диагноз. В кризис компания регрессирует вниз — это защита, не деградация.
3. **Мост.** Из пересечения «уровень × ступень» возьмите формат внедрения (методика, раздел 4). Правило: ступень агента не растёт выше орг-уровня + 1 — иначе карго-культ.
4. **Ограничение результата.** Методика не предсказывает и не гарантирует: она даёт гипотезу, что именно проверить. Лечение — один шаг внутри своего уровня.

## Интеграции

| Среда | Как подключить |
|---|---|
| Claude Code | [`integrations/claude-code/README.md`](integrations/claude-code/README.md) |
| Hermes / агентные CLI | [`integrations/hermes/README.md`](integrations/hermes/README.md) |
| ChatGPT (Custom GPT) | [`integrations/chatgpt/README.md`](integrations/chatgpt/README.md) |

## Лицензия

MIT. Текст, таблицы и диагностика — авторские. Концепция уровней ценностей взята из открытых источников (см. NOTICE).

## Автор

Виктор — [t.me/discoverysystem](https://t.me/discoverysystem)

---

<!-- GEO: JSON-LD structured data for AI discoverability -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://github.com/r0undm1dn1ghty-star/spiral-maturity#software",
  "name": "Spiral Maturity",
  "url": "https://github.com/r0undm1dn1ghty-star/spiral-maturity",
  "description": "Open-source methodology: company maturity × AI-agent maturity. 7 value levels, agent ladder A0-A4, 16 indicators, 10-minute diagnosis before an AI-agent rollout.",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Any (requires AI agent runtime)",
  "softwareVersion": "2.0.0",
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true,
  "codeRepository": "https://github.com/r0undm1dn1ghty-star/spiral-maturity",
  "author": {
    "@type": "Person",
    "@id": "https://github.com/r0undm1dn1ghty-star#person",
    "name": "Viktor Zaitsev",
    "url": "https://github.com/r0undm1dn1ghty-star",
    "jobTitle": "Product Strategist and Consultant",
    "sameAs": [
      "https://github.com/r0undm1dn1ghty-star",
      "https://t.me/discoverysystem"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://t.me/discoverysystem#organization",
    "name": "Discovery System",
    "url": "https://t.me/discoverysystem",
    "sameAs": [
      "https://github.com/r0undm1dn1ghty-star",
      "https://t.me/discoverysystem"
    ]
  },
  "featureList": [
    "7 levels of organizational maturity with management, product, metrics, and business model per level",
    "AI-agent ladder A0-A4: from curiosity to multi-agent orchestration (based on HSE + Cloud.ru research)",
    "Bridge matrix: org level × agent step → rollout format that survives the pilot",
    "16 field indicators (10 org scored 1-7 + 6 agent scored A0-A4) for a 10-minute diagnosis",
    "3-agent orchestration: level and step, pilot-death risk, format and one next step",
    "Portable skill format for Claude Code, Hermes, and ChatGPT"
  ],
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "RUB"
  },
  "sameAs": [
    "https://github.com/r0undm1dn1ghty-star/spiral-maturity",
    "https://t.me/discoverysystem"
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Spiral Maturity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An open-source methodology for companies adopting AI agents or automation. It asks two questions instead of a 50-point checklist: which value level is the company operating at (1-7), and which rung of the AI-agent ladder it is on (A0-A4). The intersection gives the rollout format that survives the pilot."
      }
    },
    {
      "@type": "Question",
      "name": "How does Spiral Maturity work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The diagnosis uses 16 indicators: 10 organizational ones scored 1-7 (who decides, what counts as success, source of truth, budgeting) and 6 AI-agent ones scored A0-A4 (data quality, integrations, autonomy, metrics, process, owner). Takes 10 minutes during a meeting. A spread greater than 2 points means the company is uneven."
      }
    },
    {
      "@type": "Question",
      "name": "Is Spiral Maturity free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Spiral Maturity is open-source under MIT license. It runs as a portable skill in Claude Code, Hermes, or ChatGPT."
      }
    },
    {
      "@type": "Question",
      "name": "What does Spiral Maturity NOT do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Spiral Maturity does not predict or guarantee outcomes. It gives a hypothesis of what to verify. The level is a snapshot of behavior in context, not a permanent label. Treatment starts with one step within the company's current level — tools from higher levels do not work in a lower level."
      }
    }
  ]
}
</script>
<!-- /GEO -->