from sqlalchemy import Table, Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import List

from .Base import Base

class OrcamentoServico(Base):

    __tablename__ = "orcamento_servico"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    orcamento_id: Mapped[int] = mapped_column(ForeignKey("orcamentos.id", ondelete="CASCADE"), nullable=False)
    
    servico_id: Mapped[int] = mapped_column(ForeignKey("servicos.id", ondelete="CASCADE"), nullable=False)
    
    quantidade: Mapped[float] = mapped_column(Float, default=1.0)
    preco_unitario: Mapped[float] = mapped_column(Float, nullable=False)
    desconto: Mapped[float] = mapped_column(Float, default=0.0)
    
    orcamento: Mapped["Orcamentos"] = relationship( # type: ignore
        "Orcamentos", 
        back_populates="orcamento_servicos"
    )
    
    servico: Mapped["Servicos"] = relationship( # type: ignore
        "Servicos", 
        back_populates="orcamento_servicos"
    )
    
    def __repr__(self) -> str:
        
        return f"OrcamentoServico(id={self.id}, orcamento_id={self.orcamento_id}, servico_id={self.servico_id}, quantidade={self.quantidade}, preco_unitario={self.preco_unitario})"