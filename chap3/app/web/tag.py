from datetime import datetime

import chap3.app.service.tag as service
from fastapi import FastAPI

from chap3.app.model.tag import TagIn, Tag, TagOut

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
