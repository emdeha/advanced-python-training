import asyncio

async def handle_client(reader, writer):
  while True:
    request = await reader.read(1024)
    if not request: break
    writer.write(request)
    await writer.drain()
  writer.close()

async def run_server():
  server = await asyncio.start_server(handle_client, 'localhost', 1337)
  async with server:
    await server.serve_forever()

asyncio.run(run_server())
