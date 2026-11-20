# Registro de decisões — Radar Alfa

Registrar aqui decisões comerciais, técnicas e operacionais relevantes. Cada entrada deve indicar **estado** (proposta, aprovada, substituída), contexto, motivo, alternativas e consequências. Não apresentar propostas como implementações.

## D-001 — Repositório como memória oficial
- **Data:** 2026-11-20
- **Estado:** aprovada para documentação inicial.
- **Decisão:** manter README, histórico de alterações e decisões no próprio repositório. Usar Issues para acompanhar tarefas, não como única memória.
- **Motivo:** permitir auditoria, continuidade entre pessoas e agentes e histórico versionado.
- **Alternativa considerada:** documentar exclusivamente nas Issues.
- **Consequência:** toda alteração exige registro documental antes de ser considerada concluída.

## D-002 — Critério comercial inicial
- **Data:** 2026-11-20
- **Estado:** diretriz comercial informada; detalhes operacionais a validar.
- **Decisão:** priorizar contratos com aproximadamente R$ 60 mil ou mais de escopo potencial para a Alfa, com foco em corrimãos de alumínio e inox para acessibilidade, sem excluir outros produtos e serviços compatíveis, como guarda-corpos e vidros.
- **Motivo:** concentrar esforço comercial em oportunidades de médio e grande porte.
- **Alternativa considerada:** buscar apenas a palavra “corrimão” ou filtrar pelo valor global da obra.
- **Consequência:** registrar “valor a verificar” quando o valor do escopo da Alfa não puder ser confirmado.

## D-003 — Execução e integrações
- **Data:** 2026-11-20
- **Estado:** proposta; não aprovada para implementação.
- **Proposta:** Python para coleta e classificação, GitHub Actions para agendamento e Telegram para alertas; possível integração futura com n8n e Hermes.
- **Motivo:** começar com arquitetura simples, modular e de baixo custo.
- **Alternativas a comparar:** Cloudflare Workers, Google Apps Script e ferramentas autohospedadas.
- **Próximo passo:** validar fontes e limites técnicos antes de decidir.

## D-004 — Referência comercial e descoberta antecipada de obras
- **Data:** 2026-11-20
- **Estado:** diretriz aprovada para o planejamento; integrações ainda não implementadas.
- **Contexto:** a Alfa mantém uma página de vendas específica para anúncios e um site com corrimãos, guarda-corpos, vidro temperado e acessibilidade. O conteúdo do site está sujeito a alterações.
- **Decisão:** usar https://alfacorrimao.com.br/corrimaos-para-predios/ como referência comercial prioritária, complementada pelo site; monitorar licitações e obras privadas, inclusive antes de surgirem pedidos específicos de corrimãos.
- **Motivo:** ampliar a descoberta de contratos compatíveis com o portfólio e o piso comercial.
- **Alternativas:** restringir a busca a editais com a palavra “corrimão” ou somente a licitações públicas.
- **Consequências:** distinguir (a) contratação aberta confirmada, (b) obra para prospecção e (c) acompanhamento. Verificar o valor do escopo da Alfa; não usar automaticamente o valor total da obra. Validar diretamente o conteúdo da página e a capacidade operacional antes de fixar palavras-chave definitivas.

## Modelo de decisão

### D-XXX — Título
- **Data:**
- **Estado:** proposta | aprovada | substituída
- **Contexto:**
- **Decisão:**
- **Motivo e evidências:**
- **Alternativas:**
- **Consequências:**
- **Issue/commit relacionado:**

## D-005 — Busca ampliada e avaliação humana de oportunidades
- **Data:** 2026-11-20
- **Estado:** diretriz comercial aprovada; capacidade e habilitações por contrato sujeitas a análise.
- **Contexto:** responsáveis pela Alfa indicaram trabalhos de metalurgia e oportunidades viárias, inclusive guarda-corpos de rodovias e padrão CET.
- **Decisão:** procurar demandas de ferro, aço inox, alumínio e estruturas metálicas além dos produtos exibidos no site; pesquisar cada objeto, valor, prazo, especificações e potencial comercial antes de encaminhar à Alfa.
- **Motivo:** não perder contratos rentáveis por filtros restritos de palavras-chave.
- **Alternativa:** aceitar apenas serviços nominalmente anunciados no site.
- **Consequência:** decisão final sobre viabilidade técnica, normas, preço e interesse pertence à Alfa; não prometer habilitação ou execução sem análise.

## D-006 — AVCB e prospecção responsável
- **Data:** 2026-11-20
- **Estado:** pesquisa aprovada; nenhuma fonte ou automação validada ainda.
- **Contexto:** investigar demanda por adequações e renovações relacionadas à segurança contra incêndio de edificações.
- **Decisão:** verificar a existência e os limites de consultas oficiais de AVCB/CLCB, dados de fiscalização e fontes de obras; diferenciar ausência de informação, licença vencida e irregularidade comprovada. Estudar vídeo institucional, e-mail e canais de compras como meios de prospecção, sem disparo automático nesta fase.
- **Motivo:** descobrir necessidades reais sem acusar indevidamente proprietários ou empresas.
- **Alternativas:** inferir irregularidade de ausência de dados ou disparar campanhas sem triagem.
- **Consequências:** documentar evidência, data e limites da consulta; avaliar conformidade de contatos e autorizar ações comerciais separadamente.

## D-007 — Máquinas integradas e execução inicial fora do n8n
- **Data:** 2026-11-20
- **Estado:** planejamento aprovado; plataforma de produção e implementação pendentes de teste.
- **Decisão:** documentar cinco máquinas integradas no mesmo Radar Alfa; priorizar Caçador de Construtoras em São Bernardo e piloto de Radar de Obras. Avaliar GitHub Actions/Python como primeira execução independente do n8n; Apps Script para planilhas e rascunhos; Cloudflare Workers para tarefas leves.
- **Motivo:** obter resultados comerciais progressivos com baixo custo e reaproveitar o repositório existente.
- **Alternativas:** aguardar o n8n, criar cinco projetos isolados ou hospedar todas as tarefas em Workers.
- **Consequências:** usar cadastro compartilhado e controle de acesso; manter revisão humana para envio de mensagens; não colocar contatos coletados em repositório público. Ver [docs/MAQUINAS.md](MAQUINAS.md).
