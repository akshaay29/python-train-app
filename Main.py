"""
Author: Akshay Gupta

Description:
This is a simple train ticket booking system written in Python using Object-Oriented Programming (OOP). 
Users can upload multiple train details, and then interact with a specific train to:
1. Book tickets for one or more passengers.
2. Check the fare.
3. View the number of available seats.

Key Features:
- Supports multiple trains.
- Handles ticket booking with waitlist logic if seats run out.
- Ensures case-insensitive train name matching.
- Uses a class-based structure for better modularity and reuse.
"""
class Train:
    def __init__(self,trname,fare,seats):
        self.trname=trname
        self.fare=fare
        self.seats=seats
    def bookTicket(self,numOfpass):
        for i in range(0,numOfpass):
            if(self.seats==0):
               self.seats-=1
               print("\nSorry,this train doesn't have any available seats left. You are waitlisted:",-1*(self.seats))
            else:   
               print("Your ticket has been booked,Your ticket number:",self.seats)
               self.seats-=1
    def getFare(self):
        print(self.fare)
    def getStatus(self):
        print("Number of the seats remaining are:",self.seats)

numbTrain=int(input("\n Enter the number of trains data to be uploaded\n"))
tr=[]
if(numbTrain<=0):
    print("\nPlease enter valid number. You have chosen 0 or less than 0 as input\n")
else:
    for i in range(0,numbTrain):
     trname=input("\nenter the name of the train\n").lower()
     fare=int(input("\nenter the fare of the train\n"))
     seats=int(input("\nenter the total number of seats available\n")) 

     tr_obj=Train(trname,fare,seats)
     tr.append(tr_obj)
     i+=1
AccessTrain=input("\nenter the train which you want to explore\n")
found=0
for i in tr:
    if (AccessTrain.lower()==i.trname.lower()):
            found=1
            choice=int(input("\n 1=Bookticket \n 2=Fare Charges \n 3=Seats Available\n"))
            if(choice==1):
              passengerNo=int(input("Enter the number of passenger"))
              i.bookTicket(passengerNo)
            elif(choice==2):
              i.getFare()
            elif(choice==3):
              i.getStatus()
            break
    
if(found==0):
    print("You entered wrong train name.Please try again")

    

        
    
