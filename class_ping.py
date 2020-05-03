import pythonping
from datetime import datetime

class PingAlert:
    def __init__(self, ip: str, alert_timer: int):
        self.__ip = ip
        self.__setted_alert_timer = alert_timer
        self.__last_alert = datetime.now()
        self.__alert = False
        self.__message_printed = False

    def __set_alert(self):
        if (datetime.now() - self.__last_alert).total_seconds() > self.__setted_alert_timer:
            self.__alert = True
        else:
            self.__alert = False

    def reset(self):
        self.__last_alert = datetime.now()
        self.__alert = False
        self.__message_printed = False

    def ping(self, verbose=False):
        def print_message(self, is_ping: bool):
            if not self.__message_printed:
                self.__message_printed = True
                if is_ping:
                    print('Пинги есть!')
                else:
                    print('похоже пингов нет...')

        try:
            _result = pythonping.ping(self.__ip, verbose=verbose, count=1).success()
        except:
            if verbose:
                print('Network error!')
            _result = False
        if _result:
            self.__last_alert = datetime.now()

        print_message(self, _result)
        self.__set_alert()
        return _result

    def alert(self):
        self.__set_alert()
        return self.__alert
