# Portfólio de Yuri Medeiros

Site pessoal estático para apresentar o perfil profissional, experiência, habilidades, formação, certificados e repositórios GitHub.

## Como visualizar localmente

Abra `index.html` em um navegador. Para que a consulta à API pública do GitHub funcione em todos os navegadores, sirva esta pasta por HTTP, por exemplo:

```powershell
python -m http.server 4173
```

Depois acesse `http://localhost:4173`.

## Estrutura

- `index.html` — página completa, estilos e consulta aos repositórios via API pública do GitHub.

Não há dependências de instalação ou etapa de build. Os 17 repositórios públicos consultados em 02/10/2026 estão incorporados no HTML e agrupados pela linguagem principal do GitHub (8 linguagens e o grupo Outros). Os indicadores e cartões funcionam sem JavaScript ou conexão. Com conexão, a página consulta todas as páginas da API pública do GitHub e atualiza os dados; se a consulta falhar, preserva a lista incorporada. A referência dos dados está em `assets/repositories.json`.

## Estado visual

Visual baseado nas referências: tema claro, ondas em azul suave, cartões translúcidos e navegação com indicador da seção ativa. Layout adaptado para celular e preferência de movimento reduzido. O fundo vetorial está em `assets/waves.svg`.

## Publicação

Site público: https://yuri-medeiros.github.io/portifolio/

O workflow `.github/workflows/pages.yml` publica automaticamente a cada push em `main` e também pode ser iniciado manualmente pela aba Actions. Configure Settings → Pages → Source como **GitHub Actions**.

Não existe etapa de build. Somente `index.html` e a pasta `assets/`, quando existir, são incluídos na publicação. O artifact `github-pages` fica disponível por um dia; sua expiração não remove o site publicado.

O workflow usa runners padrão e GitHub Pages em um repositório público, sem serviço pago ou domínio próprio. Consulte os limites atuais de armazenamento do GitHub Actions ao adicionar arquivos grandes.

Os indicadores mostram o total de repositórios e a proporção de repositórios por linguagem principal (não a quantidade de linhas de código). O calendário dos últimos 12 meses é gerado pela API GraphQL oficial no GitHub Actions, usando `github.token` somente no runner. O workflow publica `assets/contributions.json` junto ao site e roda diariamente às 03:17 (America/Sao_Paulo). A página consulta esse JSON ao abrir e desenha o calendário em SVG. Nenhuma credencial vai ao navegador. Os dados anuais só ficam disponíveis após executar a publicação; abrir o HTML local não consulta GraphQL. Falhas da consulta aparecem nos logs do Actions e o site mostra indisponibilidade, sem inventar contagens.

Os certificados são exibidos como imagens em uma janela no portfólio, sem visualizador PDF ou controles de download. Apenas imagens ficam em `assets/certificates/`; PDFs originais não são incluídos na publicação. Conteúdo visível pode ser capturado pelo visitante.
