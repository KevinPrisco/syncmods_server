from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
import os
from fastapi.responses import FileResponse
from ..models import schemes

router = APIRouter(
    prefix='/ws',
    tags=["Websocket"],
    dependencies=[]
)

clients = set()
old_mods = set()

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


@router.post("/update-mods", response_model=schemes.ModsListUpdate)
async def trigger_sync():
    global old_mods
    print(f"Clientes conectados: {len(clients)}")
    if not clients:
        print('no clientes')
        return schemes.ModsListUpdate(update_required=False, mods_list=[])

    mods_folder = os.getenv("MODS_FOLDER", "./mods")
    server_mods = set(os.listdir(mods_folder))

    if not old_mods:
        last_known_mods = server_mods

    update_required = need_update(old_mods, server_mods)

    update_message = schemes.ModsListUpdate(
        update_required=update_required,
        mods_list=list(server_mods)
    )

    # Notificar a cada cliente WebSocket
    for ws in clients.copy():
        try:
            assert isinstance(ws, WebSocket)
            await ws.send_text(update_message.model_dump_json())
        except Exception:
            clients.remove(ws)

    return update_message 

@router.get("/mods/{filename}")
async def download_mod(filename: str):
    mods_folder = os.getenv("MODS_FOLDER", "./mods")
    file_path = os.path.join(mods_folder, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

    return FileResponse(file_path, filename=filename)



def need_update(old, new):
    return old != new