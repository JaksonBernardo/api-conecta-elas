from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from .Base import Base


class Contatos(Base):

    __tablename__ = "contatos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[String] = mapped_column(String(100), nullable=False)
    telefone: Mapped[String] = mapped_column(String(20), nullable=True)
    email: Mapped[String] = mapped_column(String(100), nullable=True)
    cep: Mapped[String] = mapped_column(String(9), nullable=True)
    numero: Mapped[String] = mapped_column(Integer, nullable=True)
    logradouro: Mapped[String] = mapped_column(String(150), nullable=True)
    complemento: Mapped[String] = mapped_column(String(30), nullable=True)
    bairro: Mapped[String] = mapped_column(String(20), nullable=True)
    cidade: Mapped[String] = mapped_column(String(50), nullable=True)
    estado: Mapped[String] = mapped_column(String(2), nullable=True)
    id_empresa: Mapped[int] = mapped_column(ForeignKey("empresa.id"), nullable=False)

    empresa: Mapped["Empresa"] = relationship(  # type: ignore
        "Empresa",
        back_populates="contatos"
    )

    mensagens: Mapped[list["Mensagens"]] = relationship(  # type: ignore
        "Mensagens",
        back_populates="contato",
        cascade="all, delete-orphan",
        single_parent=True
    )

    def __repr__(self) -> str:
        return f"Contatos(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone}, empresa_id={self.empresa_id})"

