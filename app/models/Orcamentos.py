from sqlalchemy import String, Integer, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


from .Base import Base

class Orcamentos(Base):

    __tablename__ = "orcamentos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    codigo: Mapped[int] = mapped_column(Integer, nullable=False)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id"), nullable=False)
    id_empresa: Mapped[int] = mapped_column(ForeignKey("empresa.id"), nullable=False)
    valor_total_sem_desconto: Mapped[float] = mapped_column(Float, nullable=False)
    tipo_desconto: Mapped[str] = mapped_column(String(2), nullable=True)
    valor_desconto: Mapped[float] = mapped_column(Float, nullable=True)
    data_emissao: Mapped[str] = mapped_column(String(10), nullable=False)
    hora_emissao: Mapped[str] = mapped_column(String(8), nullable=False)
    descricao: Mapped[str] = mapped_column(String(500), nullable=True)

    cliente: Mapped["Clientes"] = relationship( # type: ignore
        "Clientes",
        back_populates="orcamentos",
        uselist=False,
    )

    empresa: Mapped["Empresa"] = relationship( # type: ignore
        "Empresa",
        back_populates="orcamentos",
        uselist=False
    )

    orcamento_servicos: Mapped[List["OrcamentoServico"]] = relationship( # type: ignore
        "OrcamentoServico",
        back_populates="orcamento",
        cascade="all, delete-orphan"
    )
    
    @property
    def servicos(self):

        return [os.servico for os in self.orcamento_servicos]


    def __repr__(self) -> str:
        return f"Orcamentos(id={self.id}, codigo={self.codigo}, cliente_id={self.id_cliente}, valor_total={self.valor_total_sem_desconto})"