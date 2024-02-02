from kafka import KafkaConsumer, KafkaProducer
from const import *
import threading

from concurrent import futures
import logging

import grpc
import iot_service_pb2
import iot_service_pb2_grpc

current_acceleration = 'void'
acceleration_access = 3
create_access = 1
current_light_level = 'void'
light_access = 3

DB=[
 {
 'login':'admin',
 'password':'admin',
 'access':1
 },
 {
 'login':'user',
 'password':'user',
 'access':2
 }]

last_key = 1


TA=[
    {
        'key': 1,
        'login':'admin',
        'access': 1
    }
]


def consume_acceleration():
    global current_acceleration
    consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER+':'+KAFKA_PORT)
    consumer.subscribe(topics=('acceleration'))
    for msg in consumer:
        print ('Received Acceleration: ', msg.value.decode())
        current_acceleration = msg.value.decode()

def consume_light_level():
    global current_light_level
    consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER+':'+KAFKA_PORT)
    consumer.subscribe(topics=('lightlevel'))
    for msg in consumer:
        print ('Received Light Level: ', msg.value.decode())
        current_light_level = msg.value.decode()

#verifica o acesso
def verify(key,needed):
    ta = [ t for t in TA if (t['key'] == key) ]
    if not ta:
        return 'Login Necessary'
    if ta[0]['access'] > needed:
        return 'Access Denied'
    return 'OK'



class IoTServer(iot_service_pb2_grpc.IoTServiceServicer):

    def CreateUser(self, request, context):
        ver = verify(request.key,create_access)
        if ver != 'OK':
            iot_service_pb2.AccelerationReply(status=ver)
        usr = {
            'login':request.login,
            'password':request.password,
            'access':request.access
        }
        DB.append(usr)
        return iot_service_pb2.StatusReply(status='OK')

    def UserLogin(self, request, context):
        global last_key
        usr = [ us for us in DB if (us['login'] == request.login) ]
        if not usr:
            return iot_service_pb2.LoginReply(status='User Doesnt Exists',key = -1,access = -1)
        usr = [ us for us in usr if (us['password'] == request.password) ]
        if not usr :
            return iot_service_pb2.LoginReply(status='Wrong Password',key = -1,access = -1)
        my_key= last_key
        last_key += 1
        ta = {
            'key':my_key,
            'login':usr[0]['login'],
            'access':usr[0]['access']
        }
        TA.append(ta)
        return iot_service_pb2.LoginReply(status='OK',key = my_key,access = usr[0]['access'])

    def SayAcceleration(self, request, context):
        ver = verify(request.key,acceleration_access)
        if ver != 'OK':
            iot_service_pb2.AccelerationReply(status=ver,acceleration=-1)
        return iot_service_pb2.AccelerationReply(status=ver,acceleration=current_acceleration)

    def SayLightLevel(self, request, context):
        ver = verify(request.key,acceleration_access)
        if ver != 'OK':
            iot_service_pb2.AccelerationReply(status=ver,acceleration=-1)
        return iot_service_pb2.LightLevelReply(status='OK',lightLevel=current_light_level)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iot_service_pb2_grpc.add_IoTServiceServicer_to_server(IoTServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()

    trd1 = threading.Thread(target=consume_acceleration)
    trd1.start()

    trd2 = threading.Thread(target=consume_light_level)
    trd2.start()

    serve()
