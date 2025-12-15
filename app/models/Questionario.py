from sqlalchemy import String, Integer, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .Base import Base

class Questionario(Base):

    __tablename__ = "questionario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_empresa: Mapped[int] = mapped_column(ForeignKey("empresa.id", ondelete="CASCADE"), nullable=False)
    nome_completo: Mapped[str] = mapped_column(String(250), nullable=False)
    tipo_usuario: Mapped[str] = mapped_column(Text, nullable=True)
    nome_negocio: Mapped[str] = mapped_column(Text, nullable=True)
    ramo_negocio: Mapped[str] = mapped_column(Text, nullable=True)
    busca_plataforma: Mapped[str] = mapped_column(Text, nullable=True)
    instagram: Mapped[str] = mapped_column(Text, nullable=True)
    facebook: Mapped[str] = mapped_column(Text, nullable=True)
    youtube: Mapped[str] = mapped_column(Text, nullable=True)
    link: Mapped[str] = mapped_column(Text, nullable=True)
    origem_usuario: Mapped[str] = mapped_column(Text, nullable=True)
    receber_novidade: Mapped[int] = mapped_column(Integer, default=0)  # 0 = não, 1 = sim

    empresa: Mapped["Empresa"] = relationship( # type: ignore
        "Empresa",
        back_populates="questionario",
        uselist=False
    )

    def __repr__(self) -> str:

        return f"Questionario(id={self.id}, nome_completo={self.nome_completo}, id_empresa={self.id_empresa}, nome_negocio={self.nome_negocio})"