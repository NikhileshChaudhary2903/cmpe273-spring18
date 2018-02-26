import requests 
import time
import sys

count=sys.argv[1]

count=int(count)

for i in range(count):
   r=requests.post('https://requestb.in/pssubsps', data={"ts":time.time(),'count':i+1})      
   print( "Request " + str(i+1))
   print (r.status_code) 	

 

