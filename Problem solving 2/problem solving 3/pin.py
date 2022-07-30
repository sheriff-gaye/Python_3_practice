def validate_pin(pin):

    if len(pin)==4:
        return True
    else:
        return False
print(validate_pin('1234'))
print(validate_pin('12aa'))

