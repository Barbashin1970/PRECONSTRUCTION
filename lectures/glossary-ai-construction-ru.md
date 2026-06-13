---
title: Глоссарий — английские термины для лекции «ИИ в строительстве»
purpose: Слова, которые стоит выучить/закрепить, чтобы полнее и увереннее раскрывать тему по-английски
lang: en→ru
---

# Глоссарий для лектора: ИИ в строительстве (EN → RU + как употреблять)

Термины разбиты по темам. Колонка «Заметка» — как и где употреблять, на что сделать акцент.
⭐ — было в лекции (закрепить произношение/точность); ➕ — пробел, добавит глубины теме.

## 1. ИИ / машинное обучение — ядро

| Термин (EN) | Значение (RU) | Заметка |
|---|---|---|
| ⭐ machine learning (ML) | машинное обучение | базовый зонтичный термин |
| ⭐ deep learning | глубокое обучение | «multi-layer neural networks» |
| ⭐ neural network | нейросеть | произносить «NOOR-al» |
| ⭐ supervised / unsupervised / reinforcement learning | обучение с учителем / без учителя / с подкреплением | три типа; reinforcement = «trial and error, rewards/penalties» |
| ⭐ transformer / attention | трансформер / механизм внимания | «the architecture behind LLMs (2017)» |
| ⭐ large language model (LLM) | большая языковая модель | GPT, Gemini, DeepSeek |
| ⭐ generative AI | генеративный ИИ | «creates new content» |
| ⭐ reasoning model | модель с рассуждением | «shows step-by-step reasoning», e.g. DeepSeek R1 |
| ➕ inference | инференс / вывод модели | «running the model in production» (vs training) |
| ➕ training / fine-tuning | обучение / дообучение | fine-tuning = «adapting a model to your domain» |
| ➕ foundation model | базовая (фундаментальная) модель | как у «Норникеля» — обучена на ГОСТ/нормах |
| ➕ embeddings | эмбеддинги / векторные представления | основа семантического поиска |
| ⭐ RAG (retrieval-augmented generation) | генерация с опорой на поиск | «forces the AI to cite authoritative databases» |
| ⭐ hallucination | галлюцинация | «confident but factually wrong output» |
| ➕ grounding | заземление (на источники/факты) | антоним галлюцинации; «ground the answer in sources» |
| ➕ agentic AI / AI agent | агентный ИИ / ИИ-агент | «executes multi-step tasks autonomously» |
| ➕ multi-agent orchestration | оркестрация нескольких агентов | ваш «manager skill + sub-agents» |
| ⭐ prompt engineering | промпт-инжиниринг | «the old technique» |
| ⭐ skill (agent skill) | навык (агента) | «reusable capability package» |
| ➕ MLOps | MLOps (эксплуатация ML) | «deploying, monitoring, retraining models» |
| ➕ model drift | дрейф модели | «accuracy degrades as real-world data changes» |
| ➕ human-in-the-loop | человек в контуре | «final decision stays with the engineer» — ваш ключевой тезис |

## 2. Строительство / AEC + ИИ

| Термин (EN) | Значение (RU) | Заметка |
|---|---|---|
| ⭐ pre-construction (preconstruction) | преконстракшн / предпроектная фаза | ваша «важнейшая фаза» |
| ⭐ BIM (building information modeling) | информационное моделирование зданий | стоит раскрыть глубже — аудитория этого ждёт |
| ➕ digital twin | цифровой двойник | «live virtual replica of the asset» |
| ➕ clash detection | обнаружение коллизий | «finds conflicts between systems in BIM» |
| ➕ quantity takeoff | подсчёт объёмов работ/материалов | ваш кейс с чертежами фасадов |
| ➕ bill of quantities (BoQ) | ведомость объёмов работ | смета по объёмам |
| ➕ scan-to-BIM / point cloud | скан-в-BIM / облако точек | лазерное сканирование существующих зданий — близко вашей реконструкции! |
| ➕ generative design | генеративное проектирование | «AI proposes design options under constraints» |
| ➕ 4D / 5D BIM | 4D (график) / 5D (стоимость) BIM | время и деньги поверх 3D-модели |
| ⭐ computer vision | компьютерное зрение | мониторинг СИЗ, прогресса |
| ⭐ PPE detection | детекция СИЗ | personal protective equipment (каски, жилеты) |
| ➕ predictive maintenance | предиктивное обслуживание | «predict equipment failure before it happens» |
| ➕ as-built (documentation) | исполнительная документация | «what was actually built» |
| ➕ snagging / punch list | список недоделок | дефекты перед сдачей |
| ⭐ compliance checking | проверка соответствия нормам | «against codes/standards» |
| ➕ AEC/O | проектирование-стройка-эксплуатация | Architecture, Engineering, Construction & Operations |
| ➕ commissioning / handover | пусконаладка / сдача объекта | переход к эксплуатации |

## 3. Бизнес / пресейл / экономика проекта

| Термин (EN) | Значение (RU) | Заметка |
|---|---|---|
| ⭐ pre-sales | пресейл | ИТ-аналог преконстракшн |
| ⭐ stakeholder | стейкхолдер / заинтересованная сторона | «present the pitch to stakeholders» |
| ➕ value proposition | ценностное предложение | «why the client should care» |
| ➕ ROI / payback period | окупаемость / срок окупаемости | return on investment |
| ➕ TAM / SAM / SOM | объём рынка (общий/доступный/достижимый) | для оценки рынка |
| ➕ total cost of ownership (TCO) | совокупная стоимость владения | не только цена покупки |
| ➕ procurement | закупки / тендер | «public procurement» = госзакупки |
| ➕ subcontractor | субподрядчик | часто отсекаются дорогими ИИ-внедрениями |
| ➕ scope creep | расползание объёма проекта | антоним антископа |
| ➕ due diligence | комплексная проверка / дью-дилидженс | проверка перед сделкой/стройкой |
| ➕ feasibility study | технико-экономическое обоснование (ТЭО) | «is this worth building?» |

## 4. Полезные «лекторские» обороты (для плавной речи)

| Оборот (EN) | Как использовать |
|---|---|
| "Let me give you a concrete example…" | переход к кейсу (у вас их много — хорошо) |
| "The key takeaway here is…" | выделить главную мысль |
| "A common misconception is that…" | разрушить миф (ИИ = магия) |
| "To put this in perspective…" | дать масштаб цифре |
| "Let's distinguish between A and B" | ваш приём «ИИ vs IoT», «с помощью ИИ vs ИИ внутри» |
| "This is where it gets tricky…" | подвести к сложному (галлюцинации, безопасность) |
| "Rule of thumb:" | эмпирическое правило («multiply by two») |
| "garbage in, garbage out" | про качество данных |

> Произношение, на которое стоит обратить внимание: *hierarchical* (хай-э-РАР-кикл),
> *embeddings* (эм-БЭ-дингз), *agentic* (а-ДЖЕН-тик), *Anthropic* (ан-ТРО-пик),
> *Nemetschek* (НЭ-мет-шек), *facade* (фа-САД), *infrastructure* (ИН-фра-страк-чер).
