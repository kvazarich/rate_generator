from sqlalchemy import BigInteger, Column, String

from db.models.base import Base


class Ticker(Base):
    id = Column(BigInteger, primary_key=True)
    code = Column(String, nullable=False, index=True)
