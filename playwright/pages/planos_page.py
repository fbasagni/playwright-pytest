from playwright.sync_api import Page, expect

class PlanosPage:
    def __init__(self, page: Page):
        self.page = page

    def selecionar_primeiro_plano(self) -> 'PlanosPage':
        expect(self.page.get_by_role('heading', name='Escolha o seu plano')).to_be_visible()
        self.page.get_by_role('button', name='Selecionar Plano').nth(0).click()
        return self

    def escolher_frequencia(self, frequencia: str = 'Mensal') -> 'PlanosPage':
        expect(self.page.get_by_text('Frequência da Entrega')).to_be_visible()
        self.page.get_by_text(frequencia, exact=True).click()
        self.page.get_by_role('button', name='Avançar').click()
        return self
