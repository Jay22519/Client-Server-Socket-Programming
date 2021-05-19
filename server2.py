# import socket programming library
import socket

# import thread module
from _thread import *
import threading

thread_lock = list([threading.Lock() for i in range(1000)])


# thread function
def evaluation(c,i):
	while True:

		# data received from client
		data = c.recv(1024)
		if not data:
			print('End ................')
			
			thread_lock[i].release()
			# lock released on exit
			break

		try :
			data = str(eval(data)).encode('ascii')
		except :
			data = str("Invalid Arithmetic expression").encode('ascii')

		# send back reversed string to client
		c.send(data)

	# connection closed
	c.close()


i = -1 

def Main():
	host = ""
	
	# reverse a port on your computer
	# in our case it is 12345 but it
	# can be anything
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)

	# put the socket into listening mode
	s.listen(5)
	print("socket is listening")

	# a forever loop until client wants to exit
	while True:

		# establish connection with client
		c, addr = s.accept()

		# lock acquired by client
		global i 
		i+=1 
		thread_lock[i].acquire()
		print('Connected to :', addr[0], ':', addr[1])

		# Start a new thread and return its identifier
		start_new_thread(evaluation, (c,i,))

		
        
	s.close()


if __name__ == '__main__':
	Main()
