# import socket programming library
import socket
import select, socket, sys , queue
from _thread import *
import threading





def Connection(s,inputs,outputs,message_queues) :
    connection, client_address = s.accept()
    connection.setblocking(0)
    inputs.append(connection)
    message_queues[connection] = queue.Queue()

    print('Connected to :', connection, ':',client_address,"\n\n")

def add_data(s,data,inputs,outputs,message_queues) :
    try :
        message_queues[s].put(str(eval(data)).encode('ascii'))
    except :
        message_queues[s].put(str("Invalid Arithmetic expression").encode('ascii'))

    if s not in outputs:
         outputs.append(s)


def close_connection(s,inputs,outputs,message_queues) :
    if s in outputs:
        outputs.remove(s)
    inputs.remove(s)
    s.close()
    del message_queues[s]

def send_to_client(s,inputs,outputs,message_queues) :
    try:
        next_msg = message_queues[s].get_nowait()
    except queue.Empty:
        outputs.remove(s)
    else:
        s.send(next_msg)

def exception_handling(s,inputs,outputs,message_queues) :
    inputs.remove(s)
    if s in outputs:
        outputs.remove(s)
    s.close()
    del message_queues[s]



def using_select_method(server) :

    inputs = [server]
    outputs = []
    message_queues = {}

    while inputs:
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs)
        # print(readable)
        for s in readable:
            if s is server:
                Connection(s,inputs,outputs,message_queues) ; 
            else:
                data = s.recv(1024)
                if data:
                    add_data(s,data,inputs,outputs,message_queues)     
                else:
                    close_connection(s,inputs,outputs,message_queues) 

        for s in writable:
            send_to_client(s,inputs,outputs,message_queues) 

        for s in exceptional:
            exception_handling(s,inputs,outputs,message_queues) ; 

def Main():       
    host = ""
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    print("socket binded to port", port)
    server.listen(5)
    using_select_method(server)


if __name__ == '__main__':
	Main()
