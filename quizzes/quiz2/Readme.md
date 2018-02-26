How to Setup
virtualenv my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt
How to run?
FLASK_APP=hello.py flask run
GET /
curl -i http://127.0.0.1:5000/
POST users
curl -i -X POST http://127.0.0.1:5000/users -d "name=foo"
Response

HTTP/1.0 201 Created
...
{
    "id": 1,
    "name": "foo"
}
GET users
curl -i -X GET http://127.0.0.1:5000/users/1 
Response

HTTP/1.0 200 OK
...
{
    "id": 1,
    "name": "foo"
}
DELETE users
curl -i -X DELETE http://127.0.0.1:5000/users/1 
Response

HTTP/1.0 204 No Content
...
