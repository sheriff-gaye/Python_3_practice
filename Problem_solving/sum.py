

num = int(input("How many Numbers?"))
total_sum = 0

for i in range(num):
    numbers = float(input('Enter Number:'))
    total_sum += numbers

avg = total_sum/num

print(f'Average is {avg}')
