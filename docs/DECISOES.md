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
