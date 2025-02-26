from pydantic import BaseModel
from typing import List


class ModsRequest(BaseModel):
    mods_list: list[str]

class ModsListUpdate(BaseModel):
    update_required: bool
    mods_list: List[str]
