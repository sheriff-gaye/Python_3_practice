#!/usr/bin/pyhton3

#coupon validity testing 

from datetime import  datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):

    current = datetime.strptime(current_date, '%B %d, %Y').date()
    expire = datetime.strptime(expiration_date, '%B %d, %Y').date()

    if (entered_code == correct_code) and (current < expire):
        return True

    elif (entered_code==correct_code) and(current == expire):
        return True

    else:
        return False


print(check_coupon('123', '123', 'September 5, 2018', 'October 1, 2014'))
print(check_coupon('123', '123', 'September 5, 2015', 'October 1, 2014'))
