import asyncio
import websockets
import ssl
import json

connected = set()

async def handler(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)
            for conn in connected:
                if conn != websocket:
                    await conn.send(json.dumps(data))
    finally:
        connected.remove(websocket)

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    async with websockets.serve(handler, "0.0.0.0", 9000, ssl=ssl_context):
        print("WebSocket signaling server running on wss://0.0.0.0:9000")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
