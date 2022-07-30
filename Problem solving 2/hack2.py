class Item:
    
    def __init__(self,n='',p=0):
        self.name=n
        self.price=p

    def give_item(self,name,price):
        return name,price

class ShoppingCart:
    
    def __init__(self,name0='',price0=0):
        self.nameI=name0
        self.priceI=price0
        self.name_list=[]
        self.price_list=[]

    
    def call_item(self,nameI,priceI):
        nout,pout=Item.give_item(self,nameI,priceI)
        return nout,pout

    def add(self,nameI,priceI):
        nout,pout=self.call_item(nameI,priceI)

        self.name_list=self.name_list+[nout]
        print('Your cart contains',self.name_list)

        self.price_list=self.price_list+[pout]

        return self.name_list,self.price_list


    def total(self):
        result=sum(self.price_list)
        print('Total shopping cart',result)
        print(result)
        return result

    def num_of_carts(self):
        num_items=len(self.name_list)
        print('Total shopping cart items',num_items)
        print(num_items)
        return num_items

    


