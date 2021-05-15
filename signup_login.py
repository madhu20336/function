print("signup or login")
creataccount=input("do you want signup or login: ")
def page_login(login):
    if login==login:
        password=input("enter the number: ")
        def user_name(name):
            f=open("login.txt","r")
            m=f.read()
            if name not in m:
                password =input("enter the number: ")
                m=open("login.txt","a")
                m.write("\n")
                m.write(name)
                m.write("\n")
                m.write(password)
                m.close()
                print("your ")