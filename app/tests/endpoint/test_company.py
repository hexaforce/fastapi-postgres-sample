import json
from logging import getLogger

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from db import crud
from config import settings
from utils.test_utils import random_lower_string
from utils.test_utils import headers_token

logger = getLogger("company")
ENDPOINT = f'http://api/v1/company'

# -------------------------------------------------------------
# --- check ---------------------------------------------------
# -------------------------------------------------------------
def check(db: Session, id: str, expected: dict[str, str]):
    actual = crud.company.get(db=db, id=id)
    assert actual
    assert actual.sf_account_id == expected.get("sf_account_id")

# -------------------------------------------------------------
# --- TEST ----------------------------------------------------
# -------------------------------------------------------------
def test_company(client: TestClient, db: Session) -> None:
    # CREATE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    data = {
        "sf_account_id": random_lower_string(),
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
        "sf_account_id": random_lower_string(),
    }
    r = client.put(f"{ENDPOINT}/{id}", headers=headers_token(), json=data)
    assert 200 <= r.status_code < 300
    check(db, id, data)

    # DELETE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    r = client.delete(f'{ENDPOINT}/{id}', headers=headers_token())
    assert 200 <= r.status_code < 300
    new_data = crud.company.get(db=db, id=id)
    assert not new_data
