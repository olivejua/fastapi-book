from fastapi import APIRouter
import webservice.src.service.explorer as service
from webservice.src.model.explorer import Explorer

router = APIRouter(prefix="/explorer")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)

@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

@router.patch("/{name}")
def modify(name, explorer: Explorer) -> Explorer:
    return service.modify(name, explorer)

@router.put("/{name}")
def replace(name, explorer: Explorer) -> Explorer:
    return service.replace(name, explorer)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)
