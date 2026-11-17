# Banco de Alimentos de Gravataí — MVP (Controlo de Stock e PVPS)

Aplicação web responsiva (*mobile-first*) desenvolvida para apoiar a triagem, o controlo de prazos de validade pelo método **PVPS (Primeiro que Vence, Primeiro que Sai)** e o registo de entregas às entidades assistenciais do **Banco de Alimentos de Gravataí (RS)**.

## Arquitetura e Tecnologias
* **Padrão Arquitetural:** Monolítica em Camadas (MVT — *Model-View-Template*)
* **Back-end:** Python 3.12 + Flask 3.0
* **Front-end:** HTML5 + Bootstrap 5.3 (acessibilidade WCAG AA / RNF04)
* **Base de Dados:** MySQL 8.0 (`Flask-SQLAlchemy` / `PyMySQL`)
* **Segurança:** Autenticação com hash `PBKDF2-SHA256` (`Werkzeug`), consultas parametrizadas e proteção contra XSS (OWASP Top 10)

## Funcionalidades do MVP
- **RF01:** Registo de entrada de lotes de alimentos com validação de data de validade.
- **RF02:** Listagem ativa ordenada automaticamente por vencimento mais próximo (PVPS) com alertas visuais (cor, ícone e texto).
- **RF03:** Baixa de saídas para entidades beneficiárias ativas com abatimento imediato de saldo.
- **RF04:** Relatório mensal consolidado de movimentações.

## Estrutura Prevista do Projeto
```text
├── app/
│   ├── models/        # Entidades MySQL (alimentos, lotes_estoque, entidades, saidas)
│   ├── routes/        # Controladores e regras PVPS
│   ├── templates/     # Interfaces HTML responsivas (Jinja2)
│   └── static/        # CSS e recursos locais
├── tests/             # Testes unitários e de integração
├── .env.example       # Modelo de variáveis de ambiente
├── requirements.txt   # Dependências fixadas
└── README.md
