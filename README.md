# Client-Server-Socket-Programming
This repository contains code for 4 types of client - server systems . Client will ask the server to calculate some expression and server will return answer



This assignment was part of my Computer Networks assignment .

1) Server1.py - It will be a single process server that can handle only one client at a time. If a second client tries to chat with the server while some other client's session is already in progress, the second client's socket operations should see an error. After the first client closes the connection, the server should then accept connections from the other client

2) Server2.py - It will be a multi-threaded server that will create a new thread for every new client request it receives. Multiple clients should be able to simultaneously chat with the server.

3) Server3.py - It will be a single process server that uses the "select" method to handle multiple clients concurrently

4) Server.py - It will be an echo server (that replies the same message to the client that was received from the same client); it will be a single process server that uses the "select" method to handle multiple clients concurrently.
