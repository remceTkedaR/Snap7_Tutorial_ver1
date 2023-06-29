#  Test program for communication of Snap7 python with S7 1200
# Reading data from one variable in a data block
# by Radosław Tecmer
# radek69tecmer@gmail.com
# ------------------------

import snap7
import struct
import csv

# Function read data from instance db
PLC_IP = '192.168.1.121'


def data_block_read(db_number, inst_number, data):
    db_val = client.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!f", db_val[:4])
    print(value_struct)
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = float('.'.join(str(ele) for ele in value_unpack))  # concatenating elements into a string
    my_str_value = '%-.4f' % result  # formatting the number to four decimal places
    return my_str_value


try:
    client = snap7.client.Client()
    client.connect(PLC_IP, 0, 1)
    print('connected to PLC')
except snap7.error.s7_server_errors as e:
    print('Błąd podczas nawiązywania połączenia:', str(e))

# Read temperature Outside (db 3, instance 24, data =" real" )
outside = data_block_read(3, 24, 4)

print(outside)