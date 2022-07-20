import datetime
import DateAndTime
import KeepInList

def borrowBook():
    success=False
    while(True):
        fullName=input("Enter the full name of the borrower: ")
        if fullName.isdigit():
            print("please input alphabet from A-Z")
        else:
            break    
    t="Borrow-"+fullName+".txt"
    with open(t,"w+") as f:
        f.write(str(datetime.date.today()) + "\n\n")
        f.write("               Library Management System  \n")
        f.write("                   Borrowed By: "+ fullName +"\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )        
    
    
    while success==False:
        print("Please select a option below:")
        for i in range(len(KeepInList.bookname)):
            print("Enter", i, "to borrow book", KeepInList.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(KeepInList.quantity[a])>0):
                    print("Book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ KeepInList.bookname[a]+"\t\t  "+KeepInList.authorname[a]+"\n")

                    KeepInList.quantity[a]=int(KeepInList.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(KeepInList.bookname[i]+","+KeepInList.authorname[i]+","+str(KeepInList.quantity[i])+","+"$"+KeepInList.cost[i]+"\n")


                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? Press y for yes and n for no."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(KeepInList.bookname)):
                                print("Enter", i, "to borrow book", KeepInList.bookname[i])
                            a=int(input())
                            if(int(KeepInList.quantity[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ KeepInList.bookname[a]+"\t\t  "+KeepInList.authorname[a]+"\n")

                                KeepInList.quantity[a]=int(KeepInList.quantity[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(KeepInList.bookname[i]+","+KeepInList.authorname[i]+","+str(KeepInList.quantity[i])+","+"$"+KeepInList.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
