from pyModbusTCP.client import ModbusClient
from datetime import datetime
from struct import *
import sqlite3
import time

# ---------------------------------------------------------------------------#
# Settings
# ---------------------------------------------------------------------------#
read_interval = 5
# ---------------------------------------------------------------------------#
# pH        float       0
# Cond      float       2       us/cm
# temp      float       4       C
# ---------------------------------------------------------------------------#
data_to_read = [
    ["pH", "float", 0, "", 0.0],
    ["cond", "float", 2, "us/cm", 0.0],
]


def unpack_float(low_bytes, high_bytes):
    my_pack = pack('>HH', low_bytes, high_bytes)
    f = unpack('>f', my_pack)
    return f[0]


# ---------------------------------------------------------------------------#
# Modbus client init
# ---------------------------------------------------------------------------#
c = ModbusClient()
if not c.host("localhost"):
    print("host error")
if not c.port(502):
    print("port error")


while True:
    if c.is_open():
        for data in data_to_read:
            regs = c.read_holding_registers(data[2], 2)
            if regs:
                f = unpack_float(regs[0], regs[1])
                data[4] = f
                print(data[0] + ": ", round(f, 2))
            else:
                print("read error")
        # write to database
        conn = sqlite3.connect('DATA_SOURCE.db')
        cursor = conn.cursor()
        now = datetime.now()
        record_time = now.strftime('%y-%m-%d %H-%M-%S')

        data_to_db = [record_time, data_to_read[0][0], data_to_read[0][4], data_to_read[0][3], data_to_read[1][0],
                      data_to_read[1][4], data_to_read[1][3]]
        cursor.execute(
            "insert into DATA_STORE (TIME, data_1, value_1, unit_1, data_2, value_2, unit_2) VALUES(?,?,?,?,?,?,?)",
            data_to_db)
        cursor.execute(
            "insert into DATA_SEND (TIME, data_1, value_1, unit_1, data_2, value_2, unit_2) VALUES(?,?,?,?,?,?,?)",
            data_to_db)
        cursor.close()
        conn.commit()
        conn.close()
    else:
        c.open()

    time.sleep(read_interval)
