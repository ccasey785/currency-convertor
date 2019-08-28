#author of code is Christopher Casey
from decimal import Decimal
print("Welcome! Please use this tool to estimate your trip cost. Do not")
print("use the dollar sign or commas when entering your numbers!\n")
#function for obtaining user input
def getInput(tCost = 0, hCost = 0, rcCost = 0, lCost = 0):
    
    #testing for invalid input that would throw exeption

    while True:
        try:
            tCost = float(input('Please enter the cost of your travel: '))
                      
            if tCost < 0:
                print("Please enter only positive integers!")
            
            else:                   
                break
        except ValueError:
            print("Please enter only positive integers. DO NOT INCLUDE THE $ symbol!")
            
    #testing for invalid input that would throw exeption

    while True:
        try:
            hCost = float(input("Please enter the cost of your hotel: "))
            if hCost < 0:
                print("Please enter only positive integers!")
            else:
                break
        except ValueError:
            print("Please enter only integers. DO NOT INCLUDE THE $ symbol!")
            
        #testing for invalid input that would throw exeption
        
    while True:
        try:
            rcCost = float(input("Please enter the cost of your rental car: "))
            if rcCost < 0:
                print("Please enter only positive integers!")
            else:
                break
        except ValueError:
            print("Please enter only integers. DO NOT INCLUDE THE $ symbol!")

        #testing for invalid input that would throw exeption

    while True:
        try:
            lCost = float(input("Please enter the cost of the labor for your trip: "))
            if lCost < 0:
                print("Please enter only positive integers")
            else:
                break
        except ValueError:
            print("Please enter only integers. DO NOT INCLUDE THE $ symbol!")
                           
    global inTotal
    inTotal = tCost + hCost + rcCost + lCost

                        
   
# function for converting user input total to Australian dollar  
def convertTotal(audTotal = 0):
        audTotal = round(inTotal * 1.48, 2)
        print('')
        print("Your total is $%.2f for this trip in American currency" % inTotal)
        print("Your total is $%.2f for this trip in Australian currency" % audTotal)
    

#calling the functions to perform their job
getInput()   
convertTotal()
