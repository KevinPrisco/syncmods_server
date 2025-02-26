from fastapi import APIRouter
import os
from ..models import schemes

router = APIRouter(
    prefix='/check',
    tags=["Check"],
    dependencies=[]
)


@router.post("/mods", response_model=schemes.ModsListUpdate)
async def check_mods(request: schemes.ModsRequest):
    server_mods = set(os.listdir(os.getenv("MODS_FOLDER")))
    client_mods = set(request.mods_list)

    update_required = server_mods != client_mods

    return schemes.ModsListUpdate(
        update_required=update_required,
        mods_list=list(server_mods)
    )
