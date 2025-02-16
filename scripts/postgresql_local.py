from dotenv import load_dotenv
from psycopg2 import pool
import os
import psycopg2
import socket
import subprocess
import csv


def fetchColumn(tb):
    cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tb}' AND table_schema = 'public';")

    columns = cursor.fetchall()
    return columns if columns else "No columns found."
    # [('store_id',), ('manager_staff_id',), ('address_id',), ('last_update',)]

def fetchData(tb):
    cursor.execute(f"SELECT * FROM public.{tb};")
    rows = cursor.fetchall()

    return rows if rows else "No rows found."
    # [(1, 1, 1, datetime.datetime(2006, 2, 15, 9, 57, 12)), (2, 2, 2, datetime.datetime(2006, 2, 15, 9, 57, 12))]

def writeCSV(tb):
    keys = [col[0] for col in fetchColumn(tb)]
    rows = fetchData(tb)
    data = []
    for row in rows:
        data.append({keys[i]: row[i] for i in range(len(keys))})

    with open(f"./data/postgresql/dvdrental_{tb}.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    return f"Data has been written to dvdrental_{tb}.csv."


try:
    connection_pool = pool.SimpleConnectionPool(
        1, 20,  # minconn, maxconn
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT"),
        application_name="PythonApp"
    )
    conn = connection_pool.getconn()
    print("Koneksi berhasil ke database")
except Exception as e:
    print(f"error:{e}")
    exit()
else:
    cursor = conn.cursor()

    print(writeCSV('film'))

    cursor.close()
    connection_pool.putconn(conn)