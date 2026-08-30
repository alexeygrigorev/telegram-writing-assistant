# Книги по систематизации и автоматизации бизнеса

**Цель заметки:** собрать книги, которые помогают научиться не просто «автоматизировать задачи», а проектировать бизнес как систему: находить процессы, вытаскивать знания из головы людей, убирать founder bottleneck, стандартизировать работу, выбирать правильные кандидаты для автоматизации и затем переносить это в AI-assisted / agentic workflows.

## Рекомендуемый порядок чтения

1. **SYSTEMology — David Jenyns**
2. **Clockwork: Revised and Expanded — Mike Michalowicz**
3. **Buy Back Your Time — Dan Martell**
4. **Work the System — Sam Carpenter**
5. **The E-Myth Revisited — Michael E. Gerber**
6. **Automate Your Busywork — Aytekin Tank**
7. **Traction — Gino Wickman**
8. **Built to Sell — John Warrillow**
9. **Systems Champion — David Jenyns** *(bonus / продолжение SYSTEMology)*

Этот порядок специально идет не от инструментов к автоматизациям, а от мышления к исполнению:

> **Сначала увидеть бизнес как набор систем → описать их → убрать founder как узкое место → определить, что дорого и повторяемо → стандартизировать → автоматизировать → построить операционную систему вокруг этого.**

Для будущей AI-native методологии это важнее, чем начинать с Zapier, n8n, ChatGPT или Codex. Техническая автоматизация должна появляться после того, как понятны процесс, владелец, входы, выходы, правила, исключения и definition of done.

---

# 1. SYSTEMology — David Jenyns

## Почему читать первой

Из всего списка это, пожалуй, самая близкая книга к задаче «как превратить работающий, но хаотичный бизнес в набор систем, которые можно делегировать и автоматизировать».

Главная проблема, которую решает SYSTEMology: знания о том, как работает компания, обычно находятся в головах нескольких людей. Founder знает одно, operations manager другое, VA третье. Даже если SOP существуют, они часто неполные, устаревшие или никто ими не пользуется.

Jenyns предлагает не пытаться задокументировать всю компанию сразу. Вместо этого — найти критические процессы, определить людей, которые реально умеют их выполнять, и постепенно извлечь из них рабочую систему.

## Главные идеи

Framework SYSTEMology состоит из семи стадий:

1. **Define** — определить ключевые процессы бизнеса.
2. **Assign** — определить, кто лучше всего знает каждый процесс.
3. **Extract** — вытащить процесс из головы этого человека.
4. **Organise** — привести знания к понятной структуре.
5. **Integrate** — встроить систему в реальную работу команды.
6. **Scale** — использовать процессы для роста и делегирования.
7. **Optimise** — постепенно улучшать системы.

Очень важная идея: **founder не должен лично писать все SOP**. Человек, который реально выполняет работу хорошо, часто является лучшим источником процесса.

## Что особенно важно для AI-native automation

Эта книга почти дает первую половину будущей методологии:

> **Domain expert → interview → structured process → repeatable workflow.**

AI добавляет новый слой:

- ChatGPT может интервьюировать process owner;
- AI может находить пропуски и неоднозначности;
- historical examples можно превращать в test cases;
- Codex может превращать процесс в executable workflow;
- AI может поддерживать документацию рядом с реальным исполнением.

То есть возможная формула:

> **SYSTEMology + ChatGPT + Codex = AI-native systemization.**

## Что забирать в будущую программу

- Не автоматизировать компанию целиком; выбирать несколько критических процессов.
- Не заставлять founder писать SOP с нуля.
- Интервьюировать человека на примере **последнего реального выполнения** процесса.
- Документация считается полезной только тогда, когда она встроена в работу.
- Система должна иметь owner'а.

## Практика после книги

Выбрать один повторяемый процесс и провести process extraction interview:

- Что запускает процесс?
- Что приходит на вход?
- Что ты делаешь первым?
- Какие решения принимаешь?
- Что делаешь, если чего-то не хватает?
- Где ищешь информацию?
- Как понимаешь, что работа выполнена хорошо?
- Какое доказательство остается после выполнения?

После этого попросить ChatGPT превратить разговор в структурированную workflow specification.

---

# 2. Clockwork: Revised and Expanded — Mike Michalowicz

## Почему читать второй

SYSTEMology отвечает на вопрос «как описать работу». Clockwork поднимает уровень выше:

> **Почему бизнес вообще продолжает зависеть от founder'а?**

Это очень близко к реальной причине, по которой founder может заплатить много денег за automation / AI transformation.

Часто клиент не думает:

> «Мне нужен агент».

Он думает:

> «Почему все всё равно приходит ко мне?»

> «Почему команда не может решить это без меня?»

> «Почему я постоянно проверяю, напоминаю и разруливаю исключения?»

## Главная идея

Бизнес должен постепенно переставать требовать постоянного участия owner'а в операционном исполнении.

Founder может быть bottleneck не потому, что выполняет много ручных задач, а потому что:

- все ждут его approval;
- только он знает исключения;
- только он помнит, что делать дальше;
- только он видит общую картину;
- только он решает, когда работа считается законченной.

Это более глубокая проблема, чем busywork.

## Что важно для AI-native automation

AI легко может уменьшить execution work и одновременно **усилить founder bottleneck**.

Например:

- AI делает 20 drafts вместо 3;
- founder теперь должен проверить 20 drafts;
- automation ускоряет создание задач;
- founder должен принимать еще больше решений;
- agents производят больше артефактов;
- никто, кроме founder'а, не знает, что с ними делать.

Поэтому цель автоматизации должна быть не просто:

> **больше output**

а:

> **меньше зависимости бизнеса от founder attention.**

## Что забирать в будущую программу

- Диагностировать bottleneck прежде, чем строить automation.
- Смотреть на approvals, exceptions и decisions, а не только на manual clicks.
- Не считать automation успешной, если founder становится full-time reviewer.
- После автоматизации должен быть понятен новый owner процесса.

## Практика после книги

Составить список из 20 действий, которые за последнюю неделю потребовали участия founder'а.

Разделить их на:

- действительно founder-only;
- можно делегировать человеку;
- можно формализовать;
- можно автоматизировать;
- можно выполнять AI с human approval;
- вообще не нужно делать.

Это может стать сильным упражнением для Week 1 будущей программы.

---

# 3. Buy Back Your Time — Dan Martell

## Почему читать третьей

Эта книга хорошо отвечает на вопрос:

> **Что систематизировать и автоматизировать первым?**

Очень легко начать автоматизировать то, что технически интересно: social posts, email summaries, meeting notes.

Но premium automation должна начинаться с того, что **экономически дорого**.

## Главная идея

Founder должен постепенно «выкупать» свое время, удаляя из своей жизни работу, которую может выполнять кто-то или что-то другое с достаточным качеством.

Это заставляет смотреть на automation как на allocation problem:

- Где уходит дорогое время?
- Какие задачи повторяются?
- Какие из них не требуют founder judgment?
- Какие можно стандартизировать?
- Где результат освобождает capacity, а не просто экономит несколько кликов?

## Почему это важно для $10k offer

Хороший premium automation project должен иметь понятную экономику.

Например:

Плохой кандидат:

> founder тратит 20 минут в неделю на публикацию поста.

Сильный кандидат:

> founder и Head of Ops вместе тратят 12 часов в неделю на client reporting, follow-ups и проверку входящих данных.

Поэтому полезная формула:

> **Don't automate what's easy. Automate what's expensive.**

## Что забирать в будущую программу

Automation backlog нужно сортировать не по «coolness», а по:

- частоте;
- стоимости времени;
- влиянию на revenue;
- влиянию на capacity;
- риску ошибок;
- скорости выполнения;
- зависимости от founder'а.

## Практика после книги

Создать таблицу automation opportunities:

| Process | Hours/month | Whose time | Delay cost | Error cost | Founder dependency | Automatable? |
|---|---:|---|---:|---:|---:|---:|

После этого выбрать один процесс, который имеет максимально сильную комбинацию **value × repeatability × feasibility**.

---

# 4. Work the System — Sam Carpenter

## Главная идея

Бизнес не является одной огромной хаотичной сущностью.

Это набор отдельных систем:

- sales;
- onboarding;
- customer support;
- newsletter;
- podcast;
- bookkeeping;
- recruiting;
- event production;
- reporting;
- content distribution;
- sponsor operations.

Каждую систему можно рассматривать отдельно, наблюдать, документировать, измерять и улучшать.

Это простая мысль, но она сильно меняет подход к automation.

## Почему это важно

Плохая постановка задачи:

> «Мы хотим AI-transform наш бизнес».

Хорошая:

> «Каждый понедельник мы готовим client performance report. Давайте разберем именно эту систему».

Чем меньше начальная система, тем легче:

- увидеть trigger;
- определить inputs;
- описать decisions;
- найти exceptions;
- измерить результат;
- построить automation;
- проверить reliability.

## Что забирать в будущую программу

Вместо AI transformation map компании можно сначала делать **System Inventory**.

Например:

- Marketing systems
- Sales systems
- Delivery systems
- Customer systems
- Finance systems
- People systems
- Management systems

А уже внутри каждой области — конкретные recurring workflows.

## Практика после книги

За 30 минут выписать все повторяемые системы компании.

Потом отметить:

- где founder участвует лично;
- где работа делается минимум раз в неделю;
- где есть понятный результат;
- где уже существуют examples / SOP / templates;
- где чаще всего происходят ошибки или задержки.

Это дает карту для automation discovery.

---

# 5. The E-Myth Revisited — Michael E. Gerber

## Почему эта старая книга до сих пор важна

Одна из центральных идей E-Myth:

> Хороший специалист, открывший бизнес, очень легко создает себе не компанию, а новую работу.

Вместо того чтобы строить систему, он становится незаменимым человеком внутри нее.

Gerber предлагает мысленно проектировать компанию так, словно ее придется воспроизводить снова и снова — почти как franchise prototype.

## Связь с AI

Классическая версия идеи:

> **Design the business so another human can run it.**

AI-native версия:

> **Design the business so humans and agents can run it together.**

Это не означает убрать людей. Наоборот: нужно четко определить, где человеческое judgment, relationship и accountability незаменимы, а где работа может быть формализована.

## Что забирать в будущую программу

- Не автоматизировать founder heroics.
- Сначала спросить: «Как выглядел бы этот процесс, если бы его завтра выполнял новый сотрудник?»
- Потом: «Какая часть инструкции достаточно ясна для AI?»
- И только потом: «Что должен построить Codex?»

## Практика после книги

Взять процесс, который сейчас зависит от одного человека, и написать:

> «Если этот человек завтра исчезнет на месяц, что нужно знать другому человеку, чтобы процесс продолжал работать?»

Все неизвестное — operational debt.

---

# 6. Automate Your Busywork — Aytekin Tank

## Почему эта книга ближе всего к automation в буквальном смысле

Aytekin Tank, founder Jotform, пишет непосредственно про поиск repetitive work и перевод его в automated workflows.

Это уже более tactical книга, чем SYSTEMology или Clockwork.

## Полезный framework

Один из ключевых циклов:

1. **Divide & Conquer** — разбить работу на отдельные части.
2. **Design & Implement** — спроектировать workflow и реализовать его.
3. **Refine & Iterate** — улучшать после реального использования.

## Ограничение книги

Книга появилась до нынешнего зрелого поколения coding agents и поэтому во многом отражает no-code / workflow automation эпоху.

Сейчас nontechnical operator с ChatGPT + Codex может построить гораздо больше:

- custom scripts;
- data transformations;
- file workflows;
- lightweight internal tools;
- API integrations;
- report generators;
- knowledge workflows;
- reusable agents.

Поэтому книгу лучше воспринимать не как каталог современных инструментов, а как framework для поиска automation opportunities.

## Что забирать в будущую программу

Очень сильный opening exercise:

> «Какие повторяющиеся вещи ты сделал за последние две недели?»

Для каждого пункта:

- сколько раз;
- сколько времени;
- одинаковы ли inputs;
- одинаков ли expected output;
- сколько judgment;
- какие exceptions;
- что можно проверить автоматически;
- нужен ли human approval.

## Практика после книги

Собрать **Automation Backlog** минимум из 20 задач и процессов.

Не строить ничего, пока список не отсортирован по value и risk.

---

# 7. Traction — Gino Wickman

## Зачем книга про EOS в списке automation

Traction не про AI и не про автоматизацию. Она полезна как пример того, что означает **operating system компании**.

EOS (Entrepreneurial Operating System) пытается сделать явными:

- priorities;
- ownership;
- metrics;
- accountability;
- recurring meeting cadence;
- processes;
- issue solving.

AI automation без этих слоев легко превращается в набор disconnected bots.

## Что особенно полезно

Автоматизированный workflow должен существовать внутри management system:

- Кто owner?
- Как мы видим, что он работает?
- Какая метрика показывает health?
- Что происходит при failure?
- Кто разбирает исключения?
- Когда процесс пересматривается?

То есть AI не отменяет management. Хорошая автоматизация делает management более observable.

## Что забирать в будущую программу

Каждый production workflow должен иметь минимум:

- owner;
- KPI / health metric;
- cadence review;
- escalation path;
- backlog of improvements.

## Практика после книги

Для выбранной automation написать одну карточку:

**Owner**  
**Purpose**  
**Trigger**  
**KPI**  
**Failure signal**  
**Escalation**  
**Review cadence**

Если эти поля невозможно заполнить, automation еще недостаточно встроена в бизнес.

---

# 8. Built to Sell — John Warrillow

## Главная идея

Книга показывает, почему founder-dependent и сильно кастомизированный бизнес трудно масштабировать и трудно продать.

Чтобы сделать бизнес более независимым от founder'а, нужно:

- сузить предложение;
- стандартизировать delivery;
- уменьшить bespoke work;
- создать repeatable process;
- убрать личное участие owner'а из каждой сделки и каждого проекта.

## Почему это интересно для automation

Лучше всего автоматизируются процессы, которые уже имеют некоторую repeatability.

Если каждая продажа, каждый клиент и каждый deliverable устроены полностью по-разному, automation постоянно сталкивается с exceptions.

Поэтому иногда перед automation нужно не больше AI, а **productization**.

Например:

Плохо:

> «Каждому клиенту мы делаем совершенно уникальный onboarding».

Лучше:

> «80% onboarding одинаковы, 20% — controlled exceptions».

Это уже намного более сильная база для Codex / agents.

## Что забирать в будущую программу

Перед автоматизацией спросить:

> **Можно ли сначала сделать сам бизнес-процесс более стандартным?**

Иногда лучший automation move — удалить variation.

## Практика после книги

Для одного recurring процесса выписать все варианты исполнения.

Разделить их на:

- genuinely necessary variation;
- historical accident;
- preference;
- exception;
- unnecessary complexity.

Попробовать удалить 30–50% variation до автоматизации.

---

# 9. Systems Champion — David Jenyns

## Статус в списке

Это bonus / продолжение SYSTEMology, особенно полезное после того, как стало понятно, что системы не живут сами по себе.

Главная тема — роль человека, который отвечает за то, чтобы систематизация реально происходила внутри компании.

## Почему это важно для AI automation

Очень вероятно, что для AI-native компании появится аналогичная роль:

> **AI Operations / Systems Champion**

Не обязательно инженер.

Это может быть сильный operator, Chief of Staff или operations manager, который умеет:

- разговаривать с process owners;
- превращать знания в structured workflows;
- работать с ChatGPT / Codex;
- тестировать автоматизации;
- отслеживать failures;
- поддерживать документацию;
- постепенно улучшать процессы.

В premium-программе это может быть второй участник от компании вместе с founder'ом.

## Практика после книги

Определить, кто внутри компании может стать Systems / AI Operations Champion.

Проверить, есть ли у этого человека:

- process curiosity;
- authority менять workflows;
- достаточно technical confidence;
- дисциплина документировать;
- понимание бизнеса;
- желание поддерживать системы после запуска.

---

# Как эти книги складываются в одну методологию

Можно видеть их как одну цепочку.

## Gerber — The E-Myth Revisited

> **Build a business, not a job.**

Компания не должна полностью зависеть от личного исполнения founder'а.

↓

## Carpenter — Work the System

> **A business is a collection of systems.**

Разделяем хаос на отдельные процессы.

↓

## Jenyns — SYSTEMology

> **Extract the systems from people's heads.**

Фиксируем operational knowledge.

↓

## Michalowicz — Clockwork

> **Remove the founder as the bottleneck.**

Находим места, где компания все еще требует founder attention.

↓

## Martell — Buy Back Your Time

> **Prioritize expensive work.**

Выбираем процессы, где освобождение capacity имеет реальную стоимость.

↓

## Warrillow — Built to Sell

> **Standardize before scaling.**

Убираем лишнюю вариативность.

↓

## Tank — Automate Your Busywork

> **Turn repeatable work into workflows.**

Строим automation backlog и первые процессы.

↓

## Wickman — Traction

> **Put the workflows inside an operating system.**

Owner, metrics, cadence, accountability, escalation.

↓

## AI-native extension

И здесь появляется современная часть, которую старые книги почти не покрывают:

> **Turn documented, economically valuable workflows into systems that humans and AI agents can execute together.**

Примерный цикл:

1. **Find** — найти дорогую recurring систему.
2. **Map** — разобрать реальный текущий процесс.
3. **Simplify** — убрать unnecessary variation.
4. **Specify** — сделать процесс понятным человеку и агенту.
5. **Build** — использовать ChatGPT + Codex для реализации.
6. **Test** — проверить happy paths, missing inputs, edge cases и dangerous cases.
7. **Approve** — оставить human gates там, где это важно.
8. **Run** — встроить в реальную операционную работу.
9. **Measure** — время, cost, errors, throughput, founder dependency.
10. **Improve** — обновлять system после реальных failures и exceptions.

Это и может стать основой AI-native business automation methodology.

---

# Если слушать книги как исследование будущего курса

Не стоит просто прослушивать их подряд. После каждой книги полезно вытаскивать один артефакт.

| После книги | Сделать |
|---|---|
| SYSTEMology | Process Extraction Template |
| Clockwork | Founder Bottleneck Audit |
| Buy Back Your Time | Automation ROI Backlog |
| Work the System | Company Systems Map |
| The E-Myth Revisited | Founder-Independent Process Test |
| Automate Your Busywork | Automation Candidate Inventory |
| Traction | Workflow Ownership & Metrics Card |
| Built to Sell | Process Standardization Audit |
| Systems Champion | AI Operations Champion Role Definition |

Если эти артефакты окажутся полезными на собственных операциях, они могут затем стать worksheets / templates premium-программы.

---

# Главная гипотеза

Большинство книг заканчиваются примерно здесь:

> **Document → standardize → delegate → automate.**

Но coding agents добавили новый слой.

Теперь non-programmer может не только подключить готовый Zapier workflow, но и с помощью AI построить собственное программное исполнение процесса.

Поэтому новая возможность выглядит так:

> **Научить founder'ов и operators превращать operational knowledge в software-assisted operating capacity — без необходимости становиться программистами.**

DataOps может служить глубоким reference implementation этой идеи, но не обязательным продуктом или архитектурой для участников. Главное — передать принципы, по которым человек может построить более простой AI-native operating system для своей компании.
