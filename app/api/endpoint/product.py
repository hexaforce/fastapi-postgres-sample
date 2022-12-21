from typing import Any
from typing import List
from uuid import UUID

from api import deps
from api import schemas
from db import crud
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/product", tags=["Product"])

# -------------------------------------------------------------
# --- CREATE --------------------------------------------------
# -------------------------------------------------------------
@router.post("", response_model=schemas.Product)
def create_product(
    *,
    ok: bool = Depends(deps.allow_admin_only),
    db: Session = Depends(deps.get_db_session),
    obj_in: schemas.ProductCreate,
) -> Any:
    return crud.product.create(db=db, obj_in=obj_in)


# -------------------------------------------------------------
# --- READ ----------------------------------------------------
# -------------------------------------------------------------
@router.get("/{id}", response_model=schemas.Product)
def read_product(
    *,
    ok: bool = Depends(deps.allow_admin_only),
    db: Session = Depends(deps.get_db_session),
    id: str,
) -> Any:
    UUID(id)
    return getById(db=db, id=id)


# -------------------------------------------------------------
# --- READ(all) -----------------------------------------------
# -------------------------------------------------------------
@router.get("", response_model=List[schemas.Product])
def read_products(
    *,
    ok: bool = Depends(deps.allow_admin_only),
    db: Session = Depends(deps.get_db_session),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.product.get_multi(db, skip=skip, limit=limit)


# -------------------------------------------------------------
# --- UPDATE --------------------------------------------------
# -------------------------------------------------------------
@router.put("/{id}", response_model=schemas.Product)
def update_product(
    *,
    ok: bool = Depends(deps.allow_admin_only),
    db: Session = Depends(deps.get_db_session),
    id: str,
    obj_in: schemas.ProductUpdate,
    # csrf: bool = Depends(deps.validate_csrf_token),
) -> Any:
    UUID(id)
    obj = getById(db=db, id=id)
    return crud.product.update(db=db, db_obj=obj, obj_in=obj_in)


# -------------------------------------------------------------
# --- DELETE --------------------------------------------------
# -------------------------------------------------------------
@router.delete("/{id}", response_model=schemas.Product)
def delete_product(
    *,
    ok: bool = Depends(deps.allow_admin_only),
    db: Session = Depends(deps.get_db_session),
    id: str,
    # csrf: bool = Depends(deps.validate_csrf_token),
) -> Any:
    UUID(id)
    obj = getById(db=db, id=id)
    return crud.product.remove(db=db, id=id)


def getById(db: Session, id: str):
    obj = crud.product.get(db=db, id=id)
    if not obj:
        raise HTTPException(status_code=204, detail="product not found")
    return obj
