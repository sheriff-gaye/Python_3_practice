
import goslate
insert_text=input('enter a text:')
new_gs=goslate.Goslate()
tran=new_gs.translate(insert_text,'es')
print(tran)
