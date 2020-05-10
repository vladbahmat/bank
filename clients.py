from admin import server
import psycopg2

class Clients:
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

    def authorization(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM clients LIMIT 10;')
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
            print("Can't find this user")
            return False