import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode("utf-8")
            if msg:
                print(f"\n{msg}")
        except:
            print("Connection closed.")
            break

def start_client():
    host = "127.0.0.1"   # Server IP (change if needed)
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("Connected to chat server. Type 'exit' to quit.")

    # Thread for receiving messages
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    # Main loop for sending messages
    while True:
        msg = input()
        client.send(msg.encode("utf-8"))
        if msg.lower() == "exit":
            client.close()
            break

if __name__ == "__main__":
    start_client()
