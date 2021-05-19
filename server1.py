# import socket programming library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

# thread function
def evaluation(c):
	while True:

		# data received from client
		data = c.recv(1024)
		if not data:
			print('End ...............')
			print_lock.release()
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


def Main():
	host = ""
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to port", port)

	s.listen(5)

	while True:
		if(print_lock.locked()) :
			s = "Server already busy !!!" 
				
		else :
			c, addr = s.accept()
			print_lock.acquire()
			print('Connected to :', addr[0], ':', addr[1])
			start_new_thread(evaluation, (c,))
				


	s.close()


if __name__ == '__main__':
	Main()
