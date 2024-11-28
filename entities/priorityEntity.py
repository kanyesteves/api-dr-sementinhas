from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class PriorityBase(DeclarativeBase):
    pass

class PriorityEntity(PriorityBase):
    __tablename__ = 'priorities'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    level:          Mapped[int]  = mapped_column(Integer)
    description:    Mapped[str]  = mapped_column(String(128))


    def __repr__(self):
        return f"PriorityModel({self.id=}, {self.description=})"