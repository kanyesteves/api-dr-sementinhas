from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class UserBase(DeclarativeBase):
    pass

class UserEntity(UserBase):
    __tablename__ = 'users'

    id:             Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    name:           Mapped[str]  = mapped_column(String(50))
    password:       Mapped[str]  = mapped_column(String(128))
    email:          Mapped[str]  = mapped_column(String(50))
    date_open:      Mapped[str]  = mapped_column(Date)


    def __repr__(self):
        return f"UserModel({self.id=}, {self.name=}, {self.password=})"