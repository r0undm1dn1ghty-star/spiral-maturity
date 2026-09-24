---
name: Spiral Maturity
description: Company maturity × AI-agent maturity — 7 levels, agent ladder A0-A4, 16 indicators, one next step.
license: MIT
---

# Spiral Maturity

A methodology for companies adopting AI agents or automation. Two questions instead of a 50-point checklist: what value level does the company actually live on (1–7), and which rung of the AI-agent ladder is it on (A0–A4). The intersection gives the rollout format that survives the pilot.

The agent ladder follows the public maturity model by HSE University + Cloud.ru (5 levels, 106 companies in production), plus an authorial A0 "pre-pilot" rung. Market check: 46% of Russian companies test AI agents [Yakov & Partners + Yandex], 9% see >5% EBITDA effect, 88% of world projects never reach production [Gartner].

## Levels (summary)

| Level | Driver | Management principle | Product role | Key metric | Business model |
|---|---|---|---|---|---|
| 1. Instinct | Survival, cash gap | Solve by hand, no process | No product, only "goods" | Days of runway | Hand sale, service |
| 2. Tribe | Loyalty, "ours" | Personal trust, rituals | Founder's magic | Repeat purchases | "Neighborhood shop" |
| 3. Will | Power, control | Authoritarian, fear/reward | Product = "orders into code" | Speed and obedience | "Everything through the founder" |
| 4. Order | Rules, predictability | Processes, approvals, hierarchy | Product = fulfilling the spec | Plan vs fact | Contract, vendor |
| 5. Achievement | Market, competition | Goals, bonuses, ROI | Feature factory | Revenue, ARR, retention | SaaS, subscription, marketplace |
| 6. Culture | People, agreement, inclusion | Collegial, empathy | Product = human value | Engagement, eNPS | Service-with-soul, personalization |
| 7. System | Meaning, integration | Bets + causal system | Product = node in the value chain | Learning speed, business impact | Ecosystem/platform |

## Agent ladder A0–A4

| Rung | What it looks like |
|---|---|
| A0 Curiosity | Trying LLMs by hand, copy-paste between windows |
| A1 Pilot tool | Single low-risk pilot: chatbot, text generation |
| A2 Repeatable experiment | Several working scenarios, first API connection |
| A3 Process | Agent embedded in the process, standards, human-in-the-loop |
| A4 Orchestration | Multi-agent end-to-end processes, logging, control, scaled across departments |

Bridge rule: the agent rung does not grow above org level + 1. Putting an A3 process into a level-2 organization is cargo cult.

## Diagnostics

16 indicators in `docs/diagnostics-ru.md` (Russian): 10 organizational scored 1–7 (who decides, what counts as success, source of truth, budgeting) + 6 AI-agent ones scored A0–A4 (data, integrations, autonomy, metrics, process, owner). The average gives the dominant level; a spread above 2 means the company is heterogeneous.

## License

MIT. Text and synthesis are original. The level concept is taken from open sources (see NOTICE).

## Author

Victor — [t.me/discoverysystem](https://t.me/discoverysystem)
