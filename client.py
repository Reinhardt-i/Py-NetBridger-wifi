import socket
import threading


def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
    except:
        print("Connection lost.")
        raise


def send_messages(client_socket, username):
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
    server_address = ('192.168.0.103', 12345)  # Replace with the server's IP address
    client.connect(server_address)

    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client, username))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client.close()
