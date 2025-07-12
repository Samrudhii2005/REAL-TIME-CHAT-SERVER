import asyncio
import websockets

async def listen_messages(websocket):
    try:
        async for message in websocket:
            print("\nServer:", message)
    except websockets.ConnectionClosed:
        print("Connection closed by server.")

async def send_messages(websocket):
    while True:
        message = await asyncio.get_event_loop().run_in_executor(None, input, "You: ")
        await websocket.send(message)

async def main():
    uri = "ws://127.0.0.1:8000/ws/general"
    async with websockets.connect(uri) as websocket:
        print("Connected to server!")
        # Start listening and sending concurrently
        await asyncio.gather(
            listen_messages(websocket),
            send_messages(websocket),
        )

if __name__ == "__main__":
    asyncio.run(main())