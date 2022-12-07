from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base


class BaseClass:
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


Base = declarative_base(cls=BaseClass)
