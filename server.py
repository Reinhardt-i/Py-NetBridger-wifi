import socket
import threading


clients = {}


def handle_client(client_socket, client_address):
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    print(f"{username} connected from {client_address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received from {username}: {message}")

        for client, user in clients.items():
            if client != client_socket:
                try:
                    client.send(f"{username}: {message}".encode('utf-8'))
                except:
                    clients.pop(client)
                    print(f"Client {user} disconnected.")
                    client.close()
                    raise

    clients.pop(client_socket)
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)

    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == '__main__':
    start_server()
