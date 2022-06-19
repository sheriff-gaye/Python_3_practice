

#///////////////////////////////
#      PROBLEM SOLVING  1
#///////////////////////////////
#The code request for list of
#numbers and output there average
#///////////////////////////////

num=int(input("How many Numbers?"))
total_sum=0

for i in range(num):
    numbers=float(input('Enter Number:'))
    total_sum+=numbers

avg=total_sum/num

print(f'Average is {avg}')