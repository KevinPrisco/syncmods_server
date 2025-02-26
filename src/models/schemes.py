from pydantic import BaseModel
from typing import List


class ModsRequest(BaseModel):
    mods_list: list[str]



class FTPConnection(BaseModel):
    update_required: bool
    server: str
    user: str
    password: str
    mods_list: List[str]