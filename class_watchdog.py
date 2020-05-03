class Watchdog:
    def __init__(self, path: str, filename: str):
        if isinstance(path, str):
            if path[len(path)-1] == '/':
                self.__path = path
            else:
                raise Exception('последний символ path должен быть </>')
        else:
            raise Exception('path не является строкой')

        if isinstance(filename, str):
            self.__filename = filename
        else:
            raise Exception("filename должен быть строкой")

    def kill(self):
        import psutil
        for proc in psutil.process_iter():
            if proc.name() == self.__filename:
                try:
                    proc.kill()
                    return True
                except:
                    return False

    def start(self):
        import subprocess
        __p = subprocess.Popen(self.__path + self.__filename)