# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://api.github.com/events"
  
# location given here 
r = requests.get(URL)


print(r.text)