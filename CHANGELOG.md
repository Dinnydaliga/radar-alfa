# Histórico de alterações — Radar Alfa

Este arquivo é a trilha cronológica do projeto. Toda alteração deve ter registro verificável, inclusive correções de documentação e configurações. Usar datas no formato AAAA-MM-DD.

## 2026-11-20 — Correção do timeout PNCP

- **Ação:** limitar teste a uma página; duas tentativas com timeout de 18 segundos, logs por tentativa, resposta validada e arquivo JSON com status/erros; Actions salva artefato também em falha.
- **Evidência:** capturas de três execuções com `The read operation timed out` após 25 segundos; Python e sintaxe concluídos.
- **Testes:** revisão do código e gravação confirmada no GitHub; **a nova versão ainda não foi executada**.
- **Pendências:** novo teste manual, avaliar qualidade dos dados e endpoint alternativo se persistir falha.

## 2026-11-20 — Workflow manual GitHub Actions

- **Ação:** criado `.github/workflows/teste-pncp.yml` com execução manual, teste de sintaxe, consulta PNCP e artefato temporário de resultado; atualizados README, checkpoints e decisões.
- **Motivo:** tornar o piloto visível na aba Actions, sem ativar agendamento.
- **Teste:** configuração gravada no GitHub; execução do workflow e consulta à API ainda não confirmadas.
- **Pendências:** rodar manualmente, conferir logs e corrigir eventuais erros.

## 2026-11-20 — Código piloto PNCP (não ativado)

- **Ação:** criar `scripts/pncp_piloto.py` com consulta a propostas abertas, classificação inicial e saída JSON local; atualizar documentação e checkpoints.
- **Fonte:** Swagger oficial da API PNCP.
- **Testes:** apenas inspeção documental; execução real e validação de resposta ainda pendentes.
- **Pendências:** executar, validar filtros, dados e resultados antes de qualquer agendamento.

## 2026-11-20 — Cinco máquinas e opções de execução gratuita

- **Ação:** criar `docs/MAQUINAS.md`; atualizar README, decisões D-007 e checkpoints CP-08.
- **Motivo:** priorizar captação de construtoras de São Bernardo e coletor de obras sem depender do n8n.
- **Pesquisa:** documentação oficial GitHub Actions, Google Apps Script e Cloudflare Workers, com links em MAQUINAS.md.
- **Verificação:** gravação documental no GitHub; nenhuma máquina executada, nenhum lead coletado e nenhum e-mail enviado.
- **Pendências:** validar fontes e armazenamento, implementar pilotos, testar e autorizar ativações.

## 2026-11-20 — Checkpoints e fontes oficiais AVCB/CET/DER

- **Ação:** criação de `docs/CHECKPOINTS.md` com etapas até a automação e primeiras fontes oficiais identificadas.
- **Evidência:** Via Fácil Bombeiros, CET e DER (links no checkpoint).
- **Verificação:** pesquisa documental e registro no GitHub; nenhuma consulta individual por endereço nem coleta automática testada.
- **Pendências:** validar acesso automatizado, cobertura e requisitos de cada fonte; testar protótipo.

## 2026-11-20 — Escopo metalúrgico, AVCB e infraestrutura viária

- **Ação e motivo:** ampliar README e decisões para investigar obras de metalurgia, guarda-corpos rodoviários/padrão CET, AVCB e prospecção comercial.
- **Arquivos afetados:** README.md, docs/DECISOES.md e CHANGELOG.md.
- **Decisões:** D-005 e D-006.
- **Verificação:** alterações documentais gravadas no GitHub; sem teste de coletor ou consulta automática.
- **Pendências:** confirmar fontes oficiais, critérios técnicos e disponibilidade de dados; construir checklist de implementação; aprovar qualquer envio comercial antes da execução.

## 2026-11-20 — Ampliação da estratégia comercial e classificação de oportunidades

- **Ação:** atualização de `README.md`, `docs/DECISOES.md` e deste histórico.
- **Motivo:** registrar a página de vendas de corrimãos para prédios como referência comercial; explicitar o portfólio ampliado e a busca por licitações e obras privadas.
- **Decisão:** D-004, incluindo distinção entre contratação aberta, prospecção e acompanhamento.
- **Verificação:** documentos atualizados no GitHub; não houve execução de coleta, teste de fonte ou automação.
- **Limitação:** conteúdo integral da página de vendas ainda não validado diretamente; capacidade de execução e regiões a confirmar.
- **Pendências:** mapear e testar fontes públicas e privadas; validar termos comerciais e critérios de classificação.

## 2026-11-20 — Estrutura documental inicial

- **Ação:** criação de `README.md`, `CHANGELOG.md` e `docs/DECISOES.md`.
- **Objetivo:** definir escopo comercial, proposta de arquitetura e regra obrigatória de documentação.
- **Verificação:** criação dos arquivos no GitHub; nenhuma execução do radar ou teste de integração.
- **Situação:** planejamento, sem coleta automática ativa neste repositório.
- **Pendências:** validar fontes de dados; confirmar portfólio operacional e regiões; desenhar protótipo; definir testes e mecanismo de verificação documental.

## Modelo para próximos registros

### AAAA-MM-DD — Resumo da mudança

- **Ação e motivo:**
- **Arquivos/sistemas afetados:**
- **Issue/commit/evidência:**
- **Testes e resultados:**
- **Pendências e limitações:**

## 2026-11-20 — Resumo Actions e testes (branch de trabalho)

- **Ação:** classificação direta/indireta/descartada, contagem de duplicidades e resumo Markdown no GitHub Actions; testes simulados sem rede.
- **Arquivos:** `scripts/pncp_piloto.py`, `.github/workflows/teste-pncp.yml`, `tests/test_pncp.py`, documentação.
- **Validação:** alterações gravadas na branch `feature/pncp-actions-summary-tests`; execução de testes e consulta real ainda pendentes de confirmação no Actions.
- **Limites:** uma página no piloto, sem agendamento, histórico ou envio comercial. `linkSistemaOrigem` não é necessariamente link oficial PNCP.

## 2026-11-20 — Relatório legível nos logs

- **Ação:** acrescentada impressão de contagens, oportunidades e erros em texto puro na etapa `Consultar PNCP`, preservando JSON e Job Summary.
- **Escopo:** apenas branch `feature/pncp-actions-summary-tests`; sem alterações na `main`, agendamento ou ampliação de páginas.
- **Validação:** código gravado; nova execução manual ainda pendente.
