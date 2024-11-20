import asyncio
import websockets

connected_clients = set()

async def handle_connection(websocket, path):
    """
    Handles WebSocket connections and messages.
    """
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            # Broadcast message to all connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(handle_connection, "0.0.0.0", 6789)

if __name__ == "__main__":
    print("WebSocket server is running on ws://0.0.0.0:6789")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
