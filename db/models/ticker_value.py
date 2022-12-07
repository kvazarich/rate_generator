from sqlalchemy import BigInteger, Column, DateTime, func, ForeignKey

from db.models.base import Base


class TickerValue(Base):
    id = Column(BigInteger, primary_key=True)
    ticker_id = Column(BigInteger, ForeignKey("ticker.id"))
    value = Column(BigInteger, nullable=False)
    time = Column(DateTime, default=func.now(), index=True)