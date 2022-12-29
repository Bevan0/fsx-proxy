import socket
import threading
import settings

print("\nFSX Proxy v1.0\nCreated by Bevan\n")

client_link = settings.FSX_LINK  # this is the port FSX uses
server_link = settings.SERVER_LINK  # the IP and port you'll connect to/through

BUFFER_SIZE = settings.BUFFER_SIZE
PRINT_PACKETS = settings.PRINT_PACKETS

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.connect(server_link)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(client_link)

def to_server(): # to game server
    while True:
        packet = client.recvfrom(BUFFER_SIZE)
        server.sendto(packet, server_link)
        if PRINT_PACKETS: print(f"C>S {packet}")
        if packet == '': break
    print("server closed the connection")

def to_client(): # to game client
    while True:
        packet = server.recvfrom(BUFFER_SIZE)
        client.sendto(packet, client_link)
        if PRINT_PACKETS: print(f"S>C {packet}")
        if packet == '': break
    print("client closed the connection")

threading.Thread(target=to_server, daemon=True).start()
threading.Thread(target=to_client, daemon=True).start()

print("Proxy is now active!")

while True: pass