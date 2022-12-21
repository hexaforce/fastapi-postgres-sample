from typing import Generator

import jwt
from db.session import session_main
from db.session import session_test
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi import Security
from fastapi import status
from fastapi.security.api_key import APIKeyHeader

from .idtoken import IdToken

# from fastapi_csrf_protect import CsrfProtect
# from fastapi_csrf_protect.exceptions import InvalidHeaderError
# from fastapi_csrf_protect.exceptions import TokenValidationError



auth_token = APIKeyHeader(name="authorization", auto_error=False)

def get_db_session(request: Request) -> Generator:
    db_mode = request.headers.get("test")
    try:
        if db_mode is None:
            db = session_main()
        else:
            db = session_test()
        yield db
    finally:
        db.close()


def get_current_user_token(
    auth_token: str = Security(auth_token),
) -> IdToken:
    try:
        payload = jwt.decode(auth_token, options={"verify_signature": False})
        token = IdToken.parse_obj(payload)
        token.authorization = auth_token
        token.admin = False
        if "cognito:groups" in payload:
            token.group = payload["cognito:groups"]
            token.admin = "admin" in token.group
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="HeaderのTokenが不正です。",
        )
    return token


def allow_admin_only(
    idToken: IdToken = Depends(get_current_user_token),
) -> bool:
    if not idToken.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="このAPIは管理者のみ呼び出しが可能です。",
        )
    return True


# def validate_csrf_token(
#     request: Request, csrf_protect: CsrfProtect = Depends()
# ) -> bool:
#     try:
#         csrf_token = csrf_protect.get_csrf_from_headers(request.headers)
#         csrf_protect.validate_csrf(csrf_token)
#         return True
#     except TokenValidationError:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="CSRFトークンが無効になっています",
#         )
#     except InvalidHeaderError:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="CSRF周りの問題が発生しました"
#         )
