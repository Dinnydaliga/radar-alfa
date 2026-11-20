# Radar Alfa

Projeto de inteligência comercial para identificar e acompanhar oportunidades de fornecimento e instalação de produtos e serviços da **Alfa Corrimão**.

## Objetivo e perfil comercial

Buscar contratos em licitações públicas e obras privadas. A prioridade são serviços de médio e grande porte, com **valor comercial para a Alfa em torno de R$ 60.000 ou mais**. O valor global da obra não substitui o valor potencial dos produtos e serviços da Alfa. Oportunidades próximas ao piso podem ser avaliadas.

Produtos prioritários: corrimãos duplos de parede em alumínio, em duas alturas, e soluções de acessibilidade em aço inox para rampas. Também avaliar guarda-corpos, fechamentos de sacadas, vidros e outros produtos ou serviços **desde que a capacidade de execução da Alfa seja confirmada**.

Quando o valor específico do escopo da Alfa não estiver disponível, registrar **valor a verificar**, sem inventar estimativas.

## Fontes a validar

- Licitações públicas: PNCP, Compras.gov.br e portais estaduais e municipais.
- Mercado privado: construtoras, incorporadoras, obras em andamento e fontes públicas de projetos e contratações.

A inclusão de uma fonte na lista não significa que sua integração já funciona. Validar acesso, confiabilidade, cobertura e termos de uso antes de automatizar.

## Funcionamento planejado

1. Coletar oportunidades diariamente.
2. Normalizar dados e eliminar duplicações.
3. Classificar por aderência ao portfólio, valor potencial, localização, prazo e estágio.
4. Guardar evidências, links e histórico de mudanças.
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
