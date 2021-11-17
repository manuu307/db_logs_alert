from data_processing import Compare
from query import Query
from send_mail import SendMail
from config import *

query = ""
incoming_data = Query(query).get_data()
message = Compare(incoming_data)
if message.data:
    SendMail(message.data, message.incoming_data)
else:
    print("No data to send")
