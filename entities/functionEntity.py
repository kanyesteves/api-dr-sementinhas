from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class FunctionBase(DeclarativeBase):
    pass

class FunctionEntity(FunctionBase):
    __tablename__ = 'functions'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    description:    Mapped[str]  = mapped_column(String(128))


    def __repr__(self):
        return f"FunctionModel({self.id=}, {self.name=})"