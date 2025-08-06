from .init import conn, curs
from webservice.src.model.explorer import Explorer

curs.execute("""create table if not exists explorer(
                name text primary key, 
                country text, 
                description text)""")

def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], country=row[1], description=row[2])

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump() if explorer else None

def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(explorer: Explorer) -> Explorer:
    qry = """insert into explorer values 
            (:name, :country, :description)"""
    params = model_to_dict(explorer)
    _ = curs.execute(qry, params)
    return get_one(explorer.name)

def modify(name: str, explorer: Explorer) -> Explorer:
    qry = """update explorer
                set country = :country,
                    name = :name,
                    description = :description
            where name = :name_orig"""

    params = model_to_dict(explorer)
    params["name_orig"] = name
    _ = curs.execute(qry, params)
    explorer2 = get_one(explorer.name)
    return explorer2

def replace(name: str, explorer: Explorer) -> Explorer:
    return explorer

def delete(name: str):
    qry = "delete from explorer where name = :name"
    params = {"name": name}
    res = curs.execute(qry, params)
    return bool(res)
