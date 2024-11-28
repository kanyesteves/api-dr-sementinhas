from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class EventBase(DeclarativeBase):
    pass

class EventEntity(EventBase):
    __tablename__ = 'events'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    date:           Mapped[str]  = mapped_column(Date)
    hour_start:     Mapped[str]  = mapped_column(String(50))
    hour_end:       Mapped[str]  = mapped_column(String(50))
    date_open:      Mapped[str]  = mapped_column(Date)


    def __repr__(self):
        return f"EventModel({self.id=}, {self.name=}, {self.date=})"