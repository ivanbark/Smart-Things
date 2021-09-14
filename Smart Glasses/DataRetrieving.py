import os
import mysql.connector as mariadb
import json
import sense_hat
from datetime import datetime

def data_retrieve():
    # making database connection
    mariadb_connection = mariadb.connect(
        user='data_gatherer',
        password='Ijsbeer2',
        database='SmartGlasses_Data'
    )

    # creating cursur to execute queries
    cur = mariadb_connection.cursor()

    # get image data
    stmt = 'SELECT * FROM image_data ORDER BY id ASC;'
    cur.execute(stmt)
    result = cur.fetchall()

    # commit and close
    mariadb_connection.commit()
    cur.close()
    mariadb_connection.close()


    output_json = []
    for row in result:
        output_json.append(dict(zip(row)))

    print("Content-type: application/json\n")
    print(json.dumps(output_json))
    # done

data_retrieve()