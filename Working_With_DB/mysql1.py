
# https://stackoverflow.com/questions/65565172/python-mysql-connector-hangs-indefinitely-when-connecting-to-remote-mysql-via-ss
# https://resotto.medium.com/modulenotfounderror-no-module-named-mysql-connector-mysql-is-not-a-package-bfc7256a91b5

import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        port = 3306,
        use_pure=True,
        user="root",
        password="1234"
        # database="your_database"
    )
    if conn.is_connected():
        print("Connected to MySQL successfully!")
    else:
        print("Connection failed!")
except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed.")





