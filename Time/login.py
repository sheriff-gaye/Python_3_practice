
import time

username='sheriff'
password='Sheriff#2021'

user_username=input('Enter Username:')
user_password=input('Enter Password:')

if user_username==username and user_password==password:
    print('Acess Granted')
    print('Please Wait')
    time.sleep(5)
    print('Ok Loading .........')
    time.sleep(3)
    print('Loading ....')
    time.sleep(2)
    print('Loading .......')
    time.sleep(1)
    print('Loading Completed............')
    time.sleep(5)
    print('You have been login successfully 😉🙌😀')

elif user_username!= username and  user_password==password:
    print('Incorrect Username')

elif user_username==username and user_password !=password:
    print('Incorrect Password')

else:
    time.sleep(3)
    print(' Wrong Username \n Wrong Password \n Try again Later')