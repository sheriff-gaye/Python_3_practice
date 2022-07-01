def opposite(number):
    if number<0:
        return abs(number)
    else:
        return ("-{}".format(number))


print(opposite(7))