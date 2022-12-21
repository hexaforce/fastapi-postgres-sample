from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    pass

# -------------------------------------------------------------
# --- read ----------------------------------------------------
# -------------------------------------------------------------

# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: str
    company_id: str
    product_name: str
    hearing_complete: bool
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True

# Properties to return to client
class Product(ProductInDBBase):
    pass

# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass

# -------------------------------------------------------------
# --- creation ------------------------------------------------
# -------------------------------------------------------------

# Properties to receive on Product creation
class ProductCreate(ProductBase):
    company_id: str
    product_name: str
    hearing_complete: Optional[bool]

# -------------------------------------------------------------
# --- update --------------------------------------------------
# -------------------------------------------------------------

# Properties to receive on Product update
class ProductUpdate(ProductBase):
    company_id: Optional[str]
    product_name: Optional[str]
    hearing_complete: Optional[bool]
