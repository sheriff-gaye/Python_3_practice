
import random

def play():
    user=input("r for rock, p for paper, s for scissor:")
    computer= random.choice(['r','p','s'])
    
    if user==computer:
        print('Tie')
        
    #r>s 
        
    
play()