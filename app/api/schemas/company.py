from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class CompanyBase(BaseModel):
    pass

# -------------------------------------------------------------
# --- read ----------------------------------------------------
# -------------------------------------------------------------

# Properties shared by models stored in DB
class CompanyInDBBase(CompanyBase):
    id: str
    sf_account_id: Optional[str]
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True

# Properties to return to client
class Company(CompanyInDBBase):
    pass

# Properties properties stored in DB
class CompanyInDB(CompanyInDBBase):
    pass

# -------------------------------------------------------------
# --- creation ------------------------------------------------
# -------------------------------------------------------------

  # Properties to receive on Company creation
class CompanyCreate(CompanyBase):
    sf_account_id: str

# -------------------------------------------------------------
# --- update --------------------------------------------------
# -------------------------------------------------------------

  # Properties to receive on Company update
class CompanyUpdate(CompanyBase):
    sf_account_id: Optional[str]
