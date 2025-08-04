from fastapi import APIRouter
import webservice.src.fake.creature as service
from webservice.src.model.creature import Creature

router = APIRouter(prefix="/creature")

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature | None:
    return service.get_one(name)

@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/{name}")
def modify(name, creature: Creature) -> Creature:
    return service.modify(name, creature)

@router.put("/{name}")
def replace(name, creature: Creature) -> Creature:
    return service.replace(name, creature)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)
