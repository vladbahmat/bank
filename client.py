#!/usr/bin/env python3
import socket
from server import Client
from functions import *
import os
import msvcrt
import time
import colorama
from colorama import Fore,Style
import stdiomask

clear = lambda: os.system('cls')

def client_menu():
    colorama.init()
    client=Client()
    client.create_connection_client()
    while True:
        buf=1
        k=0
        while k!=13:
            time.sleep(0.1)
            os.system('cls')
            print(Style.RESET_ALL)
            print(Fore.GREEN+"MENU")
            print(Style.RESET_ALL)
            if buf==1:
                print(Fore.RED +"Авторизация администратора")
            else:
                print(Style.RESET_ALL)
                print("Авторизация администратора")
            if buf==2:
                print(Fore.RED+"Авторизация клиента")
            else:
                print(Style.RESET_ALL)
                print("Авторизация клиента")
            if buf==3:
                print(Fore.RED+"Регистрация")
            else:
                print(Style.RESET_ALL)
                print("Регистрация")
            if buf==4:
                print(Fore.RED+"Управление")
            else:
                print(Style.RESET_ALL)
                print("Управление")
            if buf==5:
                print(Fore.RED+"Выход")
            else:
                print(Style.RESET_ALL)
                print("Выход")
            x = msvcrt.kbhit()
            if x:
                k = ord(msvcrt.getch())
                if k == 80:
                    buf=buf+1
                    if buf>5:
                        buf=1
                if k == 72:
                    buf=buf-1
                    if buf<1:
                        buf=5
        client.sending(str(buf))
        buf=int(buf)
        if buf==1:
            buf=input("Пожалуйста введите логин: ")
            client.sending(buf)
            print("Пожалуйста введите пароль: ")
            buf=stdiomask.getpass(prompt='')
            client.sending(buf)
            check=client.recover()
            check=from_str_to_bool(check)
            if check:
                clear()
                while True:
                    buf=1
                    k=0
                    while k!=13:
                        time.sleep(0.1)
                        os.system('cls')
                        print(Style.RESET_ALL)
                        print("МЕНЮ АДМИНИСТРАТОРА")
                        print(Style.RESET_ALL)
                        if buf==1:
                            print(Fore.RED+"Просмотреть список всех клиентов")
                        else:
                            print(Style.RESET_ALL)
                            print("Просмотреть список всех клиентов")
                        if buf==2:
                            print(Fore.RED+"Добавить акцию в продажу")
                        else:
                            print(Style.RESET_ALL)
                            print("Добавить акцию в продажу")
                        if buf==3:
                            print(Fore.RED+"Изменить логин клиента")
                        else:
                            print(Style.RESET_ALL)
                            print("Изменить логин клиента")
                        if buf==4:
                            print(Fore.RED+"Выйти из аккаунта администратора")
                        else:
                            print(Style.RESET_ALL)
                            print("Выйти из аккаунта администратора")
                        x = msvcrt.kbhit()
                        if x:
                            k = ord(msvcrt.getch())
                            if k == 80:
                                buf=buf+1
                                if buf>4:
                                    buf=1
                            if k == 72:
                                buf=buf-1
                                if buf<1:
                                    buf=4
                    client.sending(str(buf))
                    buf=int(buf)
                    if buf==1:
                        os.system('cls')
                        print("Список всех клиентов:")
                        print("------------------------------------------------")
                        print("|   #   |     ЛОГИН     |        ПАРОЛЬ        |")
                        print("------------------------------------------------")
                        for x in range(100):
                            buf=client.recover()
                            time.sleep(0.1)
                            if buf=="end":
                                break
                            print("|%-7s|%-15s|%-22s|"% (buf,client.recover(),client.recover()))
                            print("------------------------------------------------")
                        k=0
                        while k!=13:
                            x = msvcrt.kbhit()
                            if x:
                                k = ord(msvcrt.getch())
                    elif buf==2:
                        os.system('cls')
                        print("Введите цену данной акции: ")
                        buf=int_control()
                        client.sending(str(buf))
                        print("Введите количество лет, на котороые акция выдается: ")
                        buf=int_control()
                        client.sending(str(buf))
                    elif buf==3:
                        os.system('cls')
                        print("Список клиентов:")
                        names_list=[]
                        print("------------------------------------------------")
                        print("|   #   |     ЛОГИН     |        ПАРОЛЬ        |")
                        print("------------------------------------------------")
                        for x in range(100):
                            time.sleep(0.1)
                            buf=client.recover()
                            if buf=="end":
                                break
                            time.sleep(0.1)
                            temp=client.recover()
                            time.sleep(0.1)
                            name=client.recover()
                            names_list.append(temp)
                            print("|%-7s|%-15s|%-22s|"%(buf,temp,name))
                            print("------------------------------------------------")
                        print("Введите логин клиента, который вы хотите изменить: ")
                        choose=input()
                        for name in names_list:
                            if str(name)==str(choose):
                                client.sending(str(choose))
                                buf=input("Введите новый логин для этого клиента:")
                                client.sending(str(buf))
                        else:
                            client.sending(str(False))
                    elif buf==4:
                        break
            else:
                clear()
                print("Ошибка авторизации администратора")
        elif buf==2:
            os.system('cls')
            buf=input("Пожалуйста введите ваш логин: ")
            time.sleep(0.1)
            client.sending(buf)
            print("Пожалуйста введите ваш пароль: ")
            buf=stdiomask.getpass(prompt='')
            time.sleep(0.1)
            client.sending(buf)
            check=client.recover()
            check=from_str_to_bool(check)
            if check:
                while True:
                    buf=1
                    k=0
                    while k!=13:
                        time.sleep(0.1)
                        os.system('cls')
                        print(Style.RESET_ALL)
                        print("МЕНЮ КЛИЕНТА")
                        print(Style.RESET_ALL)
                        if buf==1:
                            print(Fore.RED+"Добавить новый счет")
                        else:
                            print(Style.RESET_ALL)
                            print("Добавить новый счет")
                        if buf==2:
                            print(Fore.RED+"Просмотреть ваши счета")
                        else:
                            print(Style.RESET_ALL)
                            print("Просмотреть ваши счета")
                        if buf==3:
                            print(Fore.RED+"Удалить счет")
                        else:
                            print(Style.RESET_ALL)
                            print("Удалить счет")
                        if buf==4:
                            print(Fore.RED+"Приобрести акцию банка")
                        else:
                            print(Style.RESET_ALL)
                            print("Приобрести акцию банка")
                        if buf==5:
                            print(Fore.RED+"Принять участие в опросе")
                        else:
                            print(Style.RESET_ALL)
                            print("Принять участие в опросе")
                        if buf==6:
                            print(Fore.RED+"Поиск счета")
                        else:
                            print(Style.RESET_ALL)
                            print("Поиск счета")
                        if buf==7:
                            print(Fore.RED+"Просмотреть все ваши акции")
                        else:
                            print(Style.RESET_ALL)
                            print("Просмотреть все ваши акции")
                        if buf==8:
                            print(Fore.RED+"Выход из аккаунта пользователя")
                        else:
                            print(Style.RESET_ALL)
                            print("Выход из аккаунта пользователя")
                        x = msvcrt.kbhit()
                        if x:
                            k = ord(msvcrt.getch())
                            if k == 80:
                                buf=buf+1
                                if buf>8:
                                    buf=1
                            if k == 72:
                                buf=buf-1
                                if buf<1:
                                    buf=8
                    client.sending(str(buf))
                    buf=int(buf)
                    if buf==1:
                        os.system('cls')
                        print("Введите сумму, которую хотите положить на счет:")
                        buf=int_control()
                        time.sleep(0.1)
                        client.sending(str(buf))
                        buf=input(("Введите имя для вашего счета:"))
                        time.sleep(0.1)
                        client.sending(buf)
                    if buf==2:
                        os.system('cls')
                        buf=1
                        k=0
                        time.sleep(0.1)
                        while k!=13:
                            os.system('cls')
                            print(Style.RESET_ALL)
                            if buf==1:
                                print(Fore.RED+"Просмотреть все счета")
                            else:
                                print(Style.RESET_ALL)
                                print("Просмотреть все счета")
                            if buf==2:
                                print(Fore.RED+"Просмотреть счета, начиная с самого крупного")
                            else:
                                print(Style.RESET_ALL)
                                print("Просмотреть счета, начиная с самого крупного")
                            if x:
                                k = ord(msvcrt.getch())
                                if k == 80:
                                    buf=buf+1
                                    if buf>2:
                                        buf=1
                                if k == 72:
                                    buf=buf-1
                                    if buf<1:
                                        buf=2
                        #buf=input("Enter an operation number:")
                        client.sending(str(buf))
                        buf=int(buf)
                        if buf==1:
                            print("Ваши счета:")
                            print("------------------------------------------------")
                            print("|   #   |    ДЕНЬГИ    |        НАЗВАНИЕ        |")
                            print("------------------------------------------------")
                            for x in range(100):
                                buf=client.recover()
                                if buf=="end":
                                    break
                                print("|%-7s|%-14s|%-24s|"%(buf,client.recover(),client.recover()))
                                print("------------------------------------------------")
                            k=0
                            while k!=13:
                                x = msvcrt.kbhit()
                                if x:
                                    k = ord(msvcrt.getch())
                        elif buf==2:
                            print("Ваши счета, начиная с самого крупного:")
                            print("------------------------------------------------")
                            print("|   #   |    ДЕНЬГИ    |        НАЗВАНИЕ        |")
                            print("------------------------------------------------")
                            for x in range(100):
                                buf=client.recover()
                                if buf=="end":
                                    break
                                print("|%-7s|%-14s|%-24s|"%(buf,client.recover(),client.recover()))
                                print("------------------------------------------------")
                            k=0
                            while k!=13:
                                x = msvcrt.kbhit()
                                if x:
                                    k = ord(msvcrt.getch())
                        else:
                            print("Incorrect number")
                    if buf==3:
                        os.system('cls')
                        print("Ваши счета:")
                        names_list=[]
                        print("------------------------------------------------")
                        print("|   #   |    ДЕНЬГИ    |        НАЗВАНИЕ        |")
                        print("------------------------------------------------")
                        for x in range(100):
                            buf=client.recover()
                            if buf=="end":
                                break
                            time.sleep(0.1)
                            temp=client.recover()
                            time.sleep(0.1)
                            name=client.recover()
                            names_list.append(name)
                            print("|%-7s|%-14s|%-24s|"%(buf,temp,name))
                            print("------------------------------------------------")
                        print("Введите имя счета для удаления: ")
                        choose=input()
                        for name in names_list:
                            if str(name)==str(choose):
                                client.sending(str(choose))
                                break
                        else:
                            client.sending(str(False))
                    if buf==4:
                        os.system('cls')
                        print("Акции доступные к покупке:")
                        print("------------------------------------------------------------------")
                        print("|   #   |    ДЕНЬГИ    |        НАЗВАНИЕ        |      СРОК      |")
                        print("------------------------------------------------------------------")
                        bond_list=[]
                        for x in range(100):
                            buf=client.recover()
                            time.sleep(0.1)
                            if buf=="end":
                                break
                            bond_list.append(buf)
                            print("|%-7s|%-14s|%-24s|%-17s|"%(buf,client.recover(),client.recover(),client.recover()))
                            print("------------------------------------------------------------------")
                        print("Введите номер акции которую хотите приобрести: ")
                        choose=int_control()
                        for id in bond_list:
                            if str(id)==str(choose):
                                client.sending(str(choose))
                                break
                        else:
                            client.sending(str(False))
                    if buf==5:
                        os.system('cls')
                        print("Просим вас принять участие в опросе")
                        print("Из предложенных вариантов выберите один вариант валюты счета, который вам предпочтительнее")
                        c = [[0] * 4 for i in range(4)]
                        a=['BYN','USD','EUR','RUB']
                        b=['BYN','USD','EUR','RUB']
                        choose_list=[]
                        time.sleep(5)
                        for i in range(4):
                            for j in range(i,4):
                                if i!=j:
                                    buf=1
                                    k=0
                                    time.sleep(0.1)
                                    while k!=13:
                                        os.system('cls')
                                        print(Style.RESET_ALL)
                                        print('1 ',a[i],'or 2 ',b[j])
                                        print("Пожалуйста выберите число: ")
                                        if buf==1:
                                            print(Fore.RED+"1")
                                        else:
                                            print(Style.RESET_ALL)
                                            print("1")
                                        if buf==2:
                                            print(Fore.RED+"2")
                                        else:
                                            print(Style.RESET_ALL)
                                            print("2")
                                        x = msvcrt.kbhit()
                                        if x:
                                            k = ord(msvcrt.getch())
                                            if k == 80:
                                                buf=buf+1
                                                if buf>2:
                                                    buf=1
                                            if k == 72:
                                                buf=buf-1
                                                if buf<1:
                                                    buf=2
                                    choose=int(buf)
                                    if int(choose)==1:
                                        choose_list.append(a[i])
                                        c[i][j]=1
                                    elif int(choose)==2:
                                        choose_list.append(b[j])
                                        c[j][i]=1
                        client.sending(str(choose_list.count("BYN")))
                        time.sleep(0.1)
                        client.sending(str(choose_list.count("USD")))
                        time.sleep(0.1)
                        client.sending(str(choose_list.count("EUR")))
                        time.sleep(0.1)
                        client.sending(str(choose_list.count("RUB")))
                        print("Спасибо за участие в опросе!")
                    if buf==6:
                        os.system('cls')
                        buf=input("Введите имя счета для поиска:")
                        client.sending(buf)
                        print("Счета которые называются '"+str(buf)+"':")
                        for x in range(100):
                            buf=client.recover()
                            if buf=="end":
                                break
                            print(buf,client.recover(),client.recover())
                    if buf==7:
                        os.system('cls')
                        print("------------------------------------------------")
                        print("|   #   |    ДЕНЬГИ    |        НАЗВАНИЕ        |")
                        print("------------------------------------------------")
                        for x in range(100):
                            buf=client.recover()
                            if buf=="end":
                                break
                            print("|%-7s|%-14s|%-24s|"%(buf,client.recover(),client.recover()))
                            print("------------------------------------------------")
                        k=0
                        while k!=13:
                            x = msvcrt.kbhit()
                            if x:
                                k = ord(msvcrt.getch())
                    elif buf==8:
                        break
            else:
                clear()
                print("Ошибка авторизации пользователя")
        elif buf==3:
            os.system('cls')
            buf=input("Пожалуйста введите ваш логин: ")
            client.sending(buf)
            buf=input("Пожалуйста введите пароль: ")
            client.sending(buf)
        elif buf==4:
            os.system('cls')
            while True:
                buf=1
                k=0
                while k!=13:
                    os.system('cls')
                    time.sleep(0.1)
                    print(Style.RESET_ALL)
                    if buf==1:
                        print(Fore.RED+"Просмотр результатов опросов")
                    else:
                        print(Style.RESET_ALL)
                        print("Просмотр результатов опросов")
                    if buf==2:
                        print(Fore.RED+"Просмотреть список всех администраторов банка")
                    else:
                        print(Style.RESET_ALL)
                        print("Просмотреть список всех администраторов банка")
                    if buf==3:
                        print(Fore.RED+"Отправить отчет в печать")
                    else:
                        print(Style.RESET_ALL)
                        print("Отправить отчет в печать")
                    if buf==4:
                        print(Fore.RED+"Зарегистрировать нового администратора в системе")
                    else:
                        print(Style.RESET_ALL)
                        print("Зарегистрировать нового администратора в системе")
                    if buf==5:
                        print(Fore.RED+"Выйти из части управления")
                    else:
                        print(Style.RESET_ALL)
                        print("Выйти из части управления")
                    x = msvcrt.kbhit()
                    if x:
                        k = ord(msvcrt.getch())
                        if k == 80:
                            buf=buf+1
                            if buf>5:
                                buf=1
                        if k == 72:
                            buf=buf-1
                            if buf<1:
                                buf=5
                client.sending(str(buf))
                buf=int(buf)
                if buf==1:
                    os.system('cls')
                    print("Результаты опросов:")
                    for x in range(100):
                        time.sleep(0.1)
                        buf=client.recover()
                        if buf=="end":
                            break
                        time.sleep(0.1)
                        print("BYN-'"+client.recover()+"',USD-'"+client.recover()+"',EUR-'"+client.recover()+"',RUB-'"+client.recover()+"'")
                        print("Результаты опроса от пользователя: ",client.recover())
                        print("\n")
                    k=0
                    while k!=13:
                        x = msvcrt.kbhit()
                        if x:
                            k = ord(msvcrt.getch())
                if buf==2:
                    os.system('cls')
                    print("------------------------------------------------")
                    print("|   #   |     ЛОГИН     |        ПАРОЛЬ        |")
                    print("------------------------------------------------")
                    for x in range(100):
                        time.sleep(0.1)
                        buf=client.recover()
                        if buf=="end":
                            break
                        print("|%-7s|%-15s|%-22s|"%(buf,client.recover(),client.recover()))
                        print("------------------------------------------------")
                    k=0
                    while k!=13:
                        x = msvcrt.kbhit()
                        if x:
                            k = ord(msvcrt.getch())
                if buf==3:
                    os.system('cls')
                    print("Сгенерирован и отправлен в печать")
                if buf==4:
                    os.system('cls')
                    buf=input("Введите логин нового работника: ")
                    client.sending(buf)
                    buf=input("Введите пароль нового работника: ")
                    client.sending(buf)
                elif buf==5:
                    break
        elif buf==5:
            #client.connection_end()
            return 0


client_menu()





