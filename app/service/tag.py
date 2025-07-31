from datetime import datetime

from app.model.tag import Tag

def create(tag: Tag) -> Tag:
    """태그를 생성한다"""
    return tag

def get(tag_str: str) -> Tag:
    return Tag(tag=tag_str, created=datetime.now(), secret="")

