def warn_the_sheep(queue):
    
    if queue[-1]!='wolf' :
        wnum=queue.index('wolf')
        res=("Oi! Sheep number {}! You are about to be eaten by a wolf!".format((len(queue))-(wnum+1)))
        return res
    elif queue[-1]=='wolf':
        res=("Pls go away and stop eating my sheep")
        return res

print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
print(warn_the_sheep(['sheep', 'wolf', 'sheep']))
print(warn_the_sheep(['sheep', 'sheep', 'wolf']))


