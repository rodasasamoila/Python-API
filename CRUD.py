import requests
import json
import pymysql
import psycopg2
import todo
todo.insert(5)
resp=todo.get_table()
print(resp)


