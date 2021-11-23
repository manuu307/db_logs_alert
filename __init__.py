from data_processing import Compare
from query import Query
from send_mail import SendMail
from config import *

query = """

SELECT
    TO_CHAR(TIMESTAMP,'MM/DD HH24:MI:SS') TIMESTAMP,
    SUBSTR(USERNAME,1,20) USERNAME,
    OS_USERNAME,
    ACTION_NAME,
    OWNER,
    OBJ_NAME,
    SUBSTR(CURRENT_USER,1,20) CURRENT_USER,
    RETURNCODE
FROM
    DBA_AUDIT_TRAIL
WHERE
    USERNAME IN ('JURTIAGA','MTUDISCO') And timestamp > sysdate - 20/1440
    order by TIMESTAMP asc

    """
incoming_data = Query(query).execute()
message = Compare(incoming_data).message()
if len(message) > 0:
    SendMail(message)
else:
    print("No data to send")
