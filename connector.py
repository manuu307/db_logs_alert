import cx_Oracle
from config import *
import os

os.environ['PATH'] = environ_path_

# if needed, place an 'r' before any parameter in order to address special characters such as '\'.
dsn_tns = cx_Oracle.makedsn(host_, port_, service_name=service_name_)
print(dsn_tns)

# if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
conn = cx_Oracle.connect(user=user_, password=password_, dsn=dsn_tns)
print(conn.version)
c = conn.cursor()
