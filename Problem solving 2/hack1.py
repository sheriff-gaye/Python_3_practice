class Car:
    def __init__ (self,speed,unit):
        self.speed=speed
        self.unit=unit    
        # return ("Car with the maximum speed of {} {}".format(int(self.speed),str(self.unit)))
        return (self.unit)


class Boat:
    pass





benx=Car(120,'kms')
print(benx)