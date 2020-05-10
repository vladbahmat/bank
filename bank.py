from admin import Admin,server
from clients import Clients
import psycopg2

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
                        elif buf=='0':
                            break
                else:
                    print("error adm auth")
            elif buf=='2':
                check=client.authorization()
                server.sending(str(check))
                if check:
                    print("good user auth")
                else:
                    print("error user auth")
            elif buf=='3':
                Bank.register_new_client()
            elif buf=='4':
                return 0
            else:
                print("Please, enter a coorect number.")

    def show_admins_list(self):
            conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM users LIMIT 100;')
            for row in cursor:
                server.sending(str(row[0]))
                server.sending(str(row[1]))
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
        new_record=(str(count+1),str(login),str(password))
        string="INSERT INTO clients (id,login,password) VALUES ('"+new_record[0]+"','" + new_record[1]+"','"+new_record[2]+"')"
        cursor.execute(string)
        conn.commit()


bank=Bank()
bank.menu()