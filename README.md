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

Não há dependências de instalação ou etapa de build. O cache dos dados do GitHub dura uma hora no navegador.

## Estado visual

Esta cópia preserva o tema existente. A revisão da paleta e dos detalhes visuais está pendente das escolhas do Yuri.

## Publicação

Site público: https://yuri-medeiros.github.io/portifolio/

O workflow `.github/workflows/pages.yml` publica automaticamente a cada push em `main` e também pode ser iniciado manualmente pela aba Actions. Configure Settings → Pages → Source como **GitHub Actions**.

Não existe etapa de build. Somente `index.html` e a pasta `assets/`, quando existir, são incluídos na publicação. O artifact `github-pages` fica disponível por um dia; sua expiração não remove o site publicado.

O workflow usa runners padrão e GitHub Pages em um repositório público, sem serviço pago ou domínio próprio. Consulte os limites atuais de armazenamento do GitHub Actions ao adicionar arquivos grandes.
