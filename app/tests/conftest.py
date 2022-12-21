from typing import Generator

import pytest
from db.session import session_main
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield session_main()

@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
