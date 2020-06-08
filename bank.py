from admin import Admin,server
from clients import Clients
import psycopg2
import time
from functions import text_string

class Bank:
    def menu(self):
        client=Clients()
        admin=Admin()
        while True:
            buf=server.recover()
            if buf=='1':
                check=admin.authorization()
                server.sending(str(check))
                if check:
                    while True:
                        buf=server.recover()
                        if buf=='1':
                            admin.show_user_list()
                        elif buf=='2':
                            admin.add_bond()
                        elif buf=='3':
                            admin.update_user_info()
                        elif buf=='4':
                            break
                else:
                    print("error adm auth")
            elif buf=='2':
                check=client.authorization()
                server.sending(str(check))
                if check:
                    while True:
                        buf=server.recover()
                        if buf=='1':
                            client.add_new_account()
                        elif buf=='2':
                            buf=server.recover()
                            if buf=='1':
                                client.show_accounts()
                            elif buf=='2':
                                client.show_top_accounts()
                            else:
                                print("client error")
                        elif buf=='3':
                            client.delete_account()
                        elif buf=='4':
                            client.buy_bond()
                        elif buf=='5':
                            client.survey()
                        elif buf=='6':
                            client.find_account()
                        elif buf=='7':
                            client.show_bonds()
                        elif buf=='8':
                            break
                else:
                    print("error user auth")
            elif buf=='3':
                Bank.register_new_client()
            elif buf=='4':
                while True:
                    buf=server.recover()
                    if buf=='1':
                        Bank.show_surves()
                    if buf=='2':
                        Bank.show_admins_list()
                    if buf=='3':
                        Bank.doc()
                    if buf=='4':
                        Bank.add_admin()
                    elif buf=='5':
                        break
            elif buf=='5':
                return 0
            else:
                print("Please, enter a coorect number.")

    @staticmethod
    def show_admins_list():
            conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM users LIMIT 100;')
            for row in cursor:
                time.sleep(0.1)
                server.sending(str(row[0]))
                time.sleep(0.1)
                server.sending(str(row[1]))
                time.sleep(0.1)
                server.sending(str(row[2]))
            server.sending("end")

    @staticmethod
    def register_new_client():
        login=server.recover()
        password=server.recover()
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM clients LIMIT 100;')
        for row in cursor:
            count=int(row[0])
        new_record=(str(count+2),str(login),str(password))
        string="INSERT INTO clients (id,login,password) VALUES ('"+new_record[0]+"','" + new_record[1]+"','"+new_record[2]+"')"
        cursor.execute(string)
        conn.commit()

    @staticmethod
    def show_surves():
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM survey LIMIT 100;')
        for row in cursor:
            server.sending(str(row[0]))
            time.sleep(0.3)
            server.sending(str(row[1]))
            time.sleep(0.3)
            server.sending(str(row[2]))
            time.sleep(0.3)
            server.sending(str(row[3]))
            time.sleep(0.3)
            server.sending(str(row[4]))
            time.sleep(0.3)
            server.sending(str(row[5]))
        server.sending("end")

    @staticmethod
    def doc():
        f=open('doc.txt','w')
        f.write(text_string)
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM users LIMIT 100;')
        for row in cursor:
            f.write("\n")
            f.write(str(row[0]))
            f.write("\n")
            f.write(str(row[1]))
            f.write("\n")
            f.write(str(row[2]))
            f.write("\n")

    @staticmethod
    def add_admin():
        login=server.recover()
        password=server.recover()
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM users LIMIT 100;')
        for row in cursor:
            count=int(row[0])
        new_record=(str(count+1),str(login),str(password))
        string="INSERT INTO users (id,login,password) VALUES ('"+new_record[0]+"','" + new_record[1]+"','"+new_record[2]+"')"
        cursor.execute(string)
        conn.commit()



bank=Bank()
bank.menu()