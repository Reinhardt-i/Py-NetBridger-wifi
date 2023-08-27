import socket


def send_message():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('server_ip_address', 12345))  # Replace with the actual IP address of the server

    while True:
        message = input("Enter a message: ")
        client.send(message.encode('utf-8'))


if __name__ == '__main__':
    send_message()
