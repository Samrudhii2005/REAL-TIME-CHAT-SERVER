import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict

app = FastAPI()

rooms: Dict[str, List[WebSocket]] = {}

@app.websocket("/ws/{room_name}")
async def websocket_endpoint(websocket: WebSocket, room_name: str):
    await websocket.accept()
    if room_name not in rooms:
        rooms[room_name] = []
    rooms[room_name].append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for connection in rooms[room_name]:
                if connection != websocket:
                    await connection.send_text(f"{room_name}: {data}")
    except WebSocketDisconnect:
        rooms[room_name].remove(websocket)
        if not rooms[room_name]:
            del rooms[room_name]

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)