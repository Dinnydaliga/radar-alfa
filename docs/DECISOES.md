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

## D-008 — Piloto manual PNCP antes de agendamento
- **Data:** 2026-11-20
- **Estado:** piloto de código criado; ativação não aprovada.
- **Decisão:** usar endpoint oficial `/v1/contratacoes/proposta` para buscar propostas abertas em SP; classificar objeto em aderência direta ou obra para prospecção. Limitar páginas, não enviar mensagens e não criar workflow agendado antes de teste real.
- **Motivo:** verificar rapidamente se a fonte gera oportunidades úteis, sem depender do n8n.
- **Alternativas:** começar por scraping de sites privados ou disparos de prospecção.
- **Limitação:** script ainda não executado; resultados, parâmetros e campos precisam de validação. Fonte: https://pncp.gov.br/api/consulta/swagger-ui/index.html

## D-009 — GitHub Actions somente manual para o primeiro teste
- **Data:** 2026-11-20
- **Estado:** configuração criada; execução não confirmada.
- **Decisão:** adicionar workflow com `workflow_dispatch`, sem cron, que verifica sintaxe e executa o piloto PNCP; em sucesso, guarda resultado como artefato temporário.
- **Motivo:** permitir teste pela interface GitHub Actions antes de ativar qualquer rotina.
- **Alternativas:** rodar somente localmente ou ativar agendamento sem validar a API.
- **Limites:** primeiro teste pode falhar por parâmetros da API; não há envio de e-mails nem integração n8n.

## D-010 — Diagnóstico e repetição limitada da API PNCP
- **Data:** 2026-11-20
- **Estado:** correção implementada; validação de execução pendente.
- **Contexto:** três tentativas manuais reportaram timeout na consulta PNCP, com Python e sintaxe aprovados.
- **Decisão:** reduzir piloto a uma página, usar timeout de 18 segundos e no máximo duas tentativas com espera curta; salvar diagnóstico JSON e artefato mesmo se a consulta falhar.
- **Motivo:** separar indisponibilidade da fonte de falhas locais e preservar evidências sem execuções indefinidas.
- **Alternativa:** aumentar indiscriminadamente o timeout ou agendar sem validação.
- **Consequência:** uma nova execução manual é necessária; não há garantia de resposta da API nem rotina diária ativa.

## D-011 — Resumo no Actions e testes sem ampliar a coleta
- **Data:** 2026-11-20
- **Estado:** implementação em branch para validação, sem integração à main.
- **Decisão:** preservar a consulta manual de uma página e os filtros comerciais existentes; contar descartadas e duplicidades, exibir resumo no Actions e testar com respostas simuladas.
- **Motivo:** leitura pelo celular sem ZIP e diagnóstico claro de erros.
- **Alternativas:** depender de artefatos temporários ou ampliar a paginação antes da validação.
- **Consequência:** cobertura ainda parcial; conferir execução real e revisar resultados antes de merge.

## D-012 — Redução de falsos positivos do piloto PNCP
- **Data:** 2026-11-20
- **Estado:** implementada na branch de testes; validação pendente.
- **Evidência:** execução `44808205837` leu 2.595 registros e gerou 902 candidatos, incluindo merenda escolar sem relação com metalurgia.
- **Decisão:** classificar diretamente apenas termos de produto/serviço específicos; para prospecção indireta exigir construção, reforma ou execução vinculada a obra/edificação; rejeitar compras rotineiras sem indicação específica de metalurgia.
- **Alternativa:** manter termos genéricos isolados como escola, hospital, engenharia e adequação, que geram muitos falsos positivos.
- **Limitação:** filtros heurísticos podem perder oportunidades; precisam de testes e revisão de amostras. Nenhuma integração à main ou agendamento.

### Complemento de validação D-012 — 2026-11-20
- O teste automatizado deve usar exemplos coerentes com a regra: `Reforma` isolada não comprova obra relevante, mas `Reforma de escola` indica prospecção; `Merenda escolar` deve ser descartada. Teste corrigido na branch, pendente de execução no Actions.
