from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import os
from models import schemes

router = APIRouter(
    prefix='/ws',
    tags=["Websocket"],
    dependencies=[]
)

clients = set()


@router.websocket("/connect")
async def wsconection_endpoint(websocket: WebSocket):
	await websocket.accept()
	clients.add(websocket)
	print(f"Cliente conectado: {websocket.client}")

	try:
		while True:
			await websocket.receive_text()
	except WebSocketDisconnect:
			clients.remove(websocket)
			print(f"Cliente desconectado: {websocket.client}")



@router.post("/update-mods", response_model=schemes.FTPConnection)
async def trigger_sync():
    if not clients:
        return schemes.FTPConnection(
            update_required=False,
            server="",
            user="",
            password="",
            mods_list=[]
        )

    # Obtener lista de mods en el servidor
    server_mods = set(os.listdir(os.getenv("MODS_FOLDER", "")))

    # Crear mensaje de actualización basado en el modelo
    update_message = schemes.FTPConnection(
        update_required=True,
        server=os.getenv("FTP_SERVER", ""),
        user=os.getenv("FTP_USER", ""),
        password=os.getenv("FTP_PASS", ""),
        mods_list=list(server_mods)
    )

    # Notificar a cada cliente WebSocket
    for ws in clients.copy():
        try:
            await ws.send_text(update_message)
        except Exception:
            clients.remove(ws)

    return update_message 