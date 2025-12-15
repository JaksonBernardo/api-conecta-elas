from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .Base import Base

class Usuarios(Base):

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    nome: Mapped[String] = mapped_column(String(100), nullable = False)
    email: Mapped[String] = mapped_column(String(100), nullable = False, unique = True)
    senha: Mapped[String] = mapped_column(String(255), nullable = False)
    empresa_id: Mapped[int] = mapped_column(ForeignKey("empresa.id"), nullable = False, unique = True)

    empresa: Mapped["Empresa"] = relationship( # type: ignore
        back_populates="usuario",
        uselist=False
    )

    def __repr__(self) -> str:

        return f"Usuarios(id={self.id}, nome={self.nome}, email={self.email}, empresa_id={self.empresa_id})"
