import Return
import KeepInList
import DateAndTime
import Borrow

def main():
    listOfBook=[]
    while(True):
        print(" ======     Welcome to the library management system     ====== ")
        print("------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To exit")
        try:
            a=int(input("Press the keys from 1-4: "))
            print()
            if(a==1):
                file=open("Stock.txt","r")
                for line in file.readlines():
                    listOfBook.append(line.strip().split(','))
                file.close()
                print("*********************************Book List*********************************")
                print("Title of the book","\t", "Author Name","\t\t", "Quantity","\t", "Price")
                print("----------------------------------------------------------------------------------------------------")
                for book in listOfBook:
                    if len(book[0])<15 and len(book[0])<22:
                        print(book[0],"\t\t",book[1],"\t\t",book[2],"\t\t",book[3])
                    elif len(book[0])>=22:
                        print(book[0]+"  "+book[1],"\t\t",book[2],"\t\t",book[3])
                    else :
                        print(book[0],"\t\t",book[1],"\t",book[2],"\t\t",book[3])
            elif(a==2):
                KeepInList.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                KeepInList.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thanks for using this library management system")
                break
            else:
                print("Please enter a valid choice ")
        except ValueError:
            print("Please input as suggested.")
main()
