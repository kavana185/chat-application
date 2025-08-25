import socket
import threading

# Store connected clients
clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
            if not msg or msg.lower() == "exit":
                break
            print(f"{addr}: {msg}")
            broadcast(msg, conn)
        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"[DISCONNECTED] {addr} left.")

def broadcast(msg, sender_conn):
    for client in clients:
        if client != sender_conn:
            client.send(msg.encode("utf-8"))

def start_server():
    host = "127.0.0.1"   # Localhost
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"[STARTED] Server running on {host}:{port}")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
