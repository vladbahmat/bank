import psycopg2
from server import Server
import datetime
from datetime import date
import time

server=Server()
class Admin:
    def __init__(self):
        server.create_connection_server()

    def show_user_list(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM clients LIMIT 100;')
        for row in cursor:
            server.sending(str(row[0]))
            time.sleep(0.1)
            server.sending(str(row[1]))
            time.sleep(0.1)
            server.sending(str(row[2]))
        server.sending("end")

    def add_bond(self):
        cost=server.recover()
        long=server.recover()
        user_id=0
        date=datetime.date.today()
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM bond LIMIT 100;')
        count=0
        for row in cursor:
            count=int(row[4])
        new_record=(str(count+1),str(cost),str(long),str(user_id),str(date))
        string="INSERT INTO bond (bond_id,cost,long,user_id,date) VALUES ('"+new_record[0]+"','" + new_record[1]+"','"+new_record[2]+"','"+new_record[3]+"','"+new_record[4]+"')"
        cursor.execute(string)
        conn.commit()

    def authorization(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM users LIMIT 10;')
        login=server.recover()
        password=server.recover()
        for row in cursor:
            if row[1]==login and row[2]==password:
                print("Good")
                self.login=login
                self.password=password
                self.user_id=row[0]
                return True
        else:
            print("Can't find this admin")
            return False

    def update_user_info(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        string="SELECT * FROM clients LIMIT 100"
        cursor.execute(string)
        for row in cursor:
            time.sleep(0.1)
            server.sending(str(row[0]))
            time.sleep(0.1)
            server.sending(str(row[1]))
            time.sleep(0.1)
            server.sending(str(row[2]))
        server.sending("end")
        buf=server.recover()
        if buf=='False':
            print("No client with this login")
        else:
            buf1=server.recover()
            string="UPDATE clients SET login='"+str(buf1)+"' WHERE login='"+str(buf)+"'"
            cursor.execute(string)
            conn.commit()

    @property
    def login(self):
        return self.login

    @property
    def password(self):
        return self.password

    @property
    def user_id(self):
        return self.user_id

    @login.setter
    def login(self,value):
        self.__dict__['login']=value

    @password.setter
    def password(self,value):
        self.__dict__['password']=value

    @user_id.setter
    def user_id(self,value):
        self.__dict__['user_id']=value

