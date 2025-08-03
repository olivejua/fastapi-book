from typing import Tuple, List, Dict, Union
from collections import namedtuple

tuple_things: Tuple = {"yeti", "bigfoot"}
list_things: List = ["yeti", "bigfoot"]
dict_things: Dict = {"mountain": "yeti", "forest": "bigfoot"}


physics_magic_number: float = 1.0/137.03599913
hp_lovecraft_noun: str = "ichor"
exploding_sheep: tuple = "sis", "boom", "bah!"
responses: dict = {"Marco": "Polo", "answer": 42}

# name: dict[keytype, valtype] = {key1: val1, key2: val2}


responses: dict[str, Union[str, int]] = {"Marco": "Polo", "answer": 42}
responses: dict[str, str|int] = {"Marco": "Polo", "answer": 42}

CreatureNamedTuple = namedtuple("CreatureNamedTuple", "name, country, area, description, aka")
namedtuple_thing = CreatureNamedTuple("yeti", "CN", "Himalaya", "Hirsute HImalayan", "Abominable Snowman")
print("Name is", namedtuple_thing[0])
print("Name is", namedtuple_thing.name)