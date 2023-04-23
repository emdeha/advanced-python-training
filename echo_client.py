import socket
import sys

def construct_http_request(msg):
  return (
    "POST / HTTP/1.1\r\n"
    "Host: localhost:1337\r\n"
    "User-Agent: curl/7.87.0\r\n"
    "Accept: */*\r\n"
    f"Content-Length: {len(msg)}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
    f"{msg}\r\n"
  )

def send_msg(msg):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 1337))
    s.sendall(str.encode(construct_http_request(msg)))
    data = s.recv(1024)

  print('Received', repr(data))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: ./echo_client.py <message>")
    exit(1)

  send_msg(sys.argv[1])