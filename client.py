import socket
import time

# GLOBAL CONSTANTS
SERVER = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5500
SERVER_ADDR = (SERVER, SERVER_PORT)
# PROTOCOL INFO
HEADER = 64
ENCODING = "utf8"
END_OF_SESSION_INDICATOR = "quit()"
# GLOBAL VARIABLES
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ADDR)


def send(msg):
    msg_length = str(len(msg))
    client.send(msg_length.encode(ENCODING))
    time.sleep(0.2)
    client.send(msg.encode(ENCODING))


def receive():
    pass


if __name__ == "__main__":
    print(f"Enter {END_OF_SESSION_INDICATOR} to leave")
    while True:
        msg = input("Enter message: ")
        send(msg)
        if msg == END_OF_SESSION_INDICATOR:
            client.close()
            break
