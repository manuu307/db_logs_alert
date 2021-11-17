# not used!
import pymysql.cursors

# Connect to the database
db = pymysql.connect(host='localhost',
                             user='test',
                             password='newpassword',
                             database='rafap',
                             cursorclass=pymysql.cursors.DictCursor)

# Create cursor object
cursor = db.cursor()
# Get cursor version
version = cursor.execute("SELECT VERSION()")
print("Cursor version: ",version)

# Query
with db:
    with cursor as cursor:
    # Create tables
        try:
            table_testing = "CREATE TABLE IF NOT EXISTS testing (id INT AUTO_INCREMENT PRIMARY KEY, hash VARCHAR(255), date DATETIME)"
            table_prod = "CREATE TABLE IF NOT EXISTS production (id INT AUTO_INCREMENT PRIMARY KEY, hash VARCHAR(255), date DATETIME)"
            cursor.execute(table_testing)
            cursor.execute(table_prod)
            print("Tables created successfully!")
        except Exception as e:
            print(e)
        

# Commit changes
    db.commit()



  