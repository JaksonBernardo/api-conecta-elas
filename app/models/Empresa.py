from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .Base import Base

class Empresa(Base):

    __tablename__ = "empresa"

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    razao_social: Mapped[String] = mapped_column(String(255), nullable = False)
    cnpj: Mapped[String] = mapped_column(String(20), nullable = False)
    endereco: Mapped[String] = mapped_column(String(100), nullable = True)
    cep: Mapped[String] = mapped_column(String(9), nullable = True)
    logradouro: Mapped[String] = mapped_column(String(150), nullable = True)
    complemento: Mapped[String] = mapped_column(String(30), nullable = True)
    bairro: Mapped[String] = mapped_column(String(20), nullable = True)
    email: Mapped[String] = mapped_column(String(100), nullable = True)
    telefone: Mapped[String] = mapped_column(String(20), nullable = True)
    meu_site: Mapped[String] = mapped_column(String(100), nullable = True)

    usuario: Mapped["Usuarios"] = relationship( # type: ignore 
        "Usuarios",
        back_populates = "empresa",
        uselist = False,
        cascade = "all, delete-orphan",
        single_parent = True
    )

    clientes: Mapped[list["Clientes"]] = relationship( # type: ignore
        "Clientes",
        back_populates = "empresa",
        cascade = "all, delete-orphan",
        single_parent = True
    )

    fornecedores: Mapped[list["Fornecedores"]] = relationship( # type: ignore
        "Fornecedores",
        back_populates = "empresa",
        cascade = "all, delete-orphan",
        single_parent = True
    )

    orcamentos: Mapped[list["Orcamentos"]] = relationship( # type: ignore
        "Orcamentos",
        back_populates = "empresa",
        cascade = "all, delete-orphan",
        single_parent = True
    )

    servicos: Mapped[list["Servicos"]] = relationship( # type: ignore
        "Servicos",
        back_populates = "empresa",
        cascade = "all, delete-orphan",
        single_parent = True
    )

    contatos: Mapped[list["Contatos"]] = relationship(  # type: ignore
        "Contatos",
        back_populates="empresa",
        cascade="all, delete-orphan",
        single_parent=True
    )

    mensagens: Mapped[list["Mensagens"]] = relationship(  # type: ignore
        "Mensagens",
        back_populates="empresa",
        cascade="all, delete-orphan",
        single_parent=True
    )

    questionario: Mapped["Questionario"] = relationship( # type: ignore
        "Questionario",
        back_populates="empresa",
        uselist=False,
        cascade="all, delete-orphan",
        single_parent=True
    )

    def __repr__(self) -> str:

        return f"User(id={self.id}, razao_social={self.razao_social}, cnpj={self.cnpj}, endereco={self.endereco}, cep={self.cep}, logradouro={self.logradouro}, complemento={self.complemento}, bairro={self.bairro}, email={self.email}, telefone={self.telefone}, meu_site={self.meu_site})"


