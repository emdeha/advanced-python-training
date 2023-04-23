import socket
import sys
from http_parser.http import HttpStream
from http_parser.reader import SocketReader

def construct_http_request(msg, apiKey):
  return (
    "POST / HTTP/1.1\r\n"
    "Host: localhost:1337\r\n"
    "User-Agent: curl/7.87.0\r\n"
    "Accept: */*\r\n"
    f"X-APIKey: {apiKey}\r\n"
    f"Content-Length: {len(msg)}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
    f"{msg}\r\n"
  )

def send_msg(msg, apiKey):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 1337))
    s.sendall(str.encode(construct_http_request(msg, apiKey)))
    r = SocketReader(s)
    p = HttpStream(r)
    if p.status_code() == 401:
      print('Unauthorized')
      return

    data = p.body_string()

  print('Received', repr(data))

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: ./echo_client.py <message> <apiKey>")
    exit(1)

  send_msg(sys.argv[1], sys.argv[2])