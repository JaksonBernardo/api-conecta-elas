from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from .Base import Base


class Mensagens(Base):

    __tablename__ = "mensagens"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_contato: Mapped[int] = mapped_column(ForeignKey("contatos.id"), nullable=False)
    id_tipo_ator: Mapped[int] = mapped_column(ForeignKey("atores.id"), nullable=False)
    id_empresa: Mapped[int] = mapped_column(ForeignKey("empresa.id"), nullable=False)
    texto: Mapped[String] = mapped_column(String(1000), nullable=False)
    data: Mapped[String] = mapped_column(String(10), nullable=False)  # Formato: 'YYYY-MM-DD'
    hora: Mapped[String] = mapped_column(String(8), nullable=False)   # Formato: 'HH:MM:SS'

    contato: Mapped["Contatos"] = relationship(  # type: ignore
        "Contatos",
        back_populates="mensagens"
    )

    empresa: Mapped["Empresa"] = relationship(  # type: ignore
        "Empresa",
        back_populates="mensagens"
    )

    ator: Mapped["Atores"] = relationship(  # type: ignore
        "Atores"
    )


