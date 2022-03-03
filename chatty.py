#required  modules 
import random
import datetime
import platform
from colorama import Fore, Back, Style
#Greeting part 
greets = ["Hello","Hi There!",'Namaskar 🙏','Glad to see you',"Yo ","What's Up ^_^"]
name="Chatty"
print(Fore.BLUE+name+":"+random.choice(greets))
#user input
user_responses = input("")

#Time 
current_time = datetime.datetime.now()
# print(current_time)

#platform 
plat = platform.platform()
print(plat)
