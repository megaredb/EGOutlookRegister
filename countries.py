from random import choice

var = ['Австралия', 'Австрия', 'Азербайджан', 'Аландские острова', 'Албания', 'Алжир', 'Американское Самоа', 'Ангилья',
       'Ангола', 'Андорра', 'Антарктида', 'Антигуа и Барбуда', 'Аргентина', 'Армения', 'Аруба', 'Афганистан',
       'Багамские о-ва', 'Бангладеш', 'Барбадос', 'Бахрейн', 'Беларусь', 'Белиз', 'Бельгия', 'Бенин', 'Бермуды',
       'Болгария', 'Боливия', 'Бонэйр', 'Босния и Герцеговина', 'Ботсвана', 'Бразилия',
       'Британская территория в Индийском океане', 'Бруней-Даруссалам', 'Буркина-Фасо', 'Бурунди', 'Бутан', 'Вануату',
       'Ватикан', 'Венгрия', 'Венесуэла', 'Виргинские о-ва (Великобритания)', 'Виргинские о-ва США', 'Вьетнам', 'Габон',
       'Гаити', 'Гайана', 'Гамбия', 'Гана', 'Гваделупа', 'Гватемала', 'Гвинея', 'Гвинея-Бисау', 'Германия', 'Гернси',
       'Гибралтар', 'Гондурас', 'Гонконг, CАР', 'Гренада', 'Гренландия', 'Греция', 'Грузия', 'Гуам', 'Дания', 'Джерси',
       'Джибути', 'Доминика', 'Доминиканская Республика', 'Египет', 'Замбия', 'Зимбабве', 'Израиль', 'Индия',
       'Индонезия', 'Иордания', 'Ирак', 'Иран', 'Ирландия', 'Исландия', 'Испания', 'Италия', 'Йемен', 'Кабо-Верде',
       'Казахстан', 'Камбоджа', 'Камерун', 'Канада', 'Катар', 'Кения', 'Кипр', 'Киргизия', 'Кирибати', 'Китай',
       'Кокосовые (Килинг) острова', 'Колумбия', 'Коморы', 'Конго', 'Конго (ДРК)', 'Корея, Республика', 'Косово',
       'Коста-Рика', "Кот-д'Ивуар", 'Куба', 'Кувейт', 'Кюрасао', 'Лаосская Народно-Демократическая Республика',
       'Латвия', 'Лесото', 'Либерия', 'Ливан', 'Ливия', 'Литва', 'Лихтенштейн', 'Люксембург', 'Маврикий', 'Мавритания',
       'Мадагаскар', 'Майотта', 'Макао, САР', 'Малави', 'Малайзия', 'Мали',
       'Малые Тихоокеанские Отдаленные Острова США', 'Мальдивы', 'Мальта', 'Марокко', 'Мартиника', 'Маршалловы Острова',
       'Мексика', 'Микронезия, Федеративные Штаты', 'Мозамбик', 'Молдова', 'Монако', 'Монголия', 'Монтсеррат', 'Мьянма',
       'Намибия', 'Науру', 'Непал', 'Нигер', 'Нигерия', 'Нидерландские Антильские о-ва (бывшие)', 'Нидерланды',
       'Никарагуа', 'Ниуэ', 'Новая Зеландия', 'Новая Каледония', 'Норвегия', 'ОАЭ', 'О-ва Питкэрн',
       'О-ва Св. Елены, Вознесения и Тристан-да-Кунья', 'Оман', 'Остров Буве', 'Остров Вознесения', 'Остров Мэн',
       'Остров Норфолк', 'Остров Рождества', 'Остров Херд и острова Макдональд', 'Острова Кайман', 'Острова Кука',
       'Острова Теркс и Кайкос', 'Пакистан', 'Палау', 'Палестинская Автономия', 'Панама', 'Папуа-Новая Гвинея',
       'Парагвай', 'Перу', 'Польша', 'Португалия', 'Пуэрто-Рико', 'Реюньон', 'Россия', 'Руанда', 'Румыния', 'Саба',
       'Сальвадор', 'Самоа', 'Сан-Марино', 'Сан-Томе и Принсипи', 'Саудовская Аравия', 'Свазиленд',
       'Северная Македония', 'Северные Марианские острова', 'Сейшелы', 'Сен-Бартелеми', 'Сенегал', 'Сен-Мартен',
       'Сен-Пьер и Микелон', 'Сент-Винсент и Гренадины', 'Сент-Китс и Невис', 'Сент-Люсия', 'Сербия', 'Сингапур',
       'Синт-Мартен', 'Синт-Эстатиус', 'Сирия', 'Словакия', 'Словения', 'Соединенное Королевство', 'Соединенные Штаты',
       'Соломоновы Острова', 'Сомали', 'Судан', 'Суринам', 'Сьерра-Леоне', 'Таджикистан', 'Таиланд', 'Тайвань',
       'Танзания, Объединенная Республика', 'Тимор-Лесте', 'Того', 'Токелау', 'Тонга', 'Тринидад и Тобаго',
       'Тристан-да-Кунья', 'Тувалу', 'Тунис', 'Туркменистан', 'Турция', 'Уганда', 'Узбекистан', 'Украина',
       'Уоллис и Футуна', 'Уругвай', 'Фарерские Острова', 'Фиджи', 'Филиппины', 'Финляндия', 'Фолклендские острова',
       'Франция', 'Французская Гвиана', 'Французская Полинезия', 'Французские Южные Территории', 'Хорватия',
       'Центрально-Африканская Республика', 'Чад', 'Черногория', 'Чехия', 'Чили', 'Швейцария', 'Швеция', 'Шпицберген',
       'Шри-Ланка', 'Эквадор', 'Экваториальная Гвинея', 'Эритрея', 'Эстония', 'Эфиопия', 'Южная Африка',
       'Южная Георгия и Южные Сандвичевы о-ва', 'Южный Судан', 'Ямайка', 'Ян-Майен', 'Япония']


def get_country_outlook():
    return choice(var)
