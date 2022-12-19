from typing import Any
from typing import Optional
from typing import TypeVar

from sqlalchemy.orm import Session

from db.base_crud import CRUDBase
from db.base_class import Base
from db import model
from api import schemas

ModelType = TypeVar("ModelType", bound=Base)


class CRUDCompany(CRUDBase[model.Company, schemas.CompanyCreate, schemas.CompanyUpdate]):
  
    def find_by_sf_account_id(
        self, db: Session, sf_account_id: Any
    ) -> Optional[ModelType]:
        return (
            db.query(self.model)
            .filter(self.model.sf_account_id == sf_account_id)
            .first()
        )

company = CRUDCompany(model.Company)
