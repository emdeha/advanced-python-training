import socket
import sys

def send_msg(msg):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 1337))
    s.sendall(str.encode(msg))
    data = s.recv(1024)

  print('Received', repr(data))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: ./echo_client.py <message>")
    exit(1)

  send_msg(sys.argv[1])