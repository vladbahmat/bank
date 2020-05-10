import psycopg2
from server import Server

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
            server.sending(str(row[1]))
            server.sending(str(row[2]))
        server.sending("end")

    def add_new_user(self):
        login=server.recover()
        password=server.recover()
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        new_record=(str(login),str(password))
        string="INSERT INTO users (login,password) VALUES ('" + new_record[0]+"','"+new_record[1]+"')"
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

