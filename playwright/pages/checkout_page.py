import re
from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def preencher_dados_pessoais(self, nome, email, telefone, nome_bebe, idade_index='0-3 meses') -> 'CheckoutPage':
        expect(self.page.get_by_role('heading', name='Dados Pessoais')).to_be_visible()
        self.page.get_by_role('textbox', name='Nome Completo').fill(nome)
        self.page.get_by_role('textbox', name='E-mail').fill(email)
        self.page.get_by_role('textbox', name='Telefone').fill(telefone)
        self.page.get_by_role('textbox', name='Nome do Bebê').fill(nome_bebe)
        
        self.page.get_by_role('combobox', name='Idade do Bebê').click()
        self.page.get_by_role('option', name=idade_index).click()
        return self

    def preencher_endereco_e_avancar(self, cep, numero, rua_esperada='Rua Joaquim Floriano', complemento='') -> 'CheckoutPage':
        self.page.get_by_role('textbox', name='CEP').fill(cep)
        self.page.get_by_role('button', name='Buscar').click()
        
        expect(self.page.get_by_role('textbox', name='Rua')).to_have_value(rua_esperada)
        
        self.page.get_by_role('textbox', name='Número').fill(numero)
        if complemento:
            self.page.get_by_role('textbox', name='Complemento (Opcional)').fill(complemento)
        
        self.page.get_by_role('button', name='Avançar').click()
        return self

    def preencher_dados_pagamento_e_finalizar(self, num_cartao, nome_cartao, validade, cvv, cpf) -> 'CheckoutPage':
        expect(self.page.get_by_text('Resumo do Pedido')).to_be_visible()
        
        self.page.get_by_role('textbox', name='Número do Cartão').fill(num_cartao)
        self.page.get_by_role('textbox', name='Nome no Cartão').fill(nome_cartao)
        self.page.get_by_role('textbox', name='Validade').fill(validade)
        self.page.get_by_role('textbox', name='CVV').fill(cvv)
        self.page.get_by_role('textbox', name='CPF do Titular').fill(cpf)

        self.page.get_by_role('button', name='Finalizar Assinatura').click()
        return self

    def validar_sucesso(self) -> 'CheckoutPage':
        expect(self.page.get_by_role('heading', name='Assinatura confirmada!')).to_be_visible(timeout=15000)
        expect(self.page.get_by_text(re.compile(r'Pedido nº BR\d+'))).to_be_visible()
        return self

    def validar_falha_pagamento(self) -> 'CheckoutPage':
        error_msg = self.page.get_by_text('Transação não autorizada', exact=False).nth(0)
        expect(error_msg).to_be_visible(timeout=15000)
        expect(self.page).to_have_url('https://babyrefil.vercel.app/subscribe')
        return self
