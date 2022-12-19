from typing import List
from typing import Optional

from pydantic import BaseModel


class IdToken(BaseModel):
    iss: str
    sub: str
    aud: Optional[str]
    exp: int
    iat: int
    jti: str
    email: Optional[str]
    group: Optional[List[str]]
    admin: Optional[bool]
    authorization: Optional[str]
