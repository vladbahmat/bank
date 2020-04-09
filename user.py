import psycopg2

class User:
    def show_user_list(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM users LIMIT 10;')
        for row in cursor:
            print(row[0],row[1],row[2])

    def add_new_user(self,login,password):
        self.login=login
        self.password=password
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        new_record=(str(self.login),str(self.password))
        string="INSERT INTO users (login,password) VALUES ('" + new_record[0]+"','"+new_record[1]+"')"
        print(string)
        cursor.execute(string)
        conn.commit()

    def authorization(self,login,password):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM users LIMIT 10;')
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

    @property
    def login(self):
        return self.login

    @property
    def password(self):
        return self.password

    @property
    def user_id(self):
        return self.user_id

user=User_server()
user.show_user_list()
user.authorization("admin","admin")