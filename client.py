# Import socket module
import socket

def connection(s):
    is_connected = True
    while is_connected :
        try :
            message = input("Enter your expression")

            s.send(message.encode('ascii'))  

            data = s.recv(1024)
            print('Received from the server :',str(data.decode('ascii'))) 
        except KeyboardInterrupt: 

            print("Closing ......\n") 
            s[i].close()
            is_connected = False ; 




def Main():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try :
        s.connect((host,port)) 
        connection(s) ; 
    except :
        print("Connection Closed/Refused")
    

if __name__ == '__main__':
	Main()
