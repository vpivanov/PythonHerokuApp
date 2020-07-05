#Constance
import inspect

#Main Page
URL = 'http://the-internet.herokuapp.com/'

#Login Page
USERNAME = 'tomsmith'
PASSWORD = 'SuperSecretPassword!'

def whoami():
    return inspect.stack()[1][3]