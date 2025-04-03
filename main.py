import telebot
import config
from telebot import types  # для указание типов
import random
import math

bot = telebot.TeleBot(config.TG_API_CONFIG)
jokes = [
    "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
    "Программист звонит в службу поддержки: 'У меня проблема, я нажал Ctrl+S, а теперь не могу найти сохранённый файл.' Поддержка: 'А где вы его искали?' Программист: 'В холодильнике.'",
    "— Как назвать человека, который знает все языки программирования? — Миф.",
    "— Почему Python не может подружиться с SQL? — Потому что у них разные типы данных.",
    "— Почему сисадмин всегда ходит с флешкой? — На всякий случай, если придётся переустанавливать Windows.",
    "— Почему математики плохо играют в прятки? — Потому что они сразу идут по координатам.",
    "— Как отличить интроверта-программиста от экстраверта? — Интроверт смотрит в свои ботинки, экстраверт — в чужие.",
    "— Почему программисты не любят природу? — Там слишком много багов.",
    "— Что сказал 0 числу 8? — 'Ничего, просто посмотрел свысока.'",
    "— Почему веган не стал программистом? — Потому что боялся, что в коде будут животные.",
    "— Как программисты называют ошибку в душе? — Баг в шампуне.",
    "— Почему программисты не любят ходить в бар? — Потому что там слишком много NaN (Not a Number).",
    "— Что говорит программист, когда ему нужно время подумать? — 'Дайте мне пару секунд... или 2^10 миллисекунд.'",
    "— Почему программист всегда мёрзнет? — Потому что он постоянно работает с открытыми окнами.",
    "— Какой напиток любят программисты? — Java.",
    "— Почему программисты не любят играть в шахматы? — Потому что там нет кнопки 'Undo'.",
    "— Что сказал один байт другому? — '01001000 01101001!' ('Hi!' в бинарном коде).",
    "— Почему программисты не умеют готовить? — Потому что они всё время используют 'fork()' вместо ложки.",
    "— Почему программисты не любят природу? — Там нет Wi-Fi.",
    "— Какой главный принцип программирования? — 'Работает? Не трогай!'",
    "— Почему программисты не любят кофе без кофеина? — Потому что это NULL-напиток.",
    "— Что сказал один сервер другому? — 'У меня слишком большая нагрузка, давай балансировать!'",
    "— Почему программисты не любят спорт? — Потому что там слишком много действий в реальном времени.",
    "— Как программист называет своего кота? — 'Кот.exe'.",
    "— Почему программисты не любят ходить в кино? — Потому что там нельзя поставить фильм на паузу и погуглить спойлеры.",
    "— Почему программисты не любят писать документацию? — Потому что код должен говорить сам за себя (но никогда не говорит).",
    "— Как программисты называют свою вторую половинку? — 'Бэкап'.",
    "— Почему программисты не любят анекдоты про программистов? — Потому что они слишком предсказуемы.",
    "— Что сказал Git программисту? — 'Ветка — не птица, но летает.'",
    "— Почему программисты не любят ходить в походы? — Потому что там нет розеток.",
    "— Как программист называет свой холодильник? — 'Хранилище данных'.",
    "— Почему программисты не любят лифты? — Потому что боятся бесконечного цикла.",
    "— Что сказал Python JavaScript? — 'Ты слишком много говоришь!'",
    "— Почему программисты не любят загадки? — Потому что они предпочитают явные ответы.",
    "— Как программисты называют свою кровать? — 'Место для отладки сна'.",
    "— Почему программисты не любят фокусы? — Потому что они не любят, когда что-то работает, и никто не знает почему.",
    "— Что сказал один алгоритм другому? — 'Давай не будем усложнять — O(1) или смерть!'",
    "— Почему программисты не любят ходить в музеи? — Потому что там всё в режиме 'read-only'.",
    "— Как программист называет свою машину? — 'Транспортный протокол'.",
    "— Почему программисты не любят садоводство? — Потому что не знают, как дебажить растения.",
    "— Что сказал компилятор программисту? — 'Я тебя не понимаю, но попробую выполнить.'",
    "— Почему программисты не любят суши? — Потому что боятся raw-данных.",
    "— Как программист называет свою подушку? — 'Кэш для головы'.",
    "— Почему программисты не любят магию? — Потому что они не верят в недокументированные функции.",
    "— Что сказал один API другому? — 'Не грузи меня своими запросами!'",
    "— Почему программисты не любят зиму? — Потому что слишком много 'снежных' исключений.",
    "— Как программист называет свою собаку? — 'Лучший друг человека.exe'.",
    "— Почему программисты не любят завтракать? — Потому что у них нет утреннего 'стартапа'.",
    "— Что сказал один баг другому? — 'Давай спрячемся в коде, а то нас сейчас пофиксят!'",
    "— Почему программисты не любят арифметику? — Потому что 2 + 2 = 5 для очень больших значений 2.",
]

arr = {
    "start": "Подробная информация о том что делает команда /start",
    "help": "Подробная информация о том что делает команда /help",
    "golinks": "Подробная информация о том что делает команда /golinks",
    "getreplybuttons": "Подробная информация о том что делает команда /getreplybuttons",
    "getinfouser": "Подробная информация о том что делает команда /getinfouser",
    "about": "Подробная информация о том что делает команда /about",
    "joke": "Подробная информация о том что делает команда /joke",
    "getrarandom": "Подробная информация о том что делает команда /getrarandom",
    "math": "Подробная информация о том что делает команда /math",
}


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == "correct":
        # bot.edit_message_reply_markup(
        #     chat_id=chat_id, message_id=message_id, reply_markup=None
        # )
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=call.message.text.replace("\nВыберите правильные корни:", ""),
            reply_markup=None,
        )
        bot.answer_callback_query(call.id, "✅ Верно! Еще пример.", show_alert=False)
        quadratic_equation(call.message)
    if "wrong_" in call.data:
        bot.answer_callback_query(
            call.id, "❌ Неверно! Попробуйте еще раз.", show_alert=False
        )
    if call.data == "1":
        get_joke(call.message)
    if call.data in arr:
        bot.reply_to(call.message, arr[call.data])


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()

    for item in arr:
        markup.add(types.InlineKeyboardButton(item, callback_data=item))

    bot.send_message(
        message.chat.id,
        text="Привет, {0.first_name}! Вот команды которые мне доступны, нажми что бы получить описание".format(
            message.from_user
        ),
        reply_markup=markup,
    )


@bot.message_handler(commands=["golinks"])
def get_links(message):
    markup = types.InlineKeyboardMarkup()
    button0 = types.InlineKeyboardButton("Дать шутку", callback_data="1")
    button1 = types.InlineKeyboardButton(
        "Сайт Moodle", url="https://moodle.ntiustu.ru/mod/assign/view.php?id=4015"
    )
    button2 = types.InlineKeyboardButton(
        "Сайт Talk", url="https://ntiurfu44.ktalk.ru/xsn3j3id436s"
    )
    markup.add(button0, button1, button2)
    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}! Хочешь перейти по ссылке?".format(message.from_user),
        reply_markup=markup,
    )


@bot.message_handler(commands=["getreplybuttons"])
def get_reaply_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    btn2 = types.KeyboardButton("Ты работаешь?")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
            message.from_user
        ),
        reply_markup=markup,
    )


@bot.message_handler(commands=["getinfouser"])
def get_info(message: telebot.types.Message):
    bot.reply_to(message, message.from_user)


@bot.message_handler(commands=["about"])
def get_about(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    btnTG = types.InlineKeyboardButton("GitHub", url="https://github.com/DimaBatalin")
    btnVK = types.InlineKeyboardButton("VK", url="https://vk.com/dimabatalin")
    markup.add(btnTG, btnVK)
    bot.send_message(
        message.chat.id,
        "Я @D1M0N02, и я сделал этого бота с помощью telebot",
        reply_markup=markup,
    )


@bot.message_handler(commands=["joke"])
def get_joke(message: telebot.types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Еще шутка?", callback_data="1"))

    bot.send_message(
        message.chat.id,
        text=jokes[random.randint(0, len(jokes) - 1)].format(message.from_user),
        reply_markup=markup,
    )


@bot.message_handler(commands=["getrarandom"])
def send_random(message):
    bot.reply_to(message, random.randint(1, 3))


def simplify_equation(a, b, c):
    # Находим наибольший общий делитель коэффициентов
    common_divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    if common_divisor > 1:
        a //= common_divisor
        b //= common_divisor
        c //= common_divisor
    return a, b, c


@bot.message_handler(commands=["math"])
def quadratic_equation(message: telebot.types.Message):
    # Генерируем целые корни
    x1 = random.randint(-10, 10)
    x2 = random.randint(-10, 10)

    # Раскрываем скобки (x - x1)(x - x2) = 0 → ax² + bx + c = 0
    a = 1
    b = -(x1 + x2)
    c = x1 * x2

    # Упрощаем уравнение
    a, b, c = simplify_equation(a, b, c)

    # Форматируем уравнение
    equation_parts = []
    if a == 1:
        equation_parts.append("x²")
    elif a == -1:
        equation_parts.append("-x²")
    else:
        equation_parts.append(f"{a}x²")

    if b != 0:
        sign_b = "+" if b > 0 else "-"
        abs_b = abs(b)
        if abs_b == 1:
            equation_parts.append(f" {sign_b} x")
        else:
            equation_parts.append(f" {sign_b} {abs_b}x")

    if c != 0:
        sign_c = "+" if c > 0 else "-"
        equation_parts.append(f" {sign_c} {abs(c)}")

    equation = "".join(equation_parts) + " = 0"

    # Создаем варианты ответов
    correct_answer = sorted([x1, x2])
    options = [correct_answer]

    # Генерируем 3 неправильных варианта
    while len(options) < 4:
        wrong_x1 = random.randint(-10, 10)
        wrong_x2 = random.randint(-10, 10)
        wrong_answer = sorted([wrong_x1, wrong_x2])
        if wrong_answer not in options:
            options.append(wrong_answer)

    # Перемешиваем варианты
    random.shuffle(options)

    # Создаем клавиатуру
    markup = types.InlineKeyboardMarkup()
    for i, option in enumerate(options):
        text = (
            f"x₁={option[0]}, x₂={option[1]}"
            if option[0] != option[1]
            else f"x={option[0]}"
        )
        if option == correct_answer:
            callback_data = "correct"
        else:
            callback_data = f"wrong_{i}"
        markup.add(types.InlineKeyboardButton(text=text, callback_data=callback_data))

    # Отправляем сообщение
    escaped_equation = (
        equation.replace("*", "×")
        .replace("-", "\-")
        .replace("+", "\+")
        .replace("=", "\=")
    )

    msg = bot.send_message(
        message.chat.id,
        f"Решите уравнение:\n`{escaped_equation}`\n\nВыберите правильные корни:",
        parse_mode="MarkdownV2",
        reply_markup=markup,
    )

    # Сохраняем ID сообщения и правильный ответ для обработки callback
    bot.register_next_step_handler(
        msg, lambda m: None
    )  # Фиктивный хендлер, чтобы избежать ошибок
    bot._chat_data[msg.chat.id] = {
        "message_id": msg.message_id,
        "correct_answer": correct_answer,
    }


@bot.message_handler(func=lambda message: True)
def get_none(message):
    match message.text:
        case "Привет":
            bot.reply_to(message, "Привет мой новый друг!")
        case "Пока":
            bot.reply_to(message, "Пока(")
        case "Ты работаешь?":
            bot.reply_to(message, "Да, я работаю")
        case _:
            bot.reply_to(message, message.text)


bot.infinity_polling()
