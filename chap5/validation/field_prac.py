from pydantic import BaseModel, Field

class Creature(BaseModel):
    name: str = Field(..., min_length=2) # ... 값이 필요하며, 기본값이 없음을 의미
    country: str
    area: str
    description: str
    aka: str

bad_creature = Creature(name="!", description="it's a raccoon", area="your attic")
