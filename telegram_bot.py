import telebot


class MyBot:

    def __init__(self):
        self.bot = None

    def run_bot(self):
        self.bot = telebot.TeleBot("5085358297:AAF6WKAwqK4Pk605bP0ghgl7XAknu9C5Vqo")
        try:
            self.bot.send_message(751113479, "Let's pinging ALL2")
        except Exception as ex:
            print(f"cannot receive message to chat {751113479}", ex)

        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            self.bot.send_message(message.chat.id, 'Это БОТ для мониторинга сетевой доступности контроллеров '
                                                   'АСУ ТП '
                                                   'СКК "МРИЯ"')

        @self.bot.message_handler(commands=['help'])
        def start_message(message):
            self.bot.send_message(message.chat.id, f'/start - активация бота\n103 - получение статусов связи 103 vlan\n'
                                                   f'105-получение статусов связи 105 vlan\n83-получение статусов '
                                                   f'связи 83 vlan\n80 - получение статусов связи 80vlan\n'
                                                   f'fail 103 - получение ip со статусом FAIL 103 vlan\n'
                                                   f'fail 105-получение ip со статусом FAIL 105 vlan\nfail 83-получение'
                                                   f'ip со статусом FAIL 83 vlan\nfail 80 - получение ip со статусом'
                                                   f' FAIL 80 vlan')

        @self.bot.message_handler(content_types=['text'])
        def get_messages(message):
            if message.text.lower() == "105":
                file1 = open("data/net_105_ping_state.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            elif message.text.lower() == "103":
                file1 = open("data/net_103_ping_state.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            elif message.text.lower() == "83":
                file1 = open("data/net_83_ping_state.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            elif message.text.lower() == "80":
                file1 = open("data/net_80_ping_state.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            elif message.text.lower() == "fail 80":
                file1 = open("data/net_80_ping_fail.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            elif message.text.lower() == "fail 83":
                file1 = open("data/net_83_ping_fail.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            elif message.text.lower() == "fail 103":
                file1 = open("data/net_103_ping_fail.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            elif message.text.lower() == "fail 105":
                file1 = open("data/net_105_ping_fail.txt", "r")
                while True:
                    # считываем строку
                    line = file1.readline()
                    # прерываем цикл, если строка пустая
                    if not line:
                        break
                    # выводим строку
                    payload_msg = line.strip()
                    self.bot.send_message(message.chat.id, payload_msg)
                    self.valid_request = True
                # закрываем файл
                file1.close()
            else:
                self.valid_request = False
            if not self.valid_request:
                self.bot.send_message(message.chat.id, "WRONG REQUEST")

        self.bot.polling()


activate_bot = MyBot()
activate_bot.run_bot()
