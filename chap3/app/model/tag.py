from datetime import datetime
from pydantic import BaseModel

# 사용자가 제공해야하는 정보를 정의
class TagIn(BaseModel):
    tag: str

# TagIn에 created(tag 생성시점)와 secret(데이터베이스에 저장될 수 있지만 외부에 노출되지 않도록 설정)
# 이라는 두개의 필드가 추가된 클래스
class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str

# 사용자에게 반환할 수 있는 항목을 정의
# 기존 TagIn과 Tag 객체가 지닌 tag 속성과 created 속성을 가짐
class TagOut(BaseModel):
    tag: str
    created: datetime