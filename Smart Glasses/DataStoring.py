import os
import mysql.connector as mariadb
import sense_hat
from datetime import datetime


# sense hat object
sh = sense_hat.SenseHat()


def data_store():
    # making database connection
    mariadb_connection = mariadb.connect(
        user='data_gatherer',
        password='Ijsbeer2',
        database='SmartGlasses_Data'
    )

    # creating cursur to execute queries
    cur = mariadb_connection.cursor()

    # creating table
    stmt = 'CREATE TABLE IF NOT EXISTS image_data (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, time_date VARCHAR(255), image_path VARCHAR(255), temp DOUBLE, facing VARCHAR(255));'
    cur.execute(stmt)

    # get root file path of every file in given directory
    for root, dirs, files in os.walk(os.path.abspath("Images/")):
        for file in files:
            image_path = os.path.join(root, file)
            print(image_path)

            # get temp and compass
            temp = round(sh.get_temperature(), 1)

            heading = round(sh.get_compass(), 1)
            if heading < 45 or heading > 315:
                facing = "North"
            elif heading < 135:
                facing = "East"
            elif heading < 225:
                facing = "South"
            else:
                facing = "West"

            # unixtimestamp of image file
            image_timestamp = os.path.getmtime(image_path)
            image_datetime = datetime.fromtimestamp(image_timestamp)
            time = image_datetime.strftime("%H:%M:%S %d/%m/%Y")

            # inserting data into database table
            stmt = 'INSERT INTO `image_data` (time_date, image_path, temp, facing) VALUES (%s, %s, %s, %s);'
            val = (time, image_path, temp, facing)
            cur.execute(stmt, val)

    # commit and close
    mariadb_connection.commit()
    cur.close()
    mariadb_connection.close()