from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from .mixins import IdIntPkMixin
from .base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        yield SQLAlchemyUserDatabase(session, cls)