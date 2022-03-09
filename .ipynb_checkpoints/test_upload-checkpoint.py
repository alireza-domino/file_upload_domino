from domino import Domino
import os


print(os.environ['DOMINO_USER_API_KEY'])
print(os.environ['DOMINO_API_HOST'])

myDomino = Domino("./",
                api_key=os.environ['DOMINO_USER_API_KEY'],
                host=os.environ['DOMINO_API_HOST'])



