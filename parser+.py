import requests
import os
import time
import shutil
import webbrowser
os.system("cls")
os.system("color 4f")
print("Loading....")
time.sleep(1)
languadge = input("Input you'r language (English, Russian): ")
if(languadge == "Russian"):
    os.system("color 1f")
    time.sleep(1)
    os.system("color ff")
    time.sleep(1)
    os.system("color 4f")
    time.sleep(1)
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
        print("Готово! Не удаляй эту папку. При запуске этой программы повторный раз она сама удалиться.")
        time.sleep(2)
        webbrowser.open("https://discord.gg/Mbupcbtq7x")
        time.sleep(5)
        
if (languadge == "English"):
    time.sleep(2)
    os.system("cls")
    os.system("color 5f")
    print("""
                                                            
                        _ __   __ _ _ __ ___  ___ _ __  _   
                        | '_ \ / _` | '__/ __|/ _ \ '__|| |_ 
                        | |_) | (_| | |  \__ \  __/ | |_   _|
                        | .__/ \__,_|_|  |___/\___|_|   |_|  
                        |_|                  
                            created by: Мирес#7373
                                    Lucky! :D
                                    
                                    
                                    
    -------------------------------------------------------------------------------                                   
    """)
    shutil.rmtree("C:\pars+")
    link = input("What site will we parse? (https://sait.com)")
    os.system("color 5f")
    namefile = input("What is the name of the site file? (Just a file with no extension) : ")
    yes = input("name site: " + namefile + ".html yes? (Y, N): " )
    if (yes == "Y"):   
        os.system("color 5f")
        time.sleep(1);
        os.system("color 4f")
        time.sleep(1);
        os.system("color 2f")
        time.sleep(1);
        os.system("color 4f")
        time.sleep(1);
        os.system("color 2c")
        responce = requests.get(link).text
        os.mkdir("C:\pars+")
        ddd = "C:\pars+"
        with open("C:/pars+" + "/" + namefile + ".html", "w", encoding="utf-8") as file:
            file.write(responce)
        os.system(r"explorer.exe C:\pars+")
        os.system("color 5f")
        print("Ready!! Don't remove this folder.")
        time.sleep(2)
        webbrowser.open("https://discord.gg/Mbupcbtq7x")
        time.sleep(5)
    else:
        link = input("What site will we parse? (https://sait.com)")
        os.system("color 5f")
        namefile = input("What is the name of the site file? (Just a file with no extension) : ")
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
        print("Ready!! Don't remove this folder.")
        time.sleep(2)
        webbrowser.open("https://discord.gg/Mbupcbtq7x")
        time.sleep(5)
