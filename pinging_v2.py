import time
import sys
import telebot
import datetime
from pythonping import ping


def write_data(filename, ip, state):
    file_curr = open(filename, 'a')
    write_text = f'{ip} {state} {datetime.datetime.now()}\n'
    file_curr.write(write_text)
    file_curr.close()


def start_write(filename):
    file = open(filename, 'w', encoding="utf-8")
    file.close()


def pinging(file_all, file_state, file_fail):
    file_al = open(file_all, "r", encoding="utf-8")
    lines = file_al.readlines()
    for i in lines:
        data_array = i.split("@")
        ping_result = ping(data_array[0], out=sys.stdout, timeout=1, size=40, count=3, verbose=True)
        if not ping_result.success():
            warning_info = f'FAIL\n{data_array[0]}\n{data_array[1]}\nscadaID: {data_array[2]}\n{str(datetime.datetime.now())}'
            bot.send_message(751113479, warning_info)
            write_data(file_state, 'FAIL', f'{data_array[0]} {data_array[1]} {data_array[2]}'
                                           f' {str(datetime.datetime.now())}')
            write_data(file_fail, 'FAIL', f'{data_array[0]} {data_array[1]} {data_array[2]}'
                                          f' {str(datetime.datetime.now())}')
        else:
            write_data(file_state, 'OK', f'{data_array[0]} {data_array[1]} {data_array[2]}'
                                         f' {str(datetime.datetime.now())}')


while True:
    start_write("data/net_80_ping_state.txt")
    start_write("data/net_80_ping_fail.txt")
    start_write("data/net_83_ping_state.txt")
    start_write("data/net_83_ping_fail.txt")
    start_write("data/net_103_ping_state.txt")
    start_write("data/net_103_ping_fail.txt")
    start_write("data/net_105_ping_state.txt")
    start_write("data/net_105_ping_fail.txt")
    try:
        bot = telebot.TeleBot("5085358297:AAF6WKAwqK4Pk605bP0ghgl7XAknu9C5Vqo")
        bot.send_message(751113479, "Let's Pinging ALL")
    except Exception as e:
        print(e)
    pinging("data/all_80.txt", "data/net_80_ping_state.txt", "data/net_80_ping_fail.txt")
    pinging("data/all_83.txt", "data/net_83_ping_state.txt", "data/net_83_ping_fail.txt")
    pinging("data/all_103.txt", "data/net_103_ping_state.txt", "data/net_103_ping_fail.txt")
    pinging("data/all_105.txt", "data/net_105_ping_state.txt", "data/net_105_ping_fail.txt")

    bot.send_message(751113479, 'Pinging Done')
    time.sleep(3600)
