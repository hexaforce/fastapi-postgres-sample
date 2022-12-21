from typing import Any
from typing import List
from typing import Optional
from typing import TypeVar

from api import schemas
from db import model
from db.base_class import Base
from db.base_crud import CRUDBase
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)

class CRUDProduct(CRUDBase[model.Product, schemas.ProductCreate, schemas.ProductUpdate]):

    def find_by_company_id(self, db: Session, company_id: Any) -> List[ModelType]:
        return db.query(self.model).filter(self.model.company_id == company_id).all()

    def find_by_company_id_and_product_name(
        self, db: Session, company_id: Any, product_name: Any
    ) -> Optional[ModelType]:
        return (
            db.query(self.model)
            .filter(self.model.company_id == company_id)
            .filter(self.model.product_name == product_name)
            .first()
        )

product = CRUDProduct(model.Product)
