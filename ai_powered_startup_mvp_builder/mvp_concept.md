# mvp_concept.md

# MVP Concept - AI Content Refiner Agent

## Problem Statement
Mentores e criadores de conteúdo técnico perdem muito tempo tentando converter documentações extensas, changelogs ou artigos técnicos em posts engajados para redes sociais (LinkedIn/Discord). O processo de extrair o "ouro" de um texto técnico e adaptar a tonalidade manualmente é lento e propenso a bloqueio criativo.

## Target Users
- Mentores de cursos EAD e Instrutores Técnicos.
- Desenvolvedores Indie (MEIs) divulgando seus serviços.
- Gestores de Comunidade Técnica.

## Core Features
1.  **URL Scraper & Parser:** Capacidade de ler uma URL (artigo ou doc), extrair o texto principal e limpar ruídos (menus, ads).
2.  **Multi-Platform Generator:** Gerar automaticamente três versões do conteúdo:
    - *Post LinkedIn:* Focado em autoridade e lições aprendidas.
    - *Snippet Discord:* Curto, direto e com formatação de código.
    - *Thread Twitter/X:* Sequencial e opinativo.
3.  **Tone Customization:** Seletor de "Personalidade do Agente" (ex: "Mentor Encorajador", "Crítico Técnico", "Vendedor Entusiasta").
4.  **Review Mode:** Exibição do texto gerado com opção de regenerar seções específicas.
5.  **History Log:** Armazenamento local (JSON) das últimas 10 gerações para referência rápida.

## Constraints
- **Sem Banco de Dados Complexo:** Persistência apenas via arquivos locais (JSON/CSV) para agilidade.
- **Single User:** Aplicação projetada para uso individual (local host ou server simples), sem sistema de autenticação multi-usuário.
- **Tech Stack:** Python (Backend leve) + Streamlit (Frontend rápido) + OpenAI API (LLM).
- **Limite de Entrada:** Processamento de textos de até 15.000 caracteres por vez.
