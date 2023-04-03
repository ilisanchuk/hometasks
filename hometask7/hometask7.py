import telebot
from telebot import types

bot = telebot.TeleBot("5964151132:AAGrs0PYF_esWHDTSsq65YtemDL5U4qmFiw")

def correct_input(message):
    if message.isdigit():
        return "int"
    elif '.' in message:
        count = 0
        for _ in message:
            if _ == '.':
                count += 1
        if count == 1:
            return 'float'
    else:
        return 'error'



@bot.message_handler(commands=['start'])

def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать вычисление")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, я бот-калькулятор, умею выполнять простые операции над 2-мя числами. Для начала введите первое число, затем выберите знак действия и потом введите второе число. Обращаю внимание на то, чтобы выполнить операции над дробными числами, записывать дробную часть нужно через точку. Приятного вычисления!", reply_markup=markup)



@bot.message_handler(func= lambda x: x.text == 'Начать вычисление' or x.text == 'Да')

def first_num(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, "Введите первое число.", reply_markup=markup)
    bot.register_next_step_handler(message, operation)


def operation(message):
    global first_number
    if correct_input(message.text) == 'int' or correct_input(message.text) == 'float':
        if correct_input(message.text) == 'int':
            first_number = int(message.text)
        elif correct_input(message.text) == 'float':
            first_number = float(message.text)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        addition = types.KeyboardButton('+')
        subtraction = types.KeyboardButton('-')
        multiplication = types.KeyboardButton('*')
        division = types.KeyboardButton('/')
        markup.add(addition, subtraction, multiplication, division)
        bot.send_message(message.chat.id, "Выберите знак действия.", reply_markup=markup)
        bot.register_next_step_handler(message, second_num)
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Неправильный формат данных. \nПопробовать ещё раз?', reply_markup=markup)


def second_num(message):
    global symbol
    symbol = message.text
    if symbol != '+' and symbol != '-' and symbol != '*' and symbol != '/':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Не туда нажали.\nПопробовать ещё раз?', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, "Введите второе число.", reply_markup=markup)
        bot.register_next_step_handler(message, calculation)

def calculation(message):
    global result
    global second_number
    if (correct_input(message.text) == 'int' or correct_input(message.text) == 'float'):
        if correct_input(message.text) == 'int':
            second_number = int(message.text)
        elif correct_input(message.text) == 'float':
            second_number = float(message.text)

        if symbol == '+' or symbol == '-' or symbol == '*' or (symbol == '/' and second_number != 0):
            if symbol == '+':
                result = first_number + second_number
            elif symbol == '-':
                result = first_number - second_number
            elif symbol == '*':
                result = first_number * second_number
            elif symbol == '/' and second_number != 0:
                result = first_number / second_number

            if (result % int(result) != 0):
                result = round(result, 4)
            else:
                result = int(result)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn1 = types.KeyboardButton('Да')
            btn2 = types.KeyboardButton('Нет')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f" Итого: {first_number} {symbol} {second_number} = {result}\n Попробовать ещё раз?", reply_markup=markup)

        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn1 = types.KeyboardButton('Да')
            btn2 = types.KeyboardButton('Нет')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'На ноль делать нельзя. \nПопробовать ещё раз?', reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Неправильный формат данных. \nПопробовать ещё раз?', reply_markup=markup)


@bot.message_handler(func= lambda x: x.text == 'Нет')

def quit(message):
    bot.send_message(message.chat.id, 'Всего хорошего.')
    bot.stop_polling()


bot.polling(none_stop=True, interval=0)