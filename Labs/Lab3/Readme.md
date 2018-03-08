How to Setup
virtualenv -p python3 my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt



How to run Chat server
python3 server.py
How to run a Chat client
python3 client.py [username]

Expected Output

Bob's client
python3 client.py Bob
User[Bob] Connected to the chat server.
[Bob] > 
[Alice]: Hi from Alice.
[Smith]: Hi from Smith.
[Bob] > Hello World


Alice's client
python3 client.py Bob
User[Alice] Connected to the chat server. 
[Alice] > Hi from Alice.
[Smith]: Hi from Smith.
[Bob]: Hello World
