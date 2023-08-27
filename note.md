### Server-side Code (server.py) :
- This code sets up a server that listens for incoming connections from clients.
When a client connects, it receives a username from the client and checks if the username is already in use.
- If the username is not in use, the server adds the client to its list of clients and starts handling messages from and to the client.
- The server uses threads to handle communication with each connected client concurrently. it listens for messages from clients and broadcasts those messages to all connected clients except the sender.

### Client-side Code (client.py) :
- This code connects to the server using the server's IP address and port.
- The client provides a username and sends it to the server.
- The code sets up two threads: one for receiving messages from the server and another for sending messages to the server.
- The client can input messages to send to the server, and it will receive messages from other connected clients.
- To run a client, execute the client.py script. You can run multiple instances of this script to simulate multiple clients connecting to the server.


#### Simulation Script (simulation.py) :
- This script simulates the interaction between a server and two clients.
- It uses the subprocess module to run the server and multiple client scripts in separate processes.
- The simulation runs for a certain duration and then terminates the server and client processes.
- To run the simulation, execute the simulation.py script. This script will start a server and two client instances that communicate with each other.

