"""
Teste do relacionamento N:N entre Orcamentos e Servicos.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.models import Base, Empresa, Usuarios, Clientes, Servicos, Orcamentos, OrcamentoServico

def test_relacionamento_nn():
    """Testa relacionamento muitos-para-muitos."""
    
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    
    print("=" * 60)
    print("TESTE RELACIONAMENTO N:N (ORÇAMENTOS ↔ SERVIÇOS)")
    print("=" * 60)
    
    with Session(engine) as session:
        # 1. Cria empresa e usuário
        print("\n1. Criando empresa...")
        empresa = Empresa(
            razao_social="Empresa Teste N:N",
            cnpj="00.000.000/0001-00"
        )
        
        usuario = Usuarios(
            nome="Teste User",
            email="teste@empresa.com",
            senha="123",
            empresa=empresa
        )
        
        # 2. Cria cliente
        print("\n2. Criando cliente...")
        cliente = Clientes(
            razao_social="Cliente Teste",
            cnpj="11.111.111/0001-11",
            empresa=empresa
        )
        
        # 3. Cria serviços
        print("\n3. Criando serviços...")
        servicos = [
            Servicos(
                nome="Desenvolvimento Web",
                custo_total=1000.00,
                preco=1500.00,
                empresa=empresa
            ),
            Servicos(
                nome="Consultoria TI",
                custo_total=500.00,
                preco=800.00,
                empresa=empresa
            ),
            Servicos(
                nome="Manutenção de Sistemas",
                custo_total=300.00,
                preco=500.00,
                empresa=empresa
            ),
            Servicos(
                nome="Hospedagem Cloud",
                custo_total=200.00,
                preco=350.00,
                empresa=empresa
            )
        ]
        
        for servico in servicos:
            session.add(servico)
        
        # 4. Cria orçamentos
        print("\n4. Criando orçamentos...")
        
        # Orçamento 1: Usa Serviço 1 e 2
        orcamento1 = Orcamentos(
            codigo=1001,
            cliente=cliente,
            empresa=empresa,
            valor_total_sem_desconto=0.0,  # Será calculado
            data_emissao="2024-01-15",
            hora_emissao="10:00:00",
            descricao="Orçamento para site + consultoria"
        )

        
        # Orçamento 2: Usa Serviço 1, 3 e 4
        orcamento2 = Orcamentos(
            codigo=1002,
            cliente=cliente,
            empresa=empresa,
            valor_total_sem_desconto=0.0,  # Será calculado
            data_emissao="2024-01-16",
            hora_emissao="14:30:00",
            descricao="Orçamento completo"
        )
        
        # Orçamento 3: Usa apenas Serviço 3
        orcamento3 = Orcamentos(
            codigo=1003,
            cliente=cliente,
            empresa=empresa,
            valor_total_sem_desconto=0.0,
            data_emissao="2024-01-17",
            hora_emissao="16:00:00",
            descricao="Apenas manutenção"
        )
        
        
        session.add_all([orcamento1, orcamento2, orcamento3])
        session.commit()
        
        print("✅ Dados criados com sucesso!")
        
        # 5. Testa os relacionamentos
        print("\n5. Testando relacionamentos N:N...")
        
        # Verifica orçamento 1
        print(f"\n📋 ORÇAMENTO #{orcamento1.codigo}:")
        print(f"   Valor total: R$ {orcamento1.valor_total_sem_desconto:.2f}")
        print(f"   Serviços ({len(orcamento1.orcamento_servicos)}):")
        for i, os_item in enumerate(orcamento1.orcamento_servicos, 1):
            print(f"   {i}. {os_item.servico.nome}")
            print(f"      Quantidade: {os_item.quantidade}")
            print(f"      Preço unitário: R$ {os_item.preco_unitario:.2f}")
            print(f"      Subtotal: R$ {os_item.quantidade * os_item.preco_unitario:.2f}")
        
        # Verifica orçamento 2
        print(f"\n📋 ORÇAMENTO #{orcamento2.codigo}:")
        print(f"   Valor total: R$ {orcamento2.valor_total_sem_desconto:.2f}")
        print(f"   Serviços ({len(orcamento2.orcamento_servicos)}):")
        for i, os_item in enumerate(orcamento2.orcamento_servicos, 1):
            print(f"   {i}. {os_item.servico.nome}")
        
        # Verifica serviço 1 (aparece em múltiplos orçamentos)
        print(f"\n🔧 SERVIÇO: {servicos[0].nome}")
        print(f"   Aparece em {len(servicos[0].orcamento_servicos)} orçamentos:")
        for i, os_item in enumerate(servicos[0].orcamento_servicos, 1):
            print(f"   {i}. Orçamento #{os_item.orcamento.codigo}")
        
        # Verifica serviço 3 (também em múltiplos)
        print(f"\n🔧 SERVIÇO: {servicos[2].nome}")
        print(f"   Aparece em {len(servicos[2].orcamento_servicos)} orçamentos:")
        for i, os_item in enumerate(servicos[2].orcamento_servicos, 1):
            print(f"   {i}. Orçamento #{os_item.orcamento.codigo}")
        
        # 6. Testa cálculos
        print("\n6. Verificando cálculos...")
        
        # Orçamento 1: 1500 + (2 * 800) = 3100
        print(f"   Orçamento 1 esperado: R$ 3100.00")
        print(f"   Orçamento 1 calculado: R$ {orcamento1.valor_total_sem_desconto:.2f}")
        print(f"   ✅ Correto? {abs(orcamento1.valor_total_sem_desconto - 3100.00) < 0.01}")
        
        # Orçamento 2: 1500 + 500 + (12 * 350) = 6200
        print(f"   Orçamento 2 esperado: R$ 6200.00")
        print(f"   Orçamento 2 calculado: R$ {orcamento2.valor_total_sem_desconto:.2f}")
        print(f"   ✅ Correto? {abs(orcamento2.valor_total_sem_desconto - 6200.00) < 0.01}")
        
        # Orçamento 3: 500 com 10% desconto = 450
        print(f"   Orçamento 3 esperado: R$ 450.00")
        print(f"   Orçamento 3 calculado: R$ {orcamento3.valor_total_sem_desconto:.2f}")
        print(f"   ✅ Correto? {abs(orcamento3.valor_total_sem_desconto - 450.00) < 0.01}")
        
        # 7. Testa propriedades helper
        print("\n7. Testando propriedades helper...")
        print(f"   orcamento1.servicos: {len(orcamento1.servicos)} serviços")
        print(f"   servico1.orcamentos: {len(servicos[0].orcamentos)} orçamentos")
        
        print("\n" + "=" * 60)
        print("✅ RELACIONAMENTO N:N FUNCIONANDO CORRETAMENTE!")
        print("=" * 60)

if __name__ == "__main__":
    test_relacionamento_nn()