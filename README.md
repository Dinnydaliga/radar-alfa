# Radar Alfa

Projeto de inteligência comercial para identificar e acompanhar oportunidades de fornecimento e instalação de produtos e serviços da **Alfa Corrimão**.

## Objetivo e perfil comercial

Buscar contratos em licitações públicas **e** obras privadas, incluindo prospecção antecipada de empreendimentos. A prioridade são serviços de médio e grande porte, com **valor comercial para a Alfa em torno de R$ 60.000 ou mais**. O valor global da obra não substitui o valor potencial dos produtos e serviços da Alfa. Oportunidades próximas ao piso podem ser avaliadas.

Produtos prioritários: corrimãos duplos de parede em alumínio, em duas alturas, e soluções de acessibilidade em aço inox para rampas. Também avaliar guarda-corpos, fechamentos de sacadas, vidro temperado e outros produtos ou serviços **desde que a capacidade de execução da Alfa seja confirmada**.

A referência comercial principal é a página de vendas [Corrimãos para prédios](https://alfacorrimao.com.br/corrimaos-para-predios/). Complementar com as páginas de produtos do [site da Alfa Corrimão](https://alfacorrimao.com.br/). **O site está em ajustes:** não presumir que fotos, textos, portfólio ou condições comerciais sejam definitivos. A página comercial foi informada pela responsável; seu conteúdo integral ainda precisa ser validado diretamente antes de extrair termos específicos dela.

Quando o valor específico do escopo da Alfa não estiver disponível, registrar **valor a verificar**, sem inventar estimativas.

## Fontes a validar

- **Licitações públicas:** PNCP, Compras.gov.br e portais estaduais e municipais.
- **Mercado privado:** construtoras, incorporadoras, empreendimentos em construção, anúncios de obras, fontes públicas de projetos e contratações, e canais de compras de empresas.

Buscar tanto contratações específicas dos produtos quanto obras maiores que possam precisar deles no futuro. Não confundir **licitação ou contratação aberta e confirmada**, **obra identificada para prospecção** e **oportunidade em acompanhamento**. Uma obra em andamento não prova que a compra dos produtos está aberta.

A inclusão de uma fonte na lista não significa que sua integração já funciona. Validar acesso, confiabilidade, cobertura e termos de uso antes de automatizar.

## Funcionamento planejado

1. Coletar oportunidades diariamente em fontes públicas e privadas validadas.
2. Normalizar dados e eliminar duplicações.
3. Classificar por aderência ao portfólio, valor potencial para a Alfa, localização, prazo e estágio.
4. Separar oportunidades confirmadas, prospecções e acompanhamentos; guardar evidências, links e histórico de mudanças.
5. Enviar alertas objetivos por Telegram e permitir execução manual.

Tecnologias **propostas, não implementadas**: Python e GitHub Actions; integrações futuras possíveis com n8n e Hermes. Credenciais devem ficar em GitHub Secrets ou mecanismo equivalente, nunca no código ou na documentação.

## Organização do trabalho

- `README.md`: orientação e regras do projeto.
- `CHANGELOG.md`: registro cronológico de alterações e verificações.
- `docs/DECISOES.md`: decisões relevantes, justificativas e alternativas.
- Issues: planejamento, tarefas, incidentes e acompanhamento, com links para commits e documentos.

Novas pastas de código, configurações, testes e resultados serão definidas quando necessárias, evitando estrutura vazia.

## Regra obrigatória: entrou, leu, fez, registrou

**Nenhuma atividade que altere o projeto é considerada concluída sem documentação correspondente.** Vale para pessoas, agentes de IA e automações.

Antes de agir, ler este README e a documentação pertinente. Depois de qualquer criação, modificação, correção ou configuração:

1. Atualizar `CHANGELOG.md` com data, ação realizada, arquivos ou sistemas afetados, testes, resultado e pendências.
2. Atualizar a documentação funcional ou técnica afetada.
3. Registrar em `docs/DECISOES.md` toda decisão relevante, com motivo e alternativas consideradas.
4. Vincular a Issue, quando houver, e apontar o commit ou outra evidência.
5. Declarar explicitamente o que **não foi** testado ou confirmado.

Pesquisas exploratórias sem alteração também devem ser registradas quando produzirem uma conclusão aproveitável para o projeto. Não registrar segredos ou dados pessoais desnecessários.

Uma futura checagem em GitHub Actions e regras de proteção de branch **poderão** exigir os registros nos pull requests; essas proteções ainda não foram configuradas.

## Qualidade e limites

Não inventar editais, valores, prazos, requisitos ou compatibilidade. Distinguir informação confirmada, estimativa e hipótese; citar fontes oficiais quando disponíveis. Não anunciar uma oportunidade como aberta sem verificar sua situação e data. Evitar resultados repetidos. Não modificar outros repositórios, nem ativar serviços ou publicar integrações, sem autorização específica.

## Situação atual

**Fase: documentação e planejamento.** Este repositório ainda não contém um radar implementado nem uma rotina diária ativa no GitHub. O próximo trabalho é mapear e testar fontes reais, antes de escrever o coletor.

## Ampliação comercial: metalurgia, AVCB e infraestrutura viária

Diretriz informada pela responsável: o radar deve buscar também serviços de fabricação, instalação e reforma em ferro, aço inox, alumínio e estruturas metálicas, além do catálogo tradicional. Incluir guarda-corpos rodoviários e padrão CET, passarelas, hospitais, prédios públicos, shopping centers, SESI/SENAI e reformas relacionadas a segurança e acessibilidade. Não descartar automaticamente uma oportunidade por não constar no site: investigar requisitos, escopo, preço, localização, prazo e potencial de margem, e encaminhar para avaliação comercial e técnica da Alfa. Não presumir que a Alfa esteja habilitada para todo tipo de serviço ou norma específica.

**AVCB/CLCB:** estudar se consultas oficiais permitem verificar a situação documental de edificações e como identificar demandas de regularização, renovação ou adequação. Ausência de registro público **não prova** irregularidade. Não classificar empresas como infratoras sem evidência oficial inequívoca. Distinguir consulta de autenticidade, situação de licença e eventuais autos de fiscalização, que podem ter disponibilidades diferentes.

**Prospecção:** avaliar apresentação institucional, vídeo, e-mail comercial e contatos profissionais de compras, respeitando privacidade, regras de comunicação e preferência dos destinatários. O radar deve apoiar o contato comercial humano, não enviar campanhas automaticamente sem aprovação.

**Campos desejados por oportunidade:** fonte e data, contratante, responsável pela obra, local, fase, objeto, documentos e requisitos, valor anunciado, valor potencial para a Alfa (ou “a verificar”), prazo, evidência, contato comercial público, classificação e próximo passo.

## Máquinas de captação e execução incremental

Planejadas cinco frentes integradas: Radar de Obras, Caçador de Construtoras, Radar AVCB, Prospecção Comercial e Gestor de Leads. O objetivo é gerar clientes empresariais e contratos lucrativos; começar com piloto de construtoras de São Bernardo e um coletor oficial de obras, sem esperar pelo n8n. Consultar [docs/MAQUINAS.md](docs/MAQUINAS.md) para responsabilidades, prioridades, opções gratuitas e limites. **Nenhuma máquina está ativa.** Dados de leads e contatos não devem ser publicados no repositório público.

## Piloto executável PNCP

Arquivo: `scripts/pncp_piloto.py`. Executar manualmente com `python scripts/pncp_piloto.py --uf SP --paginas 2`. Consulta propostas com prazo aberto, filtra descrições e gera `resultado-pncp.json` local, sem enviar mensagens nem agendar. **Código ainda não executado nem validado contra resposta real da API.** Não publicar resultados com dados de contato no repositório público.

## Teste no GitHub Actions

Workflow manual: `.github/workflows/teste-pncp.yml`. No GitHub, abrir **Actions → Teste manual Radar Alfa PNCP → Run workflow**. Ele confere a sintaxe, executa o piloto e, em caso de sucesso, disponibiliza o arquivo JSON como artefato por três dias. **Não há agendamento, envio comercial ou execução confirmada**. A primeira execução pode revelar necessidade de ajustes nos parâmetros da API PNCP.

## Diagnóstico PNCP — 2026-11-20

Três execuções manuais relatadas falharam em `Consultar PNCP` por `The read operation timed out` após 25 segundos; configuração e sintaxe passaram. O piloto agora limita o teste a **uma página**, tenta novamente uma vez em erros transitórios, registra tempo e tipo de erro e grava `resultado-pncp.json` mesmo se falhar. O workflow publica o artefato também em caso de falha. **Correção gravada, mas ainda não executada**; endpoint e disponibilidade da API permanecem sujeitos à validação real. Sem agendamento.

## Resumo de execução em teste (branch de trabalho)

Na branch `feature/pncp-actions-summary-tests`, o workflow manual foi adaptado para gerar resumo Markdown no painel da execução do GitHub Actions, com totais por classificação, duplicidades, erros e candidatos. O JSON continua como artefato temporário. A consulta continua limitada a uma página de 10 registros, sem agendamento. O link de origem pode apontar para sistema externo e não equivale a link oficial do PNCP. Os testes simulados são executados antes da consulta real; validação no Actions ainda pendente.
