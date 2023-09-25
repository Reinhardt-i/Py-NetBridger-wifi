import tkinter as tk
import socket
import threading


class ClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Py-NetBridger.")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.connect_button = tk.Button(root, text="Connect", command=self.connect_to_server)
        self.connect_button.pack()

        self.chat_text = tk.Text(root, state='disabled')
        self.chat_text.pack()

        self.message_entry = tk.Entry(root)
        self.message_entry.pack()

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.client_socket = None
        self.username = None

    def connect_to_server(self):

        if self.client_socket:
            return
        
        self.username = self.username_entry.get()
        server_address = ('0.0.0.0', 12345)  # Replace with the server's IP address
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(server_address)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.send_thread = threading.Thread(target=self.send_messages)

        self.receive_thread.start()
        self.send_thread.start()


    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.chat_text.config(state='normal')
                    self.chat_text.insert(tk.END, message + '\n')
                    self.chat_text.config(state='disabled')
            except SystemExit:
                raise SystemExit

    def send_message(self):
        message = self.message_entry.get()
        if message.lower() == "exit":
            self.client_socket.close()
            self.root.destroy()
        else:
            full_message = f"{self.username}: {message}"
            self.client_socket.send(full_message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    gui = ClientGUI(root)
    root.mainloop()
