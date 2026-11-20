# Checkpoints — Radar Alfa até a automação

Atualizado em 2026-11-20. Estado geral: planejamento; nenhuma coleta automática implementada.

## CP-01 — Escopo e governança [concluído]
- [x] Repositório e regra “entrou, leu, fez, registrou”.
- [x] Critério comercial inicial: aproximadamente R$ 60 mil de escopo potencial para a Alfa; oportunidades menores ou sem valor podem ser avaliadas.
- [x] Abrangência: corrimãos, guarda-corpos, vidros, ferro, inox, alumínio, estruturas metálicas, infraestrutura viária e adequações prediais.
- [x] Decisão comercial e técnica final reservada à Alfa.

## CP-02 — Mapa de fontes [em andamento]
- [x] Identificar fontes candidatas públicas e privadas.
- [x] Localizar consulta pública de licenças por endereço no Via Fácil Bombeiros.
- [x] Localizar compras da CET, padrões técnicos do DER e exemplo de edital de passarela.
- [ ] Testar consulta por endereço no Via Fácil: entradas, resultados, datas, limitações e eventuais barreiras de automação.
- [ ] Verificar disponibilidade legal e técnica de dados em lote de AVCB/CLCB e processos de fiscalização.
- [ ] Mapear CET, DER, concessionárias, ARTESP, prefeituras, PNCP, contratos adjudicados e empresas vencedoras.
- [ ] Mapear construtoras, administradoras, shoppings, SESI/SENAI, hospitais e canais de compras privados.
- [ ] Classificar cada fonte: gratuita/paga, oficial/terceiros, frequência, cobertura, acesso automatizável e restrições.

## CP-03 — Vocabulário e critérios [pendente]
- [ ] Extrair e validar palavras-chave do site comercial, editais reais e padrões técnicos.
- [ ] Definir sinônimos, termos de exclusão e buscas por obras grandes sem citar o produto.
- [ ] Definir classificação: edital aberto confirmado, pedido de cotação, obra para prospecção, acompanhamento, licença consultada e situação não confirmada.
- [ ] Separar valor global da obra, valor anunciado do item e valor potencial para a Alfa.

## CP-04 — Prova de conceito [pendente]
- [ ] Selecionar duas ou três fontes viáveis, testar manualmente e guardar exemplos reais.
- [ ] Definir esquema de dados com URL, data, empresa, localização, escopo, valor, prazo, evidências e status.
- [ ] Validar deduplicação, relevância e limites de uso; evitar acusações de irregularidade sem comprovação.
- [ ] Revisar exemplos e falsos positivos com a Alfa.

## CP-05 — Arquitetura e implementação [pendente]
- [ ] Comparar Python + GitHub Actions, n8n e alternativas gratuitas considerando custo, limites e manutenção.
- [ ] Aprovar arquitetura antes de programar.
- [ ] Criar coletores, normalização, armazenamento, classificação e histórico.
- [ ] Criar testes, logs, tratamento de erros, reexecução e monitoramento.

## CP-06 — Inteligência e prospecção [pendente]
- [ ] Cruzar obras, vencedores de contratos, empresas responsáveis e canais públicos de compras.
- [ ] Gerar dossiê curto: oportunidade, evidência, motivo de aderência, próximo passo e dúvidas.
- [ ] Preparar materiais de apresentação e rascunhos de contato, com revisão humana e conformidade de privacidade.
- [ ] Não disparar mensagens comerciais automaticamente sem autorização.

## CP-07 — Alertas e operação [pendente]
- [ ] Definir periodicidade, filtros e responsáveis pelos alertas.
- [ ] Integrar Telegram ou outro canal aprovado; testar alertas reais e deduplicação.
- [ ] Executar piloto supervisionado, medir oportunidades úteis, falsos positivos e custo.
- [ ] Aprovar ativação do agendamento; documentar manutenção, contingência e responsável.
- [ ] Considerar integração com n8n/Hermes apenas após validação do núcleo.

## Evidências iniciais da pesquisa (fontes oficiais)
- Via Fácil Bombeiros: https://viafacil2.policiamilitar.sp.gov.br/VFB_WEB/Default.aspx — oferece consultas públicas por endereço e número, e consultas relacionadas à fiscalização.
- CET compras públicas: https://cetsp.com.br/consultas/acesso-a-informacao/compras-publicas.aspx
- CET circulação de pedestres: https://cetsp.com.br/consultas/quadro-de-servicos/circulacao-de-pedestres.aspx
- CET obras em vias / TPOV: https://ssl.cetsp.com.br/consultas/obras-e-servicos-de-infraestrutura-urbana-%28tpov%29.aspx
- DER padrões técnicos: https://dersp.der.sp.gov.br/WebSite/Documentos/Tecnicas.aspx — inclui PP-DE-C04/029, guarda-corpo metálico.
- DER exemplo histórico de recuperação de passarela SP-304: https://www.der.sp.gov.br/Website/Arquivos/dengen/concorrencia902422025.pdf

**Limites:** não foi verificada a automação das consultas, nem demonstrada base completa de imóveis irregulares. Documentos e exemplos não comprovam que uma contratação esteja aberta em 2026-11-20.

## CP-08 — Máquinas de captação [planejado]
- [x] Definir as cinco máquinas e prioridade comercial inicial (ver [MAQUINAS.md](MAQUINAS.md)).
- [x] Comparar preliminarmente GitHub Actions, Apps Script e Cloudflare Workers por documentação oficial.
- [ ] Testar piloto do Caçador de Construtoras em São Bernardo, com evidências de contatos públicos.
- [ ] Testar primeiro coletor oficial de obras em Python.
- [ ] Definir armazenamento privado dos leads, deduplicação e fluxo de revisão comercial.
- [ ] Aprovar e implementar cada fluxo, com testes e registro; ativar n8n apenas quando fizer sentido.

## CP-09 — Piloto PNCP [código criado, teste pendente]
- [x] Criar script de consulta pública PNCP com limite de páginas e filtro inicial.
- [ ] Executar contra API real, verificar campos, paginação, erros e qualidade das oportunidades.
- [ ] Ajustar palavras-chave e revisar exemplos reais com a Alfa.
- [ ] Decidir armazenamento, logs e agendamento somente após testes.

## CP-10 — GitHub Actions manual [configurado; teste pendente]
- [x] Criar `.github/workflows/teste-pncp.yml` com acionamento exclusivamente manual.
- [ ] Executar pela aba Actions e conferir logs e artefato.
- [ ] Corrigir eventuais erros de parâmetros/API e avaliar candidatos reais.
- [ ] Aprovar agendamento somente depois de piloto útil.

## CP-11 — Timeout PNCP [correção gravada, reteste pendente]
- [x] Analisar capturas: três falhas em consulta PNCP por tempo esgotado; sintaxe aprovada.
- [x] Adicionar duas tentativas, tempo controlado, logs e arquivo JSON de diagnóstico mesmo em falha.
- [x] Publicar artefato de diagnóstico também quando a etapa falhar.
- [ ] Rodar novamente o workflow manual, conferir o artefato e validar resposta da API.
- [ ] Se persistir timeout, avaliar endpoint alternativo/fonte antes de ativar qualquer agendamento.
