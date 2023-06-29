# Library Snap7
# Connection with the PLC controller S7 1200
# by  Radosław Tecmer
# e-mail radek69tecmer@gmail.com
# --------------------------------------------------


import snap7
import time


# client = snap7.client.Client()
# client.connect('192.168.1.121', 0, 1)
PLC_IP = '192.168.1.121'


try:
    client = snap7.client.Client()
    client.connect(PLC_IP, 0, 1)
    print('connected to PLC')
except snap7.error.s7_server_errors as e:
    print('Błąd podczas nawiązywania połączenia:', str(e))
    time.sleep(0.2)
    client = snap7.client.Client()
    client.connect(PLC_IP, 0, 1)
    print('next connected to PLC')
else:
    print('closing the connection')

