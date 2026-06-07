import pytest
from playwright.sync_api import Page
from faker import Faker

fake = Faker('pt_BR')

@pytest.mark.e2e
def test_adesao_assinatura_sucesso_ct001(page: Page, home_page, planos_page, checkout_page):
    """
    CT001: Validar fluxo completo de adesão de assinatura com sucesso (Cartão Válido)
    """
    nome_fake = fake.name()
    email_fake = fake.email()

    # 1. Acesso à Home e Navegação
    home_page.acessar_babyrefil().clicar_assinar_agora()

    # 2. Seleção de Plano
    planos_page.selecionar_primeiro_plano()

    # 3. Recorrência
    planos_page.escolher_frequencia('Mensal')

    # 4. Dados Pessoais e Endereço
    checkout_page.preencher_dados_pessoais(
        nome=nome_fake, 
        email=email_fake, 
        telefone='11999999999', 
        nome_bebe='Baby QA'
    ).preencher_endereco_e_avancar(
        cep='04534-011', 
        numero='1000', 
        rua_esperada='Rua Joaquim Floriano',
        complemento='17o andar'
    )

    # 5. Pagamento
    checkout_page.preencher_dados_pagamento_e_finalizar(
        num_cartao='4242424242424242', 
        nome_cartao=nome_fake.upper(), 
        validade='12/30', 
        cvv='182', 
        cpf='00000000000'
    )

    # 6. Confirmação
    checkout_page.validar_sucesso()

@pytest.mark.e2e
def test_adesao_falha_pagamento_ct002(page: Page, home_page, planos_page, checkout_page):
    """
    CT002: Validar fluxo de adesão com falha no pagamento (Cartão Recusado)
    """
    nome_fake = fake.name()
    email_fake = fake.email()

    # 1. Acesso à Home e Navegação
    home_page.acessar_babyrefil().clicar_assinar_agora()

    # 2. Seleção de Plano
    planos_page.selecionar_primeiro_plano()

    # 3. Recorrência
    planos_page.escolher_frequencia('Mensal')

    # 4. Dados Pessoais e Endereço
    checkout_page.preencher_dados_pessoais(
        nome=nome_fake, 
        email=email_fake, 
        telefone='11999999999', 
        nome_bebe='Baby QA'
    ).preencher_endereco_e_avancar(
        cep='04534-011', 
        numero='1000', 
        rua_esperada='Rua Joaquim Floriano',
        complemento='17o andar'
    )

    # 5. Pagamento (Cartão Inválido - Saldo Insuficiente)
    checkout_page.preencher_dados_pagamento_e_finalizar(
        num_cartao='5555555555554444', 
        nome_cartao=nome_fake.upper(), 
        validade='12/30', 
        cvv='182', 
        cpf='00000000000'
    )

    # 6. Asserção de Falha
    checkout_page.validar_falha_pagamento()
