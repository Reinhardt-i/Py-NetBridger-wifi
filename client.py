import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("Connection lost.")
            break
            raise  # lol


def send_messages(client_socket, username):
    while True:
        message = input()
        full_message = f"{username}: {message}"
        client_socket.send(full_message.encode('utf-8'))


if __name__ == '__main__':
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('server_ip_address', 12345))  # Replace with the server's IP address

    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client, username))

    receive_thread.start()
    send_thread.start()
