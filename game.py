def chain(init_val, functions):
    
    def add10(init_val):
        return init_val+10

    def mul30(add10):
        return add10*30


print(chain(50,[add10,mul30]))



