import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
import client_messaging  

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Room")

        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=20, pady=10)

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(padx=20, pady=10)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

        self.client_socket = client_messaging.client_socket
        self.alias = None

        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect(('::1', 59000))
            self.alias = simpledialog.askstring("Alias", "Choose an alias:")
            if self.alias:
                self.client_socket.send(self.alias.encode('utf-8'))
                threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))
            self.root.quit()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, message + '\n')
                self.chat_area.config(state='disabled')
                self.chat_area.yview(tk.END)
            except:
                messagebox.showerror("Error", "Failed to receive message")
                self.client_socket.close()
                break

    def send_message(self, event=None):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        client_messaging.send_message(self.alias, message)

    def on_closing(self):
        self.client_socket.close()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.protocol("WM_DELETE_WINDOW", client.on_closing)
    root.mainloop()
