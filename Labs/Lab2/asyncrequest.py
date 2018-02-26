import asyncio
import requests, time
import sys
def request(n):
	r = requests.post("https://requestb.in/18uxf0t1", data={"ts":time.time()})
	print (r.content.decode('UTF-8') ,n)

async def async_call():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            request, 
            i
        )
        for i in range(count)
    ]
    for response in await asyncio.gather(*futures):
        pass

count=sys.argv[1]

count=int(count)

loop = asyncio.get_event_loop()
loop.run_until_complete(async_call())

print("Synchronous Call:")
count=sys.argv[1]

count=int(count)

for i in range(count):
   r=requests.post('https://requestb.in/18uxf0t1', data={"ts":time.time(),'count':i+1})      
   print( "Request " + str(i+1))
   #print (r.status_code) 	
