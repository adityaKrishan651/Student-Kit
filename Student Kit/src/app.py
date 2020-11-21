import views
from views import *

views.main()

url = "http://www.kite.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
    for i in range(5):
	    print("No internet connection.")
else:
    ui.run()    