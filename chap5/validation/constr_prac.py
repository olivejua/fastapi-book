from pydantic import BaseModel, constr

# constr : 제약된 문자열
class Creature(BaseModel):
    name: constr(min_length=2)
    country: str
    area: str
    description: str
    aka: str

bad_creature = Creature(name="!", description="it's a raccoon", area="your attic")

