from fastapi import APIRouter
import os, json
from ..models import schemes

router = APIRouter(
    prefix='/check',
    tags=["Check"],
    dependencies=[]
)


@router.post("/mods", response_model=schemes.FTPConnection)
async def check_mods(request: schemes.ModsRequest):
    server_mods = set(os.listdir(os.getenv("MODS_FOLDER")))
    client_mods = set(request.mods_list)

    update_required = server_mods != client_mods

    update_message = schemes.FTPConnection(
        update_required=update_required,
        server=os.getenv("FTP_SERVER"),
        user=os.getenv("FTP_USER"),
        password=os.getenv("FTP_PASS"),
        mods_list=list(server_mods)
    )
    
    return update_message