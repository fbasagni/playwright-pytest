# Automação E2E - BabyRefil
![Status](https://img.shields.io/badge/status-ativo-success.svg) ![Python](https://img.shields.io/badge/python-3.11+-blue.svg) ![Playwright](https://img.shields.io/badge/playwright-0.7.1-green)

Projeto de automação de testes End-to-End (E2E) para a loja virtual de assinatura de fraldas, **BabyRefil**.

---

## 1. Sobre o projeto

Este projeto demonstra a construção completa de um framework de testes automatizados ponta-a-ponta, simulando jornadas de usuários reais desde o acesso até a finalização do fluxo de assinatura. O projeto foca em testar:

- Fluxo de adesão com sucesso utilizando um meio de pagamento válido.
- Fluxo de adesão com falha utilizando um meio de pagamento bloqueado (simulando casos de transação não autorizada).
- Navegação fluida e validações visuais baseadas em assertivas estritas (`expect`).

A modelagem foi pensada utilizando o design pattern de Page Objects (POM), garantindo consistência, fácil escalabilidade e legibilidade de código.

---

## 2. O que foi implementado

- Arquitetura baseada em **Page Object Model (POM)**.
- Geração de massa de dados dinâmicos utilizando **Faker**, simulando entradas reais a cada execução.
- Navegação padronizada definindo `base-url` via **pytest.ini**.
- Injeção de dependência e controle de fluxo configurados puramente através do **conftest.py** (fixtures customizadas).
- Interface fluente (_Fluent Interface_) para encadeamento de chamadas e legibilidade explícita de testes.
- Geração de relatórios robustos com o framework **Allure Reports**.

---

## 3. Estrutura do Repositório

```text
playwright-pytest/
├── playwright/                   # Diretório principal da automação
│   ├── e2e/                      # Scripts de setup e testes E2E
│   │   └── test_adesao.py        # Cenários de sucesso e falhas de pagamento
│   ├── pages/                    # Page Objects (abstração de tela)
│   │   ├── checkout_page.py      
│   │   ├── home_page.py          
│   │   └── planos_page.py        
│   └── conftest.py               # Configurações do Pytest (fixtures)
├── allure-results/               # Evidências e outputs de relatórios (Gerado automaticamente)
├── pytest.ini                    # Parâmetros padrão do Pytest e marcações customizadas
├── requirements.txt              # Bibliotecas listadas para o ambiente
└── README.md                     # Documentação de implantação e utilização
```

---

## 4. Tecnologias Utilizadas

- **Linguagem**: Python
- **Automator Framework**: Playwright (via `pytest-playwright`)
- **Testing Framework**: Pytest
- **Reports**: Allure
- **Massa de Dados**: Faker

---

## 5. Como Executar

Para reproduzir o projeto em qualquer ambiente:

1. Clone o repositório.
2. Crie e ative uma virtual environment (ex: `python -m venv .venv`).
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Instale e garanta os navegadores suportados pelo Playwright:
   ```bash
   playwright install chromium
   ```
5. Execute os testes automatizados (Headless mode é o padrão):
   ```bash
   pytest
   ```
6. **[Opcional]** Explore a execução chamando a UI do navegador (Headed):
   ```bash
   pytest --headed
   ```
7. Para gerar e ver os relatórios:
   ```bash
   allure serve allure-results
   ```

---

## 6. Detalhes de Arquitetura e Boas Práticas

- **Testes mais limpos com Pytest**: Uso de _fixtures_ no `conftest.py` para injetar os Page Objects direto nos testes, mantendo os scripts focados apenas nas regras de negócio.
- **Evidências sob demanda**: O `pytest.ini` foi configurado para salvar vídeos, screenshots e traces apenas quando um teste falha (`on-failure`). Isso poupa espaço em disco e facilita a integração contínua (CI).
- **Locators resilientes**: Priorização de seletores baseados em acessibilidade e comportamento do usuário (`get_by_role`, `get_by_text`). Essa abordagem evita o uso de locators frágeis (como XPaths complexos) e reduz drasticamente a quebra da automação por mudanças de layout.