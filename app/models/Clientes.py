from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .Base import Base

class Clientes(Base):

    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    razao_social: Mapped[String] = mapped_column(String(255), nullable = False)
    cnpj: Mapped[String] = mapped_column(String(20), nullable = False)
    endereco: Mapped[String] = mapped_column(String(100), nullable = True)
    cep: Mapped[String] = mapped_column(String(9), nullable = True)
    email: Mapped[String] = mapped_column(String(100), nullable = True)
    nome_responsavel: Mapped[String] = mapped_column(String(50), nullable = True)
    id_empresa: Mapped[int] = mapped_column(ForeignKey("empresa.id"), nullable = False)

    empresa: Mapped["Empresa"] = relationship( # type: ignore
        back_populates="clientes",
        uselist=False
    )

    orcamentos: Mapped[list["Orcamentos"]] = relationship( # type: ignore
        "Orcamentos",
        back_populates="cliente",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:

        return f"Clientes(id={self.id}, razao_social={self.razao_social}, cnpj={self.cnpj}, endereco={self.endereco}, cep={self.cep}, email={self.email}, nome_responsavel={self.nome_responsavel}, id_empresa={self.id_empresa})"

