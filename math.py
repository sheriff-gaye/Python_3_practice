
#this program is to converte weight 

weight=float(input('Enter your Weight:'))

unit=str(input('K or L:'))

if(unit.upper()=='L'):
    converter=weight/0.45
    print('Your weight in Lbs is',converter)

else:
    converter=weight*0.45
    print("Your weight in Kg is", converter)

print('Thank you🙌')
