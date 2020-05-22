from admin import server
import psycopg2
from bond import Bond
import time
from account import Account
from bond import Bond

class Clients:
    def __init__(self):
        self.login=str
        self.password=str
        self.user_id=int
        self.accout=[Account]
        self.bond=[Bond]

    #@property
    #def login(self):
     #   return self.login

    @property
    def password(self):
        return self.password

    #@property
    #def user_id(self):
     #   return self.user_id

    #@login.setter
    #def login(self,value):
     #   self.__dict__['login']=value

    @password.setter
    def password(self,value):
        self.__dict__['password']=value

    #@user_id.setter
    #def user_id(self,value):
     #   self.__dict__['user_id']=value

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

    def add_new_account(self):
        money=server.recover()
        account_name=server.recover()
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM accounts LIMIT 10;')
        for row in cursor:
            count=int(row[1])
        new_record=(str(self.user_id),str(count+1),str(money),str(account_name))
        string="INSERT INTO accounts (client_id,account_id,money,account_name) VALUES ('" + new_record[0]+"','"+new_record[1]+"','" + new_record[2]+"','" + new_record[3]+"')"
        cursor.execute(string)
        conn.commit()

    def show_accounts(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        string="SELECT * FROM accounts WHERE client_id = '"+str(self.user_id)+"'"
        cursor.execute(string)
        for row in cursor:
            time.sleep(0.1)
            server.sending(str(row[1]))
            time.sleep(0.1)
            server.sending(str(row[2]))
            time.sleep(0.1)
            server.sending(str(row[3]))
        server.sending("end")

    def delete_account(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        string="SELECT * FROM accounts WHERE client_id = '"+str(self.user_id)+"'"
        cursor.execute(string)
        for row in cursor:
            time.sleep(0.1)
            server.sending(str(row[1]))
            time.sleep(0.1)
            server.sending(str(row[2]))
            time.sleep(0.1)
            server.sending(str(row[3]))
        server.sending("end")
        buf=server.recover()
        if buf=='False':
            print("No account with this name")
        else:
            string="DELETE FROM accounts WHERE account_name='"+str(buf)+"'"
            cursor.execute(string)
            conn.commit()

    def buy_bond(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM bond LIMIT 10;')
        for row in cursor:
            if row[3]==0:
                time.sleep(0.1)
                server.sending(str(row[4]))
                time.sleep(0.1)
                server.sending(str(row[1]))
                time.sleep(0.1)
                server.sending(str(row[0]))
                time.sleep(0.1)
                server.sending(str(row[2]))
        server.sending("end")
        buf=server.recover()
        if buf=='False':
            print("No bond with this number")
        else:
            string="UPDATE bond SET user_id ='"+str(self.user_id)+"' WHERE bond_id ='"+str(buf)+"'";
            cursor.execute(string)
            conn.commit()

    def survey(self):
        time.sleep(0.1)
        byn=server.recover()
        time.sleep(0.1)
        usd=server.recover()
        time.sleep(0.1)
        eur=server.recover()
        time.sleep(0.1)
        rub=server.recover()
        print(byn,usd,eur,rub)
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM survey LIMIT 100;')
        count=0
        for row in cursor:
            count=int(row[0])
        new_record=(str(count+1),str(byn),str(usd),str(eur),str(rub),str(self.login))
        string="INSERT INTO survey (survey_id,byn,usd,eur,rub,login) VALUES ('" + new_record[0]+"','"+new_record[1]+"','" + new_record[2]+"','" + new_record[3]+"','" + new_record[4]+"','" + new_record[5]+"')"
        cursor.execute(string)
        conn.commit()

    def show_top_accounts(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        string="SELECT * FROM accounts WHERE client_id = '"+str(self.user_id)+"' ORDER BY money DESC"
        cursor.execute(string)
        for row in cursor:
            time.sleep(0.1)
            server.sending(str(row[1]))
            time.sleep(0.1)
            server.sending(str(row[2]))
            time.sleep(0.1)
            server.sending(str(row[3]))
        server.sending("end")

    def find_account(self):
        temp=server.recover()
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        string="SELECT * FROM accounts WHERE client_id = '"+str(self.user_id)+"' AND account_name= '"+str(temp)+"'"
        cursor.execute(string)
        for row in cursor:
            time.sleep(0.1)
            server.sending(str(row[1]))
            time.sleep(0.1)
            server.sending(str(row[2]))
            time.sleep(0.1)
            server.sending(str(row[3]))
        server.sending("end")

    def show_bonds(self):
        conn=psycopg2.connect(dbname='bank',user='postgres',password='Lipetsk4859',host='localhost')
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM bond LIMIT 10;')
        for row in cursor:
            if row[3]==self.user_id:
                time.sleep(0.1)
                server.sending(str(row[1]))
                time.sleep(0.1)
                server.sending(str(row[0]))
                time.sleep(0.1)
                server.sending(str(row[2]))
        server.sending("end")