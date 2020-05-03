# import setup_module
# setup_module.Depending.append('pythonping')
# setup_module.Depending.init()

import pythonping


if __name__ == '__main__':
    response_list = pythonping.ping("192.168.18.22", verbose=True)
    if response_list.success():
        print('yea')
    else:
        print('nope')