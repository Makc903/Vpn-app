<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Поле — Бизнес-план настольной игры | Группа 7/89</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', 'Georgia', serif;
            background: #eef1f5;
            color: #1e2a3a;
            line-height: 1.7;
            padding: 40px 20px;
        }
        .container {
            max-width: 1100px;
            margin: 0 auto;
            background: #ffffff;
            padding: 60px 70px;
            border-radius: 16px;
            box-shadow: 0 8px 40px rgba(0, 40, 80, 0.12);
        }

        /* ===== ШАПКА ===== */
        .header {
            margin-bottom: 20px;
            padding-bottom: 25px;
            border-bottom: 4px solid #1a4d7a;
        }
        .header-text h1 {
            font-size: 2.6em;
            color: #0f2a44;
            letter-spacing: -1px;
            line-height: 1.1;
        }
        .header-text .subtitle {
            font-size: 1.1em;
            color: #5a6b7c;
            font-style: italic;
            margin-top: 5px;
        }

        h2 {
            font-size: 1.9em;
            color: #0f2a44;
            margin-top: 60px;
            margin-bottom: 20px;
            padding-left: 15px;
            border-left: 6px solid #1a4d7a;
        }
        h3 {
            font-size: 1.3em;
            color: #1a4d7a;
            margin-top: 35px;
            margin-bottom: 12px;
        }
        h4 {
            font-size: 1.1em;
            color: #1e2a3a;
            margin-top: 25px;
            margin-bottom: 8px;
            font-weight: 600;
        }
        p {
            margin-bottom: 15px;
            text-align: justify;
        }
        ul, ol {
            margin-left: 25px;
            margin-bottom: 20px;
        }
        li {
            margin-bottom: 8px;
        }

        .highlight {
            background: #eaf2fa;
            border-left: 5px solid #1a4d7a;
            padding: 20px 25px;
            margin: 25px 0;
            border-radius: 0 8px 8px 0;
        }
        .highlight strong {
            color: #0f2a44;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.95em;
        }
        th {
            background: #0f2a44;
            color: #fff;
            padding: 14px 12px;
            text-align: left;
            font-weight: 600;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #dce3ea;
            vertical-align: top;
        }
        tr:nth-child(even) {
            background: #f7f9fc;
        }

        .badge {
            display: inline-block;
            background: #1a4d7a;
            color: #fff;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 600;
            margin-right: 8px;
            margin-bottom: 5px;
        }
        .badge-accent {
            background: #c9a84c;
            color: #1e2a3a;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin: 25px 0;
        }
        .card {
            background: #f7f9fc;
            border: 1px solid #dce3ea;
            border-radius: 10px;
            padding: 25px;
        }
        .card h4 {
            margin-top: 0;
            color: #0f2a44;
        }
        .number {
            font-size: 2.2em;
            font-weight: 700;
            color: #1a4d7a;
            line-height: 1;
        }

        /* ===== КАРТОЧКИ ПРИМЕРОВ ===== */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .game-card {
            border: 1px solid #dce3ea;
            border-radius: 12px;
            overflow: hidden;
            background: #fff;
            box-shadow: 0 2px 12px rgba(0, 40, 80, 0.06);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .game-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0, 40, 80, 0.12);
        }
        .game-card-header {
            padding: 14px 18px;
            font-weight: 700;
            font-size: 0.95em;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .game-card-header.blue {
            background: #1a4d7a;
            color: #fff;
        }
        .game-card-header.green {
            background: #2c5e3f;
            color: #fff;
        }
        .game-card-header.gold {
            background: #c9a84c;
            color: #1e2a3a;
        }
        .game-card-header.red {
            background: #8b3a3a;
            color: #fff;
        }
        .game-card-body {
            padding: 18px;
            font-size: 0.92em;
        }
        .game-card-body .label {
            font-size: 0.8em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #7a8a9a;
            margin-bottom: 4px;
        }
        .game-card-body .value {
            margin-bottom: 14px;
            font-weight: 500;
        }
        .game-card-body .value:last-child {
            margin-bottom: 0;
        }
        .quote {
            font-style: italic;
            color: #4a5a6a;
            border-left: 3px solid #c9a84c;
            padding-left: 12px;
            margin: 10px 0;
            font-size: 0.95em;
        }
        .card-tag {
            display: inline-block;
            font-size: 0.75em;
            padding: 2px 10px;
            border-radius: 12px;
            background: #eaf2fa;
            color: #1a4d7a;
            font-weight: 600;
            margin-right: 5px;
        }
        .card-tag.gold {
            background: #fdf3d9;
            color: #8a6d1f;
        }

        .footer {
            margin-top: 70px;
            padding-top: 30px;
            border-top: 2px solid #dce3ea;
            text-align: center;
            color: #7a8a9a;
            font-size: 0.9em;
        }
        .footer a {
            color: #1a4d7a;
            text-decoration: none;
        }

        .toc {
            background: #f0f3f7;
            padding: 30px 35px;
            border-radius: 10px;
            margin: 30px 0;
        }
        .toc h3 {
            margin-top: 0;
            color: #0f2a44;
        }
        .toc ol {
            margin-bottom: 0;
        }
        .toc a {
            color: #1a4d7a;
            text-decoration: none;
            font-weight: 500;
        }
        .toc a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .container { padding: 30px 20px; }
            .header-text h1 { font-size: 1.8em; }
            .grid-2 { grid-template-columns: 1fr; }
            .cards-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">

        <!-- ===== ШАПКА ===== -->
        <div class="header">
            <div class="header-text">
                <h1>🎲 «ПОЛЕ»</h1>
                <p class="subtitle">Настольная игра о социологии — от Ассоциации «Группа 7/89»<br>Бизнес-план и концепция проекта</p>
            </div>
        </div>

        <!-- ===== СОДЕРЖАНИЕ ===== -->
        <div class="toc">
            <h3>📑 Содержание</h3>
            <ol>
                <li><a href="#idea">Резюме проекта</a></li>
                <li><a href="#concept">Концепция игры</a></li>
                <li><a href="#mechanics">Ключевые механики</a></li>
                <li><a href="#structure">Структура и компоненты</a></li>
                <li><a href="#cards">Примеры карт</a></li>
                <li><a href="#market">Анализ рынка и аудитория</a></li>
                <li><a href="#value">Ценность для Ассоциации</a></li>
                <li><a href="#finance">Финансовая модель</a></li>
                <li><a href="#roadmap">Дорожная карта</a></li>
                <li><a href="#online">Онлайн-версия</a></li>
                <li><a href="#risks">Риски и их снижение</a></li>
                <li><a href="#summary">Итоги и призыв к действию</a></li>
            </ol>
        </div>

        <!-- ==================== 1. РЕЗЮМЕ ==================== -->
        <h2 id="idea">1. Резюме проекта</h2>

        <div class="highlight">
            <strong>«Поле»</strong> — это настольная игра, которая превращает социологию в увлекательное соревнование. Игроки становятся исследовательскими компаниями: собирают данные, строят выборки, защищают отчёты и балансируют между прибылью и профессиональной этикой.
        </div>

        <p><strong>Ключевая идея:</strong> сделать социологию понятной, интересной и обсуждаемой — от офиса Ассоциации до студенческой аудитории. Игра создаётся профессиональным сообществом «Группа 7/89» и использует реальные кейсы из книги <em>«А вы точно социологи?»</em> <strong>(а также любых других книг — можно добавлять любые произведения и создавать лимитированные версии с эксклюзивными событиями из первых уст, истории, которые вы нигде не услышите)</strong>.</p>

        <div class="grid-2">
            <div class="card">
                <div class="number">6</div>
                <h4>Уникальных изюминок</h4>
                <p>Живая выборка, эффект интервьюера, этическая шкала, двойное дно данных, кооператив против кризиса, реальные кейсы.</p>
            </div>
            <div class="card">
                <div class="number">4</div>
                <h4>Режима сложности</h4>
                <p>Экспресс (5 мин), Базовый, Стандарт, Продвинутый. От пасьянса до кампании.</p>
            </div>
            <div class="card">
                <div class="number">1–6+</div>
                <h4>Игроков</h4>
                <p>Один, дуэль, компания. Универсальность для любого стола.</p>
            </div>
            <div class="card">
                <div class="number">10</div>
                <h4>Тестовых экземпляров</h4>
                <p>Пилотный тираж для плейтестов, презентаций и апробации в вузах.</p>
            </div>
        </div>

        <!-- ==================== 2. КОНЦЕПЦИЯ ==================== -->
        <h2 id="concept">2. Концепция игры</h2>

        <h3>2.1. Название и жанр</h3>
        <p><strong>Название:</strong> «Поле» — короткое, ёмкое, отсылает к социологии, но интригует непосвящённых.</p>
        <p><strong>Жанр:</strong> евростратегия с элементами кооперации и соревнования. Лёгкий дедуктивный и ресурсный компонент.</p>

        <h3>2.2. Целевая аудитория</h3>
        <ul>
            <li><strong>Сотрудники исследовательских компаний</strong> — социологи, аналитики, менеджеры проектов.</li>
            <li><strong>Студенты</strong> социологических и маркетинговых специальностей.</li>
            <li><strong>Клиенты агентств</strong> — для тимбилдинга и демонстрации ценности исследований.</li>
            <li><strong>Широкая аудитория</strong> — все, кто интересуется социологией.</li>
        </ul>

        <h3>2.3. Главная идея</h3>
        <p>Игроки — исследовательские компании, которые борются за контракты, собирают данные, строят выборки и защищают отчёты перед заказчиком. Побеждает тот, кто наберёт больше <strong>репутации</strong> и <strong>прибыли</strong>, соблюдая профессиональную этику.</p>

        <!-- ==================== 3. МЕХАНИКИ ==================== -->
        <h2 id="mechanics">3. Ключевые механики</h2>

        <h3>3.1. Базовый цикл хода (5 фаз)</h3>
        <ol>
            <li><strong>Бриф</strong> — получение карты заказчика.</li>
            <li><strong>Планирование</strong> — выбор метода исследования.</li>
            <li><strong>Поле</strong> — сбор данных, броски, опрос респондентов.</li>
            <li><strong>Анализ</strong> — двойное дно: правда или подгонка.</li>
            <li><strong>Отчёт</strong> — презентация, голосование, оплата.</li>
        </ol>

        <h3>3.2. Шесть уникальных изюминок</h3>

        <table>
            <tr>
                <th style="width: 25%;">Изюминка</th>
                <th>Суть</th>
                <th style="width: 30%;">Почему это ново</th>
            </tr>
            <tr>
                <td><span class="badge">1</span> Живая выборка</td>
                <td>Фишки респондентов двигаются по карте города между раундами.</td>
                <td>В массовых настолках нет динамической выборки — обычно всё статично.</td>
            </tr>
            <tr>
                <td><span class="badge">2</span> Эффект интервьюера</td>
                <td>У каждого игрока скрытый модификатор к типам респондентов.</td>
                <td>Социальная психология в настолке — редкость.</td>
            </tr>
            <tr>
                <td><span class="badge">3</span> Этическая шкала</td>
                <td>Трек этики 0–10: можно срезать углы, но это влияет на финал.</td>
                <td>Профессиональная этика как игровая механика — почти не встречается.</td>
            </tr>
            <tr>
                <td><span class="badge">4</span> Двойное дно данных</td>
                <td>Карты отчётов имеют две стороны: «для заказчика» и «реальность».</td>
                <td>Механика сокрытия информации и морального выбора — уникальна.</td>
            </tr>
            <tr>
                <td><span class="badge">5</span> Кооператив против кризиса</td>
                <td>Все игроки — одна компания против колоды кризисов.</td>
                <td>Кооператив в теме социологии не использовался.</td>
            </tr>
            <tr>
                <td><span class="badge">6</span> Реальный кейс</td>
                <td>Карты на основе книги «А вы точно социологи?» <strong>(и любых других книг — с возможностью создавать лимитированные версии с эксклюзивными историями из первых уст)</strong>.</td>
                <td>Прямая связь с реальным профессиональным сообществом. Возможность коллабораций с авторами и издательствами.</td>
            </tr>
        </table>

        <!-- ==================== 4. СТРУКТУРА ==================== -->
        <h2 id="structure">4. Структура и компоненты</h2>

        <h3>4.1. Игровое поле</h3>
        <p>Карта города с <strong>6 районами</strong>: Центр, Спальный, Промзона, Пригород, Деревня, Студенческий квартал. В каждом районе — свои типы респондентов.</p>

        <h3>4.2. Компоненты коробки</h3>
        <table>
            <tr><th>Компонент</th><th>Кол-во</th></tr>
            <tr><td>Игровое поле</td><td>1</td></tr>
            <tr><td>Планшеты игроков</td><td>6</td></tr>
            <tr><td>Карты заказчиков</td><td>30 (включая 6 реальных кейсов)</td></tr>
            <tr><td>Карты методов</td><td>15</td></tr>
            <tr><td>Карты респондентов</td><td>60 (включая 12 баек из книги)</td></tr>
            <tr><td>Карты рисков</td><td>20</td></tr>
            <tr><td>Карты событий</td><td>20</td></tr>
            <tr><td>Карты этических дилемм</td><td>15</td></tr>
            <tr><td>Карты интервьюеров</td><td>6</td></tr>
            <tr><td>Фишки респондентов</td><td>15</td></tr>
            <tr><td>Жетоны денег и репутации</td><td>80+</td></tr>
            <tr><td>Кубики d6</td><td>4</td></tr>
            <tr><td>Правила (2 буклета)</td><td>1 комплект</td></tr>
        </table>

        <h3>4.3. Режимы игры</h3>
        <table>
            <tr><th>Режим</th><th>Время</th><th>Для кого</th></tr>
            <tr><td><strong>Экспресс-Поле</strong></td><td>5–10 мин</td><td>Первый контакт, 1–4+ игроков</td></tr>
            <tr><td><strong>Базовый</strong></td><td>45–60 мин</td><td>Новички</td></tr>
            <tr><td><strong>Стандарт</strong></td><td>60–90 мин</td><td>Обычные игроки</td></tr>
            <tr><td><strong>Продвинутый</strong></td><td>90–120 мин</td><td>Опытные, кооператив</td></tr>
            <tr><td><strong>Кампания</strong></td><td>2+ часа</td><td>Социологи, серия партий</td></tr>
        </table>

        <!-- ==================== 5. ПРИМЕРЫ КАРТ ==================== -->
        <h2 id="cards">5. Примеры карт</h2>

        <p>Ниже — примеры карт из будущей игры. Они показывают, как реальные байки из книги <em>«А вы точно социологи?»</em> превращаются в игровые механики. <strong>Аналогично можно интегрировать любые другие книги — с созданием лимитированных версий и эксклюзивных историй из первых уст.</strong></p>

        <h3>5.1. Карты заказчиков</h3>
        <div class="cards-grid">

            <div class="game-card">
                <div class="game-card-header blue">
                    <span>🏛 Госсектор</span>
                    <span>Бюджет: 3</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Задание</div>
                    <div class="value">Узнать, почему молодёжь не ходит на выборы</div>
                    <div class="label">Срок</div>
                    <div class="value">2 раунда</div>
                    <div class="label">Особое условие</div>
                    <div class="value">Данные должны быть репрезентативны по возрасту</div>
                    <div class="quote">«Нам нужны честные данные. Но если они будут слишком честными — мы вас не поймём».</div>
                    <div><span class="card-tag">Реальный кейс</span></div>
                </div>
            </div>

            <div class="game-card">
                <div class="game-card-header green">
                    <span>🏢 Бизнес</span>
                    <span>Бюджет: 4</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Задание</div>
                    <div class="value">Выяснить, почему падают продажи кофе в офисах</div>
                    <div class="label">Срок</div>
                    <div class="value">1 раунд</div>
                    <div class="label">Особое условие</div>
                    <div class="value">Заказчик не хочет слышать про цену</div>
                    <div class="quote">«Мы уже знаем, что дело не в цене. Найдите другую причину».</div>
                    <div><span class="card-tag gold">Двойное дно</span></div>
                </div>
            </div>

            <div class="game-card">
                <div class="game-card-header gold">
                    <span>🤝 НКО</span>
                    <span>Бюджет: 2</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Задание</div>
                    <div class="value">Оценить потребности бездомных в приютах</div>
                    <div class="label">Срок</div>
                    <div class="value">2 раунда</div>
                    <div class="label">Особое условие</div>
                    <div class="value">Этика: подгонка данных карается строже (−2 вместо −1)</div>
                    <div class="quote">«Мы работаем с людьми, которым и так тяжело. Не подведите».</div>
                    <div><span class="card-tag">Реальный кейс</span></div>
                </div>
            </div>

        </div>

        <h3>5.2. Карты респондентов (из книги)</h3>
        <div class="cards-grid">

            <div class="game-card">
                <div class="game-card-header blue">
                    <span>👤 Мужчина, 54 года</span>
                    <span>Промзона</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Цитата</div>
                    <div class="quote">«— Скажите, сколько человек проживает в вашем домохозяйстве?<br>— А кошку и холодильник считать?»</div>
                    <div class="label">Реакция</div>
                    <div class="value">Шум. Если включить в выборку — заказчик не поймёт (−1 репутация).</div>
                    <div><span class="card-tag gold">Байка из книги</span></div>
                </div>
            </div>

            <div class="game-card">
                <div class="game-card-header green">
                    <span>👩 Женщина, 34 года</span>
                    <span>Спальный район</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Цитата</div>
                    <div class="quote">«Я вам сейчас всё расскажу, только вы не записывайте. А то потом позвонят и будут предлагать пластиковые окна».</div>
                    <div class="label">Реакция</div>
                    <div class="value">Ценные данные. +1 к качеству выборки.</div>
                    <div><span class="card-tag gold">Байка из книги</span></div>
                </div>
            </div>

            <div class="game-card">
                <div class="game-card-header gold">
                    <span>🧑 Студент, 19 лет</span>
                    <span>Студенческий квартал</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Цитата</div>
                    <div class="quote">«Социология? Это где спрашивают, что я думаю, а потом пишут, что я думаю не то?»</div>
                    <div class="label">Реакция</div>
                    <div class="value">Ироничный, но честный. +1 к репутации, если включить.</div>
                    <div><span class="card-tag gold">Байка из книги</span></div>
                </div>
            </div>

        </div>

        <h3>5.3. Карты событий и рисков</h3>
        <div class="cards-grid">

            <div class="game-card">
                <div class="game-card-header red">
                    <span>⚠ Событие</span>
                    <span>Кризис</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Название</div>
                    <div class="value">«Скандал в отрасли»</div>
                    <div class="label">Эффект</div>
                    <div class="value">Все игроки теряют 1 репутацию. Тот, у кого этика ниже 3, теряет 2.</div>
                    <div class="quote">«В СМИ попала информация о фальсификации данных в одном из агентств. Доверие к опросам падает».</div>
                </div>
            </div>

            <div class="game-card">
                <div class="game-card-header red">
                    <span>⚠ Риск</span>
                    <span>Поле</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Название</div>
                    <div class="value">«Отказ от ответа»</div>
                    <div class="label">Эффект</div>
                    <div class="value">Респондент отказывается отвечать. Бросок d6: на 1–2 карта остаётся с меткой «отказ».</div>
                    <div class="quote">«— Я не буду это обсуждать. До свидания».</div>
                </div>
            </div>

            <div class="game-card">
                <div class="game-card-header red">
                    <span>⚠ Дилемма</span>
                    <span>Этика</span>
                </div>
                <div class="game-card-body">
                    <div class="label">Название</div>
                    <div class="value">«Заказчик просит подогнать»</div>
                    <div class="label">Выбор</div>
                    <div class="value">
                        <strong>А)</strong> Подогнать: +3 деньги, −1 этика.<br>
                        <strong>Б)</strong> Сказать правду: +1 репутация, +1 этика, но заказчик может уйти.
                    </div>
                    <div class="quote">«Ну вы же понимаете, нам нужны цифры, которые можно показать инвесторам».</div>
                </div>
            </div>

        </div>

        <!-- ==================== 6. РЫНОК ==================== -->
        <h2 id="market">6. Анализ рынка и аудитория</h2>

        <h3>6.1. Обоснование актуальности</h3>
        <p>Настольные игры про социологию уже существуют в мире — значит, ниша живая:</p>
        <ul>
            <li><strong>«Это нелогично!»</strong> (Hobby World) — игроки угадывают реальные результаты исследований.</li>
            <li><strong>«Квотная выборка»</strong> (НИУ ВШЭ) — образовательная игра про сбор респондентов.</li>
            <li><strong>Sociosfera</strong> (Испания, 2026) — мини-сессии на 5–10 минут.</li>
            <li><strong>Plexus</strong> (США) — платформа для онлайн-микроигр по социологии.</li>
        </ul>

        <div class="highlight">
            <strong>Вывод:</strong> «Поле» может стать <strong>первой коммерческой настольной игрой от профессионального сообщества</strong> в России — с реальными байками, механикой двойного дна и интеграцией с книгой. <strong>А возможность добавлять любые другие книги и создавать лимитированные версии с эксклюзивными историями из первых уст открывает безграничный потенциал для коллабораций и новых изданий.</strong>
        </div>

        <h3>6.2. Целевые сегменты</h3>
        <table>
            <tr><th>Сегмент</th><th>Размер</th><th>Как привлечь</th></tr>
            <tr><td>Члены Ассоциации «7/89»</td><td>47 компаний</td><td>Презентация на съезде, амбассадоры</td></tr>
            <tr><td>Социологические факультеты</td><td>100+ вузов РФ</td><td>Апробация, методические материалы</td></tr>
            <tr><td>Любители настолок</td><td>Миллионы</td><td>Краудфандинг, маркетплейсы</td></tr>
            <tr><td>Корпоративный тимбилдинг</td><td>Тысячи компаний</td><td>B2B-лицензии</td></tr>
        </table>

        <!-- ==================== 7. ЦЕННОСТЬ ==================== -->
        <h2 id="value">7. Ценность для Ассоциации «7/89»</h2>

        <div class="grid-2">
            <div class="card">
                <h4>📣 Продвижение</h4>
                <p>Игра — «визитка» профессии для широкой аудитории. Социология перестаёт быть абстракцией.</p>
            </div>
            <div class="card">
                <h4>🎓 Образование</h4>
                <p>Инструмент для вузов и тимбилдинга. Первая российская настолка, рекомендованная для преподавания социологии.</p>
            </div>
            <div class="card">
                <h4>💰 Монетизация</h4>
                <p>Продажи игры + рост продаж книги «А вы точно социологи?» + B2B-лицензии. <strong>А также доход от коллабораций с другими книгами и лимитированных изданий.</strong></p>
            </div>
            <div class="card">
                <h4>🤝 Сообщество</h4>
                <p>Турниры, клубы, онлайн-сезоны. Игра объединяет профессионалов и новичков.</p>
            </div>
        </div>

        <h3>7.1. Интеграция с книгой</h3>
        <ul>
            <li><strong>12 карт респондентов</strong> — реальные байки из книги.</li>
            <li><strong>6 карт заказчиков</strong> — реальные кейсы.</li>
            <li><strong>Промо-вкладыш</strong> с QR-кодом на сайт 7/89 и «Литрес».</li>
            <li><strong>Режим «Кампания по книге»</strong> — серия партий с обсуждением.</li>
            <li><strong>Возможность добавлять любые другие книги</strong> — создание лимитированных версий с эксклюзивными событиями из первых уст, историями, которые вы нигде не услышите.</li>
        </ul>

        <!-- ==================== 8. ФИНАНСЫ ==================== -->
        <h2 id="finance">8. Финансовая модель</h2>

        <h3>8.1. Стартовый этап: пилот 10 экземпляров</h3>
        <table>
            <tr><th>Статья</th><th>Сумма (руб.)</th></tr>
            <tr><td>Печать 10 прототипов</td><td>30 000</td></tr>
            <tr><td>Художник (иллюстрации, дизайн)</td><td>50 000</td></tr>
            <tr><td>Разработка правил и баланс</td><td>0 (силами Ассоциации)</td></tr>
            <tr><td>Логистика и презентация</td><td>10 000</td></tr>
            <tr><td><strong>Итого пилот</strong></td><td><strong>90 000</strong></td></tr>
        </table>

        <h3>8.2. Масштабирование: тираж 1000 экземпляров</h3>
        <table>
            <tr><th>Статья</th><th>Сумма (руб.)</th></tr>
            <tr><td>Печать 1000 экз. (~800 руб./шт.)</td><td>800 000</td></tr>
            <tr><td>Маркетинг и краудфандинг</td><td>150 000</td></tr>
            <tr><td>Логистика</td><td>50 000</td></tr>
            <tr><td><strong>Итого тираж</strong></td><td><strong>1 000 000</strong></td></tr>
        </table>

        <h3>8.3. Прогноз выручки</h3>
        <table>
            <tr><th>Канал</th><th>Цена</th><th>Объём</th><th>Выручка</th></tr>
            <tr><td>Продажа игры</td><td>2 500 руб.</td><td>800 шт.</td><td>2 000 000 руб.</td></tr>
            <tr><td>B2B-лицензии</td><td>50 000 руб.</td><td>10 компаний</td><td>500 000 руб.</td></tr>
            <tr><td>Рост продаж книги</td><td>—</td><td>+20%</td><td>~100 000 руб.</td></tr>
            <tr><td><strong>Итого</strong></td><td></td><td></td><td><strong>~2 600 000 руб.</strong></td></tr>
        </table>

        <div class="highlight">
            <strong>Окупаемость:</strong> при тираже 1000 экз. и продаже 800 шт. проект окупается и приносит прибыль ~1,6 млн руб. Средства могут быть реинвестированы в онлайн-версию. <strong>Дополнительный потенциал: коллаборации с другими книгами и лимитированные издания.</strong>
        </div>

        <!-- ==================== 9. ДОРОЖНАЯ КАРТА ==================== -->
        <h2 id="roadmap">9. Дорожная карта</h2>

        <table>
            <tr><th>Период</th><th>Этап</th><th>Результат</th></tr>
            <tr><td>Октябрь–декабрь 2026</td><td>Разработка правил и прототипа</td><td>PDF-версия для печати</td></tr>
            <tr><td>Январь–март 2027</td><td>Печать 10 тестовых экземпляров</td><td>Коробки для тестирования</td></tr>
            <tr><td>Апрель–июнь 2027</td><td>Плейтесты с членами Ассоциации</td><td>Обратная связь, правки</td></tr>
            <tr><td>К следующему съезду</td><td>Презентовать игру</td><td>Публичный показ, сбор контактов</td></tr>
            <tr><td>Август–сентябрь 2027</td><td>Апробация в вузах</td><td>Методические материалы</td></tr>
            <tr><td>Октябрь 2027</td><td>Краудфандинг</td><td>Пилотный тираж 1000 экз.</td></tr>
            <tr><td>2028</td><td>Онлайн-версия</td><td>Бета-тест, релиз</td></tr>
        </table>

        <!-- ==================== 10. ОНЛАЙН ==================== -->
        <h2 id="online">10. Онлайн-версия</h2>

        <h3>10.1. Платформа и архитектура</h3>
        <ul>
            <li><strong>Web-first</strong> (браузер) + мобильное приложение.</li>
            <li><strong>Синхронный мультиплеер</strong> (2–6 игроков в реальном времени).</li>
            <li><strong>Асинхронный режим</strong> (пошаговые ходы).</li>
            <li><strong>Боты</strong> для одиночной игры и обучения.</li>
        </ul>

        <h3>10.2. Фичи</h3>
        <ul>
            <li>Туториал с интерактивным обучением (5 минут).</li>
            <li>Ежедневные челленджи («собери выборку за 5 ходов»).</li>
            <li>Рейтинги и сезоны.</li>
            <li>Редактор карт — игроки создают свои сценарии.</li>
            <li>Интеграция с сайтом 7/89 и «Литрес».</li>
            <li><strong>Возможность добавлять контент из любых книг — лимитированные события, эксклюзивные истории из первых уст.</strong></li>
        </ul>

        <h3>10.3. Монетизация</h3>
        <ul>
            <li><strong>Бесплатная база</strong> — все режимы доступны.</li>
            <li><strong>Косметика</strong> — скины карт, аватары.</li>
            <li><strong>Платные кампании</strong> — доп. сценарии от реальных кейсов, <strong>а также лимитированные истории из первых уст</strong>.</li>
            <li><strong>B2B-лицензии</strong> — для вузов и компаний.</li>
        </ul>

        <!-- ==================== 11. РИСКИ ==================== -->
        <h2 id="risks">11. Риски и их снижение</h2>

        <table>
            <tr><th>Риск</th><th>Вероятность</th><th>Снижение</th></tr>
            <tr><td>Сложные правила отпугнут новичков</td><td>Средняя</td><td>Экспресс-режим на 5 минут, 3 уровня входа</td></tr>
            <tr><td>Недостаток финансирования</td><td>Средняя</td><td>Пилот на 10 экз., краудфандинг, амбассадоры</td></tr>
            <tr><td>Низкий интерес аудитории</td><td>Низкая</td><td>Опора на сообщество 7/89, книга, вузы</td></tr>
            <tr><td>Технические сложности онлайн-версии</td><td>Средняя</td><td>Поэтапная разработка, бета-тест</td></tr>
        </table>

        <!-- ==================== 12. ИТОГИ ==================== -->
        <h2 id="summary">12. Итоги и призыв к действию</h2>

        <div class="highlight">
            <strong>«Поле»</strong> — это не просто настольная игра. Это инструмент продвижения социологии, объединения сообщества и создания нового канала монетизации для Ассоциации «7/89».
        </div>

        <h3>Что мы предлагаем:</h3>
        <ol>
            <li><strong>Пилот 10 экземпляров</strong> — для тестирования и презентаций.</li>
            <li><strong>Презентация к следующему съезду</strong> — публичный показ, сбор контактов.</li>
            <li><strong>Апробация в вузах</strong> — выход на социологические факультеты.</li>
            <li><strong>Краудфандинг</strong> — тираж 1000 экземпляров.</li>
            <li><strong>Онлайн-версия</strong> — Web + мобильное приложение.</li>
        </ol>

        <h3>Почему это выгодно:</h3>
        <ul>
            <li>✅ <strong>Продвижение профессии</strong> — игра делает социологию понятной и интересной.</li>
            <li>✅ <strong>Монетизация</strong> — продажи игры, книги, B2B-лицензии. <strong>Плюс доход от коллабораций с другими книгами и лимитированных изданий.</strong></li>
            <li>✅ <strong>Сообщество</strong> — турниры, клубы, онлайн-сезоны.</li>
            <li>✅ <strong>Инновации</strong> — первая коммерческая настолка от профессионального сообщества в России.</li>
            <li>✅ <strong>Образование</strong> — инструмент для вузов и тимбилдинга.</li>
            <li>✅ <strong>Безграничный потенциал</strong> — возможность добавлять любые книги и создавать лимитированные версии с эксклюзивными историями из первых уст.</li>
        </ul>

        <div class="highlight">
            <strong>Призыв к действию:</strong> поддержать пилотный тираж 10 экземпляров, назначить ответственных за разработку правил и дизайн, включить презентацию игры в программу следующего съезда.
        </div>

        <!-- ==================== ФУТЕР ==================== -->
        <div class="footer">
            <p><strong>Проект «Поле»</strong> — настольная игра о социологии</p>
            <p>Ассоциация исследовательских компаний «Группа 7/89»</p>
            <p>Сайт: <a href="https://www.789.ru/">www.789.ru</a></p>
            <p style="margin-top: 15px; font-size: 0.85em;">Документ подготовлен для внутренней презентации. Версия 1.3 — 2026 г.</p>
        </div>

    </div>
</body>
</html>
