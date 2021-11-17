from datasources.models import *
from connector import conn, c


class Query:
    def __init__(self, query):
        self.query = query

    def execute(self):
        data = []
        c.execute(self.query)
        for row in c:
            print(row[0], '-', row[1], '-', row[2], '-', row[3],
                  '-', row[4], '-', row[5], '-', row[6], '-', row[7])
            try:
                data.append((
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                ))
                stmt = (
                    insert(logs_testing).values(
                        timestamp=row[0],
                        username=row[1],
                        os_username=row[2],
                        action_name=row[3],
                        owner=row[4],
                        obj_name=row[5],
                        current_user=row[6],
                        return_code=row[7])
                )
                conn_mysql.execute(stmt)
                print("Data added", '\n')
            except Exception as e:
                print(e)
        conn.close()
        return data
