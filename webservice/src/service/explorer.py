from webservice.src.model.explorer import Explorer
from webservice.src.data import explorer as data

def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(explore: Explorer) -> Explorer:
    return data.create(explore)

def replace(name: str, explorer: Explorer) -> Explorer:
    return data.replace(name, explorer)

def modify(name: str, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)

def delete(name: str) -> bool:
    return data.delete(name)
