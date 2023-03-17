from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class BasicTable(Base):
    __tablename__ = "base_table"
    __table_args__ = {"schema": "public"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[Optional[str]] = mapped_column(String(250))

    def __repr__(self) -> str:
        return f"row=(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
