from datasources.models import *
from send_mail import *
from query import *
from config import *


class Compare:
    def __init__(self, incoming_data):
        self.data = []
        self.incoming_data = incoming_data
        self.stored_data = []
        # query the last 20 rows from the table logs_testing
        get_from_testing = select(logs_testing).where(
            logs_testing.c.id > 0).order_by(logs_testing.c.id.desc()).limit(20)
        for row in conn_mysql.execute(get_from_testing).fetchall():
            # append row to prev_data except for id
            self.stored_data.append(row[1:9])

        # compare the data with the previous data
        if self.incoming_data:
            for row in self.incoming_data:
                if row not in self.stored_data:
                    self.data.append(row)
        if self.data:
            # add To: and Subject: to the message

            message = 'From: Arcanus Notificaciones <rafap@arcanus.com.uy> \n' 'Subject: Movimientos de logs (TESTING) \n' 'To: ' + \
                receiver_email_+'\n'
            message += "Los siguientes movimientos fueron registrados en el log de TESTING: \n"
            for row in self.data:
                message += "\n" + "TIMESTAMP : " + str(row[0]) + " | " + "USERNAME : " + str(row[1]) + " | " + "OS_USERNAME: " + str(row[2]) + " | " + "ACTION: " + str(
                    row[3]) + " | " + "OWNER : " + str(row[4]) + " | " + "OBJ: " + str(row[5]) + " | " + "CURRENT_USER: " + str(row[6]) + " | " + "RETURNCODE: " + str(row[7]) + "\n"
        return message
