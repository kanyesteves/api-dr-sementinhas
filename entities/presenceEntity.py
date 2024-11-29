from sqlalchemy import String, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class PresenceBase(DeclarativeBase):
    pass

class PresenceEntity(PresenceBase):
    __tablename__ = 'presences'

    id:               Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    users_present:    Mapped[dict]  = mapped_column(JSON)
    description:      Mapped[str]  = mapped_column(String(128))


    def __repr__(self):
        return f"PresenceModel({self.id=}, {self.description=})"