import socket
import threading
import logging
from typing import Dict


clients: Dict[socket.socket, str] = {}
clients_lock = threading.Lock()

# Configuring logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def handle_client(client_socket: socket.socket, client_address: tuple):
    """
        Handle incoming messages from a client.

    Args:
        client_socket (socket.socket): The client's socket.
        client_address (tuple): The client's address (host, port).
    """
    try:
        username = client_socket.recv(1024).decode('utf-8')
        with clients_lock:
            if username in clients.values():
                client_socket.send("Username already in use. Please choose another.".encode('utf-8'))
                client_socket.close()
                return
            clients[client_socket] = username

        print(f"{username} connected from {client_address}")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            logging.info(f"Received from - !{username} : {message}")


            with clients_lock:
                for client, user in clients.items():
                    if client != client_socket:
                        try:
                            client.send(f" {message}".encode('utf-8'))
                        except:
                            print(f"Client {user} disconnected.")
                            client.close()
                            del clients[client]
                            break
                            raise
                        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        with clients_lock:
            if client_socket in clients:
                print(f"Client {clients[client_socket]} disconnected.")
                del clients[client_socket]
            client_socket.close()


def start_server():
    """
        Starts the server and listen for incoming client connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 12345)
    server.bind(server_address)
    server.listen(5)

    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == '__main__':
    start_server()
