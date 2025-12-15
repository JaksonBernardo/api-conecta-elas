from sqlalchemy import String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from .Base import Base

class Servicos(Base):

    __tablename__ = "servicos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    custo_total: Mapped[float] = mapped_column(Float, nullable=False)
    despesa_fixa: Mapped[float] = mapped_column(Float, nullable=True)
    impostos: Mapped[float] = mapped_column(Float, nullable=True)
    margem_lucro: Mapped[float] = mapped_column(Float, nullable=True)
    preco: Mapped[float] = mapped_column(Float, nullable=False)  # Preço base/sugerido
    id_empresa: Mapped[int] = mapped_column(ForeignKey("empresa.id"), nullable=False)

    empresa: Mapped["Empresa"] = relationship( # type: ignore
        "Empresa",
        back_populates="servicos",
        uselist=False
    )

    orcamento_servicos: Mapped[List["OrcamentoServico"]] = relationship( # type: ignore
        "OrcamentoServico",
        back_populates="servico",
        cascade="all, delete-orphan"
    )
    
    @property
    def orcamentos(self):

        return [os.orcamento for os in self.orcamento_servicos]

    def __repr__(self) -> str:

        return f"Servicos(id={self.id}, nome={self.nome}, preco={self.preco}, id_empresa={self.id_empresa})"
    