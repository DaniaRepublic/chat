import socket
import threading

# GLOBAL CONSTANTS
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5500
ADDR = (SERVER, PORT)
# PROTOCOL INFO
HEADER = 64
ENCODING = "utf8"
END_OF_SESSION_INDICATOR = "quit()"
# GLOBAL VARIABLES
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def serve_client(conn, addr):
    run = True
    while run:
        msg_length = conn.recv(HEADER).decode(ENCODING)
        if msg_length:
            try:
                msg_length = int(msg_length)
            except Exception as e:
                print("[EXCEPTION] ", e)
                run = False
                continue
            msg = conn.recv(msg_length).decode(ENCODING)
            if msg == END_OF_SESSION_INDICATOR:
                run = False
                continue

            print(f"message from {addr} : ", msg)
    
    conn.close()
    print(f"[DISCONNECT] client {addr} disconnected")


def accept_connections():
    server.listen()
    print("[STARTED] server started")
    while True:
        print("[CONNECTION] waiting for connection")
        conn, addr = server.accept()
        thread = threading.Thread(target=serve_client, args=(conn, addr))
        thread.start()
        print(f"[CONNECTION] accepted connection from {addr}")
    
    server.close()
    print("[STOPPED] server stopped")


print(f"[START] starting the server on {SERVER}")
accept_connections()