import json
from logging import getLogger

from api import schemas
from db import crud
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from utils.test_utils import headers_token
from utils.test_utils import random_lower_string

logger = getLogger("product")
ENDPOINT = f'http://api/v1/product'

# -------------------------------------------------------------
# --- check ---------------------------------------------------
# -------------------------------------------------------------
def check(db: Session, id: str, expected: dict[str, str]):
    actual = crud.product.get(db=db, id=id)
    assert actual
    assert actual.company_id == expected.get("company_id")
    assert actual.product_name == expected.get("product_name")


# -------------------------------------------------------------
# --- TEST ----------------------------------------------------
# -------------------------------------------------------------
def test_product(client: TestClient, db: Session) -> None:

    company_id = crud.company.create(db=db, obj_in=schemas.CompanyCreate(
      sf_account_id=random_lower_string()
    )).id
    
    # CREATE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    data = {
        "company_id": company_id,
        "product_name": random_lower_string(),
    }
    r = client.post(ENDPOINT, headers=headers_token(), json=data)
    assert 200 <= r.status_code < 300
    id = r.json()["id"]
    check(db, id, data)

    # GET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    r = client.get(f"{ENDPOINT}/{id}", headers=headers_token())
    assert 200 <= r.status_code < 300
    check(db, id, json.loads(r.text))

    # UPDATE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    data = {
        "company_id": company_id,
        "product_name": random_lower_string(),
    }
    r = client.put(f"{ENDPOINT}/{id}", headers=headers_token(), json=data)
    assert 200 <= r.status_code < 300
    check(db, id, data)

    # DELETE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    r = client.delete(f'{ENDPOINT}/{id}', headers=headers_token())
    assert 200 <= r.status_code < 300
    new_data = crud.product.get(db=db, id=id)
    assert not new_data

    crud.company.remove(db=db, id=company_id)
