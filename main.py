from class_ping import PingAlert
from class_watchdog import Watchdog
from time import sleep
from config import *

def dot_sleep(sec: int):
    from sys import stdout
    for i in range(sec):
        sleep(1)
        stdout.write(".")
        stdout.flush()
    print()


if __name__ == '__main__':
    print(f"****** Ok, i'm started. Let's ping {IP_FOR_PING} ******")
    print()
    ping_alert = PingAlert(ip=IP_FOR_PING, alert_timer=PING_ALERT_TIMER)
    watchdog = Watchdog(path=WATCHDOG_PATH, filename=WATCHDOG_FILENAME)
    while True:
        ping_alert.ping(verbose=VERBOSE)
        if ping_alert.alert():
            print(f'Подключения нет уже {PING_ALERT_TIMER} сек.. Убиваю {WATCHDOG_FILENAME}.')
            watchdog.kill()
            print(f'Убил. Жду {SLEEP_AFTER_KILLING_WATCHDOG} сек.')
            dot_sleep(SLEEP_AFTER_KILLING_WATCHDOG)
            print(f'Запускаю {WATCHDOG_FILENAME}')
            watchdog.start()
            print(f"Жду {SLEEP_AFTER_STARTING_WATCHDOG} сек. прежде, чем начать пинговать опять.")
            dot_sleep(SLEEP_AFTER_STARTING_WATCHDOG)
            ping_alert.reset()
            print('Начинаю пинговать опять.')
        sleep(1)