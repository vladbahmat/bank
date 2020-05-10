#!/usr/bin/env python3
import socket
from server import Client
from functions import *
import os

clear = lambda: os.system('cls')

def client_menu():
    client=Client()
    client.create_connection_client()
    while True:
        print("MENU")
        print("1.Admin authorization")
        print("2.Client authorization")
        print("3.Register as new client")
        print("3.Exit")
        buf=input("Enter a number from 1 to 3: ")
        client.sending(buf)
        buf=int(buf)
        if buf==1:
            buf=input("Please enter an admin login: ")
            client.sending(buf)
            buf=input("Please enter an admin password: ")
            client.sending(buf)
            check=client.recover()
            check=from_str_to_bool(check)
            if check:
                clear()
                while True:
                    print("ADMIN MENU")
                    print("1.Show all clients list")
                    print("0.Exit from admin account")
                    buf=input("Enter an operation number:")
                    client.sending(buf)
                    buf=int(buf)
                    if buf==1:
                        print("All clients list:")
                        for x in range(100):
                            buf=client.recover()
                            if buf=="end":
                                break
                            print(buf)
                            print(client.recover())
                            print(client.recover())
                    elif buf==0:
                        break
            else:
                clear()
                print("error adm auth")
        elif buf==2:
            buf=input("Please enter an client login: ")
            client.sending(buf)
            buf=input("Please enter an client password: ")
            client.sending(buf)
            check=client.recover()
            check=from_str_to_bool(check)
            print(check)
            if check:
                clear()
                print("good auth")
            else:
                clear()
                print("error auth")
        elif buf==3:
            buf=input("Please, enter your login: ")
            client.sending(buf)
            buf=input("Please, enter your password: ")
            client.sending(buf)
        elif buf==4:
            client.connection_end()
            return 0
        else:
            print("Please, enter a coorect number.")


client_menu()





