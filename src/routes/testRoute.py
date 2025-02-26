from fastapi import APIRouter

router = APIRouter(
    prefix='/test',
    tags=["Test"],
    dependencies=[]
)

@router.get("/")
async def healtcheck():
    return 'Funcionando!'
