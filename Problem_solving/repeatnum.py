from sqlalchemy import false, true


def alternate(n, first_value, second_value):
    
    for i in range(1,n+1):
        if n%2==0:
            order=(n-1)*(first_value,second_value)
            return list(order)
        else:
            order=[(n-1)*(first_value,second_value)]
            order.pop()
            return list(order)
        




print(alternate(1,'true','false'))