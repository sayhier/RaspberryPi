import sqlite3

conn = sqlite3.connect('DATA_SOURCE.db')
cursor = conn.cursor()


# ---------------------------------------------------------------------------#
# Table for data store
# ---------------------------------------------------------------------------#
cursor.execute('''CREATE TABLE IF NOT EXISTS  DATA_STORE(TIME TEXT PRIMARY KEY);''')

i = 0
while i <= 100:
    i = i+1
    name = "data_" + str(i)
    value = "value_" + str(i)
    unit = "unit_" + str(i)
    cursor.execute("alter table DATA_STORE add column '%s' 'text'" % name)
    cursor.execute("alter table DATA_STORE add column '%s' 'float'" % value)
    cursor.execute("alter table DATA_STORE add column '%s' 'text'" % unit)

# ---------------------------------------------------------------------------#
# Modbus client init
# ---------------------------------------------------------------------------#
cursor.execute('''CREATE TABLE IF NOT EXISTS  DATA_SEND(TIME TEXT PRIMARY KEY);''')

i = 0
while i <= 100:
    i = i+1
    name = "data_" + str(i)
    value = "value_" + str(i)
    unit = "unit_" + str(i)
    cursor.execute("alter table DATA_SEND add column '%s' 'text'" % name)
    cursor.execute("alter table DATA_SEND add column '%s' 'float'" % value)
    cursor.execute("alter table DATA_SEND add column '%s' 'text'" % unit)


# ---------------------------------------------------------------------------#
cursor.close()
conn.commit()
conn.close()
# ---------------------------------------------------------------------------#
