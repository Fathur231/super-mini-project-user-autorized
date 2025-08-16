username = str(input("enter you're username for register : "))
password = str(input("enter you're password for register : "))

def function1():
        while True:
            loggin_name = str(input("please enter username = "))
            loggin_pass = str(input("please enter password = "))
            if loggin_name == username and loggin_pass == password :
             print("you're logged")
             break    
            else:
                print("something else not correct, try again")
                pass
def function2():
        while True:
            print("""
                    1.add you're information
                    2.check you're information
                    3.exit""")
            a = input("enter you're choice : ") 
            if a == "1":
                A = (f"""{input("you're name :")})
                         {input("you're phone :")})
                         {input("you're country :")}""")

            elif a == "2":
               print(A)

            elif a == "3":
                break

            else:a == str
            pass


print(function1())
print(function2())
print("thank you for using a my project -_-")