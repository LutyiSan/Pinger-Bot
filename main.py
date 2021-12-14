import subprocess
import sys
import time


def run():
    bot_start = subprocess.Popen([sys.executable, 'telegram_bot.py'])
    time.sleep(5)  # Даем время серверу на запуск
    ping_start = subprocess.Popen([sys.executable, 'pinging_v2.py'])
    time.sleep(5)
    bot_start.wait()
    ping_start.wait()


if __name__ == '__main__':
    run()
