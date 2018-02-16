import time
import grpc
import ping_pb2
import ping_pb2_grpc
class PingClient():
    def _init_(self,host='0.0.0.0',port=3000):
        self.channel=grpc.insecure.channel('%s %d' %(host,port))
        self.stub=ping_pb2_grpc.PingPongStub(self.channel)

    def ping(self,data):
        req=Request(data=str(data))
        return self.stub.ping(req)

    def test():
        client=PingClient()
        resp=client.ping('ping')
        print('Response={}',format(resp.data)) 

if _name_== '__main__':
test()

         
