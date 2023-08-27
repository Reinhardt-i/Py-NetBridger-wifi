
import socket
import threading


clients = {}
clients_lock = threading.Lock()


def handle_client(client_socket, client_address):
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
            print(f"Received from {username}: {message}")

            with clients_lock:
                for client, user in clients.items():
                    if client != client_socket:
                        try:
                            client.send(f"{username}: {message}".encode('utf-8'))
                        except:
                            print(f"Client {user} disconnected.")
                            client.close()
                            del clients[client]
                            break
                            raise
    finally:
        with clients_lock:
            if client_socket in clients:
                print(f"Client {clients[client_socket]} disconnected.")
                del clients[client_socket]
            client_socket.close()


def start_server():
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
