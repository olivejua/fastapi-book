from datetime import datetime

import app.service.tag as service
from fastapi import FastAPI

from app.model.tag import TagIn, Tag, TagOut

app = FastAPI()

@app.post('/')
def create(tag_in: TagIn):
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.now(), secret="shhhh")
    service.create(tag)
    return tag_in

@app.get('/{tag_str}', response_model=TagOut)
def get_one(tag_str: str):
     tag: Tag = service.get(tag_str)
     return tag
