import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(('localhost', 1337))
  s.listen()
  while True:
    conn, addr = s.accept()
    with conn:
      while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)