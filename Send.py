import sqlite3
import socket
import time

# ---------------------------------------------------------------------------#
# Table for data store
# ---------------------------------------------------------------------------#

while 1:
    conn = sqlite3.connect('DATA_SOURCE.db')
    cursor = conn.cursor()
    cursor.execute("Select * From DATA_SEND Limit 1")
    record = cursor.fetchone()
    if record is None:
        print('no record in database')
        cursor.close()
        conn.commit()
        conn.close()
    else:
        record1 = record[0:6]
        # 需不需要握手，以及如何判断发送成功

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立连接:
        try:
            #s.connect(('sayhier.gicp.net', 39654))
            s.connect(('127.0.0.1', 9999))
            result = s.sendall(bytes(str(record1), 'utf-8'))
            if result is None:
                print("send OK")
                cursor.execute("delete from DATA_SEND where TIME = ?;", (record1[0],))
        except:
            print("connection error")

        cursor.close()
        conn.commit()
        conn.close()
    time.sleep(2)
