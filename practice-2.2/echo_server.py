import socket

from http_parser.http import HttpStream, NoMoreData
from http_parser.reader import SocketReader

def handle_connection(conn):
  with conn:
    r = SocketReader(conn)
    p = HttpStream(r)
    conn.sendall(p.body_string())

def start_listening():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 1337))
    s.listen()
    while True:
      conn, addr = s.accept()
      handle_connection(conn)

if __name__ == "__main__":
  start_listening()