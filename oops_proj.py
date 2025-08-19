class Chatbook:
    def __init__(self):
        self.username=""
        self.password=''
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input=input("""welcome to chatbook
                         1.press 1 for signup
                         2.press 2 for signin
                         3.press 3 write a post
                         4.press 4 message to friend
                         5.press any other key for exit""")
        if user_input=="1":
            pass
        elif user_input=="2":
            pass
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

obj=Chatbook()

        
