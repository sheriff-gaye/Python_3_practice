
import json

player1='{"name":"sheriff","age":20,"hobby":"programming"}'

# with open('player.txt','w') as json_file:
    # json.dump(player1,json_file)
    
x=json.loads(player1)

print(json.dumps(x, indent=4 ,sort_key=True))