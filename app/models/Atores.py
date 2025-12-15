from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .Base import Base

class Atores(Base):

    __tablename__ = "atores"

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    tipo: Mapped[String] = mapped_column(String(10), nullable = False)

    def __repr__(self) -> str:
        
        return f"Atores(id={self.id}, tipo={self.tipo})"

