import datetime
import KeepInList
import DateAndTime
def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + DateAndTime.getDate()+"    Time:"+ DateAndTime.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")
        
    d = {}
    borrowFile = open("Borrow-"+name+".txt","r")
    (key,val) = ("Date",borrowFile.readline().strip().split(" : "))
    d[key] = val
    print(d[key][0])

    year, month, day = d[key][0].split('-')
    date1 = datetime.datetime(int(year), int(month), int(day)) 
    newDate = date1 + datetime.timedelta(days=10)
    #if date1> newDate:
        

    total = 0.0
    for i in range(3):
        if KeepInList.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+KeepInList.bookname[i]+"\t\t$"+KeepInList.cost[i]+"\n")
                KeepInList.quantity[i]=int(KeepInList.quantity[i])+1
            total+=float(KeepInList.cost[i])
    print("Returned successful")
    print("\t\t\t\t\t\t\t"+"$"+str(total))
                
    if newDate <= datetime.datetime.now():
        remainingDay = datetime.datetime.now() - newDate
        totalAmount = str(float(KeepInList.cost[i]) + (float(remainingDay.days)*float(KeepInList.cost[i])))
        with open(b,"a")as f:
            f.write("\t\t\t\t\tTotal: $"+ str(totalAmount))

    with open("Stock.txt","w+") as f:
            for i in range(3):
                f.write(KeepInList.bookname[i]+","+KeepInList.authorname[i]+","+str(KeepInList.quantity[i])+","+"$"+KeepInList.cost[i]+"\n")
