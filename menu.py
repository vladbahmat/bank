class Menu:
    def work(self):
        print("""Choose an operation please:
        1.Admin
        2.User
        3.Exit""")
        choice=input()
        if choice==1:
            print("You enter like a damin.")
        elif choice==2:
            print("You enter like a user.")
        elif choice==3:
            print("Bye")
            return 0
        else:
            print("Enter correct number.")
            menu=Menu()
            menu.work()



menu=Menu()
menu.work()