import requests
import os
import time
import shutil
os.system("cls")
os.system("color 4f")
print("Loading....")
time.sleep(2)
os.system("cls")
os.system("color 5f")
print("""
                                                         
                      _ __   __ _ _ __ ___  ___ _ __  _   
                     | '_ \ / _` | '__/ __|/ _ \ '__|| |_ 
                     | |_) | (_| | |  \__ \  __/ | |_   _|
                     | .__/ \__,_|_|  |___/\___|_|   |_|  
                     |_|                  
                          Данная прогамма создана для:
                          Сохранение сайтов в документ
                                Тоесть парсинг
                           Программу создал: Мирес#7373
                                   Удачи! :D
                                   
                                   
                                   
-------------------------------------------------------------------------------                                   
""")
shutil.rmtree("C:\pars+")
link = input("Какой сайт будем парсить? (https://cait.com)")
os.system("color 5f")
namefile = input("Как назовём файл сайта? (Просто файл без расширения) : ")
yes = input("Название сайта: " + namefile + ".html верно? (Да, Нет): " )
if (yes == "Да"):   
    link = input("Какой сайт будем парсить? (https://cait.com)")
    os.system("color 5f")
    namefile = input("Как назовём файл сайта? (Просто файл без расширения) : ")
    os.system("color 5f")
    time.sleep(1);
    os.system("color 4f")
    time.sleep(1);
    os.system("color 2f")
    time.sleep(1);
    os.system("color 4f")
    time.sleep(1);
    os.system("color 2c")
    time.sleep(1);
    os.system("color 4f")
    responce = requests.get(link).text
    os.mkdir("C:\pars+")
    ddd = "C:\pars+"
    with open("C:/pars+" + "/" + namefile + ".html", "w", encoding="utf-8") as file:
        file.write(responce)
    os.system(r"explorer.exe C:\pars+")
    os.system("color 5f")
    print("Готово!")
    time.sleep(5)
else:
    link = input("Какой сайт будем парсить? (https://cait.com)")
    os.system("color 5f")
    namefile = input("Как назовём файл сайта? (Просто файл без расширения) : ")
    os.system("color 5f")
    time.sleep(1);
    os.system("color 4f")
    time.sleep(1);
    os.system("color 2f")
    time.sleep(1);
    os.system("color 4f")
    time.sleep(1);
    os.system("color 2c")
    time.sleep(1);
    os.system("color 4f")
    responce = requests.get(link).text
    os.mkdir("C:\pars+")
    ddd = "C:\pars+"
    with open("C:/pars+" + "/" + namefile + ".html", "w", encoding="utf-8") as file:
        file.write(responce)
    os.system(r"explorer.exe C:\pars+")
    os.system("color 5f")
    print("Готово!")
    time.sleep(5)

