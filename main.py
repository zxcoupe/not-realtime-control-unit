# -*- coding: utf-8 -*-

import math

import matplotlib as mpl
import matplotlib.pyplot as plt
import psycopg2

# Tunnel Config

SSH_INTERNAL_PORT = 5432
# Postgres Config
DB_HOST = "127.0.0.1"
DB_PORT = SSH_INTERNAL_PORT
DB_PASSWORD = "postgres"
DB_DATABASE = "postgres"
DB_USER = "postgres"

conn = psycopg2.connect(host = DB_HOST, password = DB_PASSWORD,
                    database = DB_DATABASE, user = DB_USER, port = DB_PORT)




cursor = conn.cursor()

print ( conn.get_dsn_parameters(),"\n")

cursor.execute("SELECT version();")
record = cursor.fetchone()

print("You are connected to - ", record,"\n")

cursor.execute('SELECT * from pg_shadow')
record = cursor.fetchone()
print("Мой запрос 1 - ", record,"\n")

cursor.execute('SELECT * FROM pg_user LIMIT 1')
record = cursor.fetchall()
print("Мой запрос 2 - ", record,"\n")

#SELECT temp_files AS "Temporary files"
#     , temp_bytes AS "Size of temporary files"
#FROM   pg_stat_database db;

#query = input("Следующий запрос предлагается ввести вручную: ")
#print("Введен запрос: ",query)
#cursor.execute(query)
#record = cursor.fetchall()
#print("Результат ручного ввода - ", record,"\n")

print('Дрон ожидает координаты отправки: \n\
   -9+9 по оси X\n\
   -9+9 по оси Y\n')
x = int(input())
y = x // 60
z = x % 60

print(y, "ч", z, "м")

if x > 1 and y > 5:
   print("Получена директива координат белого дома")
elif x > 0 and y < 0:
   print("Получена директива координат пивного ларька")
elif y > 0:
   print("Получена директива спец.координат по закрытому коду")
else:
   print("Получена директива самоликвидации")

cursor.close()
conn.close()

print("PostgreSQL connection is closed")

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 10, -1.5, 1.5])

plt.title('Sine & Cosine')
plt.xlabel('x')
plt.ylabel('F(x)')

xs = []
sin_vals = []
cos_vals = []

x = 0.0
while x < 10.0:
       sin_vals += [ math.sin(x) ]
       cos_vals += [ math.cos(x) ]
       xs += [x]
       x += 0.1

plt.plot(xs, sin_vals, color = 'blue', linestyle = 'solid',
        label = 'sin(x)')
plt.plot(xs, cos_vals, color = 'red', linestyle = 'dashed',
        label = 'cos(x)')
plt.legend(loc = 'upper right')
fig.savefig('trigan.png')
plt.show()
