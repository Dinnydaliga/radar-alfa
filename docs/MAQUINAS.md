# Máquinas de captação — Radar Alfa

**Data:** 2026-11-20. **Status:** arquitetura proposta, com prioridade de implementação rápida. Nenhuma máquina foi implementada ou ativada.

**Objetivo comum:** conquistar clientes empresariais, obras relevantes e contratos lucrativos para a Alfa Corrimão. Evitar cinco sistemas isolados: compartilhar cadastro de empresas, oportunidades, evidências, histórico e revisão humana.

## M-01 — Radar de Obras
- Descobrir editais, contratos adjudicados, obras públicas, obras privadas, reformas, infraestrutura viária e oportunidades de subcontratação.
- Prioridade: primeiro coletor de fonte oficial estruturada, testado antes de agendar.
- Execução candidata: Python no GitHub Actions, independente do n8n.

## M-02 — Caçador de Construtoras
- Começar por São Bernardo do Campo; depois ampliar geograficamente.
- Localizar construtoras/incorporadoras, sites oficiais, contatos comerciais ou de compras publicamente divulgados, obras relevantes e evidência da origem.
- Não inventar e-mails, não coletar dados pessoais desnecessários e respeitar regras de acesso aos sites.
- Execução candidata: Python no GitHub Actions; Google Apps Script como alternativa para planilhas.

## M-03 — Radar AVCB
- Estudar licenças e sinais públicos de demandas por adequação e renovação.
- Via Fácil tem consulta pública, mas não há API oficial gratuita em massa confirmada; CAPTCHA e ausência de cadastro completo impedem assumir automação viável.
- Manter como investigação/manual até validar fonte autorizada; ausência de registro não é prova de irregularidade.

## M-04 — Prospecção Comercial
- Gerar dossiês, apresentações, rascunhos de e-mails e propostas de contato direcionadas a compras/engenharia.
- Envio somente após revisão e autorização; respeitar LGPD, finalidade, minimização de dados e opção de não receber novos contatos.
- Execução candidata: Apps Script para rascunhos/planilhas, ou n8n quando operacional; não ativar disparos.

## M-05 — Gestor de Leads
- Guardar estágio, responsável, última interação, próxima ação, respostas e resultados comerciais.
- Execução inicial candidata: planilha compartilhada; n8n futuramente para orquestração.

## Plataformas comparadas (documentação oficial consultada em 2026-11-20)
- **GitHub Actions:** executores padrão gratuitos para repositórios públicos; bom para Python agendado e testes versionados. https://docs.github.com/en/actions/concepts/billing-and-usage
- **Google Apps Script:** gatilhos programados e integração com Sheets; execução de até seis minutos por chamada e cotas diárias. https://developers.google.com/apps-script/guides/services/quotas
- **Cloudflare Workers Free:** Cron Triggers e tarefas leves; limites de CPU e requisições, inadequado como escolha automática para coleta pesada. https://developers.cloudflare.com/workers/platform/limits/
- **n8n:** opção de orquestração, não é pré-requisito do primeiro coletor; avaliar instância existente antes de ligar.

## Ordem de entrega proposta
1. **Primeira entrega:** lista piloto de construtoras de São Bernardo com contatos comerciais verificáveis, fontes e indicação de obras.
2. **Em paralelo:** prova de conceito de coleta de licitações/obras de fonte oficial.
3. Padronizar cadastro compartilhado e deduplicação.
4. Gerar rascunhos de abordagem e validar com a Alfa antes de enviar.
5. Adicionar alertas, histórico e métricas.
6. Integrar n8n para coordenação quando estiver operacional.
7. Retomar AVCB em escala somente se surgir fonte autorizada e tecnicamente viável.

**Regra de segurança comercial:** não armazenar base de leads empresariais sensível em repositório público; código e documentação podem ficar no GitHub, dados operacionais em armazenamento com acesso controlado. Nenhuma automação de envio ou coleta foi ativada.
