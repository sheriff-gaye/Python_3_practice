
import time


code=123
user_input=int(input("Enter Your Pin..:"))

if code==user_input:
    balance=200
    time.sleep(5)
    print("WELCOME TO STANDARD CHARTETED BANK")
   
    time.sleep(6)

    print('***************************************')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('***************************************')

    print('')
    print('-Select 1 to Withdraw')
    print('-Select 2 to Deposit')
    print('-Select 3 to Check Blanance')
    print('-Select 4 to Change Pin')
    print('')


    print("***************************************")
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('***************************************')


    transaction=int(input("Enter Transaction Number :"))
    if transaction==1:
        withdraw=int(input('Enter Amount :'))
        if balance !=0 and withdraw <balance:
             print('You have Successfully withdraw $',withdraw)
        
        else:
            print('You cannot Withdraw more than your Balance')

    elif transaction==2:
        Deposit=int(input('Deposit Amount:'))
        balance +=Deposit
        print('You have successfully Deposit',Deposit)
        print('Your Current Blance is',balance)

    elif transaction==3:
       print('Your Balance is',balance)




else:
    print('OOps! Wrong Pin Try Again')



