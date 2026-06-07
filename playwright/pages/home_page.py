import re
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def acessar_babyrefil(self) -> 'HomePage':
        self.page.goto('/')
        expect(self.page.get_by_role('heading', name='Fraldas e cuidados na sua porta.')).to_be_visible()
        return self

    def clicar_assinar_agora(self) -> 'HomePage':
        self.page.get_by_role('link', name=re.compile('Assinar Agora', re.IGNORECASE)).first.click()
        return self
