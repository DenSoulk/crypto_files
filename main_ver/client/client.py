import requests
import asyncio
client_id=input()

async def ping_server(client_id):

    print("ping")
    r = requests.get(f'http://127.0.0.1:5000/ping/'+client_id)
    await asyncio.sleep(2.5)


async def message_server(client_id):
    message="mes"
    r = requests.get('http://127.0.0.1:5000/message/'+client_id+"+"+message)
    print(r.json())

async def main(client_id):

    ping_server_t = asyncio.create_task(ping_server(client_id))
    await ping_server_t
    message_server_t = asyncio.create_task(message_server(client_id))





while True:
    asyncio.run(main(client_id))