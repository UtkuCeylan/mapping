import csv
import random
import time

#Yonler : 0 -> Yukari
#         1 -> Sag
#         2 -> Asagi
#         3 -> Sol

x_value = 0 #Arac Konumu X -> Baslangic Icin Her Zaman (0,0)
y_value = 0 #Arac Konumu Y -> Baslangic Icin Her Zaman (0,0)
frw_sensor = 0 
left_sensor = 5 
direction = 2 
obstacle_x = 0
obstacle_y = 0

fieldnames = ["x_value","y_value", "frw_sensor", "left_sensor", "direction", "obstacle_x", "obstacle_y"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "y_value": y_value,
            "frw_sensor": frw_sensor,
            "left_sensor": left_sensor,
            "direction" : direction,
            "obstacle_x": obstacle_x,
            "obstacle_y": obstacle_y,
        }

        csv_writer.writerow(info)
        print(x_value,y_value, frw_sensor, left_sensor,direction, obstacle_x, obstacle_y)

        if(direction == 1):

            x_value = x_value + 1   # ************ 1 yerine aracin 1 saniyede yer degistirme degeri gelecek ************
            y_value = y_value 
            obstacle_x = x_value
            obstacle_y = y_value + left_sensor

        elif(direction == 2):

            x_value = x_value   
            y_value = y_value - 1  # ************ 1 yerine aracin 1 saniyede yer degistirme degeri gelecek ************
            obstacle_x = x_value + left_sensor
            obstacle_y = y_value 

        elif(direction == 3):

            x_value = x_value - 1    # ************ 1 yerine aracin 1 saniyede yer degistirme degeri gelecek ************
            y_value = y_value  
            obstacle_x = x_value 
            obstacle_y = y_value - left_sensor

        elif(direction == 0):

            x_value = x_value    
            y_value = y_value + 1  # ************ 1 yerine aracin 1 saniyede yer degistirme degeri gelecek ************  
            obstacle_x = x_value - left_sensor
            obstacle_y = y_value 

        else:
            x_value = x_value
            y_value = y_value
            obstacle_x = obstacle_x
            obstacle_y = obstacle_y

    time.sleep(1)


        
    

