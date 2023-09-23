import socket
import threading
from typing import Tuple

def receive_messages(client_socket: socket.socket):
    """
        Receive and display messages from the server.

    Args:
        client_socket (socket.socket): The client's socket connected to the server.
    """
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
    except:
        print("Connection lost.")
        raise


def send_messages(client_socket: socket.socket, username: str):
    """
        Send messages to the server.

    Args:
        client_socket (socket.socket): The client's socket connected to the server.
        username (str): The username of the client.
    """
    try:
        while True:
            message = input()
            if message.lower() == "exit":
                break
            full_message = f"{username}: {message}"
            client_socket.send(full_message.encode('utf-8'))
    except:
        print("An error occurred while sending messages.")
        raise


if __name__ == '__main__':

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 12345)
    client.connect(server_address)

    username = input("Enter your username : ")
    client.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client, username))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client.close()
