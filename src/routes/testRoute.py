from fastapi import APIRouter

router = APIRouter(
    prefix='/test',
    tags=["Test"],
    dependencies=[]
)

@router.get("/test")
async def healtcheck():
    return 'Funcionando!'
