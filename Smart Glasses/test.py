import os
from datetime import datetime

a_list = []

for root, dirs, files in os.walk(os.path.abspath("Images/")):
    for file in files:
        image_path = os.path.join(root, file)
        image_timestamp = os.path.getmtime(image_path)
        image_datetime = datetime.fromtimestamp(image_timestamp)
        image_time = image_datetime.strftime("%H:%M:%S %d/%m/%Y")
        
        a = image_path, image_time
        a_list.append(a)

print(a_list)
print(a_list[0])