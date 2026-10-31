# Proposta de melhorias — cofiex-scorer V.1 BETA

Data: 30/10/2026 (revisão 2, com os comentários do usuário). Escopo: arquitetura e insumos da
skill; produto para o TTL (Task Team Leader) do Banco Mundial no Brasil; refinamento e
calibração da pontuação; aproveitamento dos pleitos de 2023–2024 e das Notas Técnicas do
regime anterior (Resolução COFIEX 17/2021).

**O que mudou na revisão 2.**
- A "probabilidade de aprovação" saiu. Entrou o **direcionamento de sublimite** (seção 3).
- A lente Banco Mundial ganhou uma seção própria e concreta (seção 4).
- O relatório ganhou regras de hierarquia de números e de não repetição (seção 2.1).
- Meta de MAE da Nota Geral: ≤1,0.

---

## 1. Diagnóstico da arquitetura atual

**Como funciona hoje.**
- **SKILL.md (446 linhas):** princípio de julgamento cego, protocolo de recuperação, fases 0
  a 12 e formato de saída.
- **`references/` (~1.300 linhas, 17 arquivos):** regulação, rubrica (Área Estratégica,
  Capacidade de Pagamento, Dívida, Índice de Desenvolvimento Humano e nota final), calibração,
  perguntas do Grupo Técnico, iteração, revisão sênior, plano de correção e saída em .docx.
- **Fichas anonimizadas:** 261 de pleito e 390 de avaliação (121 sob a RN 1/2024, 245 sob a
  Resolução 17/2021 e 24 sem regime), mais o CSV derivado e 17 cartões de setor.
- **Dados objetivos:** uma planilha empacotada (External Credit Operations Database, set/2026).
- **Saídas:** sumário executivo, onze seções e relatório .docx.

**O que já funciona bem.**
- **Erro estável.** O MAE da Nota Geral ficou em 1,44 com n=89, igual ao de n=30, e o viés
  médio é próximo de zero.
- **Componentes objetivos quase sem erro.** Capacidade de Pagamento e Dívida têm MAE de cerca
  de 0,18.
- **Lente de Área Estratégica calibrada.** A lente A.6, a rota para Área Estratégica máxima e
  os critérios por nível e por objetivo do PPA vêm de 1.021 justificativas de Notas Técnicas.
- **Julgamento cego protegido.** Há cartões de setor com n<5 ocultos e um ambiente de teste
  cego que funciona de novo.

**Limitações encontradas.**

| # | Limitação | Evidência | Efeito |
|---|---|---|---|
| L1 | A Área Estratégica concentra o erro | MAE de 1,29 na Área Estratégica, contra ~0,18 em Capacidade de Pagamento e Dívida | A faixa de Nota Geral fica larga (o exemplo testado foi de 5,8 a 14,3) |
| L2 | A fatia do orçamento por área é estimada "de olho" | É a variável que mais separa os níveis (30% para B, ~67% para A), mas não há passo determinístico para calculá-la | Nível errado na área principal custa de 1 a 2 pontos |
| L3 | Tendência da Dívida sem fonte empacotada | A planilha não traz Dívida Consolidada sobre Receita Corrente Líquida | O item vira sempre um cenário (0,50 a 1,00) |
| L4 | Capacidade de Pagamento estadual sem ciclo | Só há a coluna "Fiscal Rating 2026", descrita como "equivalente" | Divergência possível na reunião-alvo |
| L5 | Âncora do Índice de Desenvolvimento Humano | Viés de −0,29 no teste cego; o piso da reunião é uma âncora fixa | Subestimação sistemática |
| L6 | A skill não usa os dados de sublimite que já existem | A base consolidada (165ª–189ª) traz limites por reunião, utilização oficial e resultado por categoria, mas a skill trabalha com regras fixas e multiplicadores de probabilidade | O conselho de momento e sublimite é genérico |
| L7 | Quase nada específico do Banco Mundial | O BIRD financia 29% dos pleitos das fichas (76 de 261), mas a skill não trata dos instrumentos IPF/PforR/DPF, do Marco Ambiental e Social, do Country Partnership Framework nem do Project Concept Note | O produto não conversa com o ciclo de projeto do Banco |
| L8 | O conhecimento do regime anterior é subutilizado | 295 Notas Técnicas com a "análise técnica" pontuada item a item ficam fora da calibração | A revisão sênior (A.1–A.5) é calibrada por impressão, não por nota oficial |
| L9 | Âncoras em conflito sem regra de precedência | Por exemplo, justiça com cerca de 8,0 contra a salvaguarda de 6,0 a 7,5 | O executor escolhe arbitrariamente |
| L10 | Fases interativas travam execuções delegadas | As fases 1 e 9.5 perguntam ao usuário | A execução em lote fica sem padrão definido |
| L11 | Idiomas misturados nas fichas | As narrativas estão em inglês e a saída é em português | Custo de tradução e risco de termos inconsistentes |
| L12 | Relatório com números demais e repetição | A mesma nota e a mesma lacuna aparecem no sumário, na rubrica, na revisão sênior e no plano de correção, com faixas, taxas e multiplicadores | O TTL não sabe qual número levar para a reunião |

---

## 2. Produto mais útil para o TTL do Banco Mundial no Brasil

O TTL usa a ferramenta em três momentos: (a) **antes da submissão**, para orientar o cliente
na redação da carta-consulta; (b) **na fila da COFIEX**, para escolher sublimite e reunião;
(c) **na preparação**, para levar os achados ao Project Concept Note e ao documento de
avaliação do projeto.

### 2.1 Regras de redação do relatório (valem para todas as propostas abaixo)

**Um número em destaque.** O relatório tem um só número principal: a **Nota Geral esperada**,
com a Nota de Área Estratégica logo abaixo. Todo outro número fica em segundo plano e precisa
de uma frase que diga quando ele importa. Exemplos:
- faixa mínima e máxima: "a nota cai para X se a área principal for lida como C";
- teto de sublimite: "a nota só decide se houver disputa no sublimite Geral";
- dados objetivos: "valor oficial, não muda com a redação da carta".

**Sem previsões paralelas.** Nada de probabilidade de aprovação, multiplicadores ou taxas de
desfecho como números de primeiro plano. A circunstância de aprovação aparece como leitura do
sublimite (seção 3), em texto curto.

**Cada seção traz uma informação nova, com um papel só:**

| Seção | Papel único | O que não repete |
|---|---|---|
| Resumo do TTL | Nota esperada, sublimite recomendado, 3 ações | Não detalha justificativas |
| Pontuação pela rubrica | Por que cada item recebeu a nota | Não propõe correções |
| Revisão sênior e lente Banco Mundial | Qualidade do projeto, do ponto de vista de um banco | Não volta a pontuar áreas |
| Plano de correção | O que mudar, onde e quanto vale | Cita a lacuna por referência ("ver A.5"), sem reexplicar |
| Sublimite e momento | Onde e quando submeter | Não repete a nota, só a posição frente à linha de corte |

Um achado aparece uma vez, na seção que é dona dele. As outras seções fazem referência a ele.
O gerador .docx passa a checar parágrafos quase iguais entre seções e alerta antes de entregar.

### 2.2 Propostas

| # | Melhoria | O que entrega | Esforço |
|---|---|---|---|
| T1 | **Resumo do TTL (1–2 páginas, no início do .docx)** | Veredito em uma linha. Nota Geral esperada em destaque, sublimite recomendado, as 3 lacunas que mais custam nota e as 3 ações de maior ganho. Opção bilíngue português/inglês para circular na equipe. | P |
| T2 | **Carta de comentários ao cliente, por seção do Anexo I** | Tabela "seção do formulário → problema → redação sugerida", pronta para enviar ao mutuário. Substitui o plano de correção na versão para o cliente, sem duplicá-lo no relatório interno. | M |
| T3 | **Lente Banco Mundial** | Ver seção 4. | M |
| T4 | **Justificativa do credor** | Texto-modelo e checklist da justificativa "por que BIRD" aceita pela SEAID (44% das Notas do regime anterior deram nota cheia no item 1.5). Comparativo de custo e prazo com outros credores a partir da planilha (Loans_Master/Banks). | P |
| T5 | **Painel de carteira** | Página com os pleitos que o TTL acompanha: nota esperada, sublimite recomendado, saldo do sublimite, fase no Portal e próxima reunião. Atualizada pela skill a cada simulação. | M |
| T6 | **Modo "pré-carta" (rascunho incompleto)** | Aceitar nota conceitual ou rascunho parcial e devolver as lacunas que impedem pontuar. Integrar com a skill cofiex-pleito-builder: o scorer diagnostica e o builder redige. | M |
| T7 | **Planilha de custo por área e produto** | Planilha anexa (.xlsx) com cada produto, valor, área do PPA "dona" e % do total. É o insumo que mais move a nota (L2), e o cliente pode preenchê-la diretamente. | P |

---

## 3. Direcionamento de sublimite (substitui a "probabilidade de aprovação")

**Por quê.** A aprovação depende sobretudo do sublimite escolhido e do saldo dele na reunião.
A nota decide apenas dentro de um sublimite disputado. A base consolidada (165ª–189ª) mostra:

| Sublimite | Pleitos | Aprovados (inclui parciais) | Menor nota aprovada | Uso típico do limite na reunião |
|---|---|---|---|---|
| Subnacional – Geral | 325 | 39% | 6,20 | **96% a 175%**: saturado em quase toda reunião |
| Subnacional – Ambiental e Climático | 22 | 68% | 6,87 | 20% a 98%: muitas vezes sobra saldo |
| Subnacional – PPP | 15 | 73% | 5,37 | 19% a 100%: sobra saldo na maior parte das reuniões |
| Subnacional – Fiscal | 13 | 54% | 9,65 | 21% a 100% |
| Subnacional – Reestruturação de Dívidas | 15 | 87% | 5,61 | sem limite divulgado |
| Subnacional – Operações em R$ | 8 | 88% | 7,41 | 96% a 98% |

**No sublimite Geral, a linha de corte subiu muito.**
- Até a 184ª reunião, a menor nota aprovada ficava entre 6,2 e 7,6.
- Nas reuniões de 2026, ficou entre 10,3 e 11,9. Na 185ª, nenhum pleito do Geral foi
  aprovado, mesmo com nota 11,9.
- A 191ª reunião (prevista para 03/12/2026) divulga US$ 272 milhões no Geral e saldo zero
  em PPP e Ambiental e Climático.

Ou seja: a mesma nota pode aprovar num sublimite e não aprovar em outro. Mudar de sublimite
vale mais que ganhar 1 ponto de nota.

**O que o módulo entrega (texto curto, sem probabilidade em percentual):**
1. **Elegibilidade por sublimite.** Para cada sublimite, um "sim / não / sim, se..." pelos
   critérios da norma. Exemplos:
   - Ambiental e Climático exige recursos integralmente ambientais ou climáticos (deliberação
     da 170ª).
   - PPP exige contraprestação com indicadores de nível de serviço (pergunta 28 do Grupo
     Técnico).
   - Fiscal, Programa de Equilíbrio Fiscal e Regime de Recuperação Fiscal dependem da situação
     fiscal do ente.
2. **Saldo e linha de corte.** Saldo divulgado para a próxima reunião, linha de corte recente
   do sublimite e posição do pleito: acima da linha, perto dela ou abaixo.
3. **Recomendação.** O melhor sublimite e a melhor reunião, e o que mudar no desenho para
   ficar elegível no sublimite menos disputado. Por exemplo: separar um componente climático
   numa operação própria, ou reduzir o valor para caber no saldo.

**Como implementar.**
- Empacotar na skill uma tabela anonimizada, gerada da base consolidada. Por sublimite e
  reunião: limite, valor aprovado, número de aprovados, menor nota aprovada e maior nota não
  aprovada. São dados agregados de reunião, não de pleito.
- Script `tools/build_sublimit_table.py` para atualizar a tabela a cada reunião.
- Novo arquivo `references/strategy/sublimit-targeting.md` com as regras de elegibilidade.
- Remover de `rubric/final-score.md` os multiplicadores de probabilidade (×0,9, ×1,15 etc.),
  porque o módulo novo os substitui.

---

## 4. Como incorporar o Banco Mundial (detalhe de T3)

Novo arquivo `references/review/world-bank-lens.md`, **aplicado sempre**, qualquer que seja o
credor declarado (o TTL avalia também pleitos que podem migrar para o BIRD). Cada bloco gera
uma informação que nenhuma outra seção traz:

| Elemento | O que a skill faz com a carta | Saída no relatório | Fonte a empacotar |
|---|---|---|---|
| **Instrumento** (IPF, PforR, DPF) | Lê o desenho e indica o instrumento coerente. PforR quando há programa de governo com resultados verificáveis. DPF quando o objeto é reforma de política ou fiscal. IPF nos demais casos. Aponta conflito entre o instrumento declarado e o desenho, por exemplo PforR sem indicadores que possam virar DLI. | Uma linha: instrumento sugerido e o porquê | Resumo das políticas operacionais (OP 10.00, PforR, DPF) |
| **DLIs** (se PforR) | Seleciona 3 a 5 indicadores da carta que podem virar indicadores vinculados a desembolso, com protocolo de verificação. | Tabela curta: indicador → DLI → como verificar | Guia de DLIs do PforR |
| **Padrões Ambientais e Sociais** (ESS 1–10) | Pelo tipo de obra e pelo público, marca os padrões acionados: reassentamento (ESS5), povos indígenas e comunidades tradicionais (ESS7), patrimônio cultural (ESS8), segurança de barragens etc. Estima a classe de risco (alto, substancial, moderado, baixo). | Lista dos padrões acionados e classe de risco provável | Tabela "tipo de intervenção → padrões típicos", anonimizada a partir do corpus |
| **Country Partnership Framework** | Verifica se o objetivo do projeto se encaixa num objetivo do quadro de parceria vigente com o Brasil. | Uma linha: objetivo do quadro atendido, ou ausência de encaixe | Objetivos do quadro de parceria vigente (documento público) |
| **PDO e indicadores PDO** | Reescreve o objetivo geral da carta no formato de objetivo do projeto e escolhe 3 a 5 indicadores de resultado já presentes na carta. | Rascunho pronto para o Project Concept Note | Regras de redação do objetivo e dos indicadores |
| **Ponte para o Project Concept Note** | Mapeia as seções da carta para as do Project Concept Note e mostra o que falta escrever. | Tabela "seção do Project Concept Note → onde está na carta → lacuna" | Estrutura padrão do Project Concept Note |

**Por que é útil para a nota COFIEX.** Os pontos que o Banco exige na preparação são os mesmos
que a SEAID critica: arranjo institucional, sustentabilidade e indicadores. A lente Banco
Mundial não pontua de novo. Ela converte essas lacunas no vocabulário do Banco e diz em que
documento cada uma será cobrada.

**Cuidados.** A classe de risco e o instrumento são sugestões para a equipe do Banco, não
decisões. As fontes do Banco ficam com data e versão, porque mudam.

---

## 5. Refinamento e calibração da pontuação

### 5.1 Insumos determinísticos (atacam L2–L5)
| # | Melhoria | Como | Ganho esperado |
|---|---|---|---|
| C1 | **Passo obrigatório "orçamento por área"** antes de classificar níveis | Extrair o valor de cada componente e produto, atribuir cada produto a uma única área "dona" (repartição linear quando a carta não diz) e calcular o %. Aplicar os limiares das Notas Técnicas: ≥~67% para A, >30% para B, ~30% para C, 4–12% para D. Um script em `scripts/` torna o cálculo reprodutível e alimenta a planilha T7. | Menor MAE da Área Estratégica; é a variável de maior peso |
| C2 | **Base de Dívida empacotada** | Tabela de Dívida Consolidada sobre Receita Corrente Líquida por estado e capital (RGF/Siconfi, último quadrimestre), com data. Fórmula da rubrica aplicada automaticamente. | A Tendência da Dívida deixa de ser cenário |
| C3 | **Capacidade de Pagamento estadual por ciclo** | Tabela com a classificação da STN em cada ciclo (2024, 2025, 2026). O ciclo é escolhido pela data da reunião-alvo. | Fecha L4 |
| C4 | **Piso de Índice de Desenvolvimento Humano por reunião** | Tirar da base consolidada o menor IDH real de cada reunião e usar a distribuição empírica no lugar da âncora fixa de 0,668. | Corrige o viés de −0,29 |

### 5.2 Calibração da Área Estratégica (ataca L1)
| # | Melhoria | Como |
|---|---|---|
| C5 | **Calibrar por área, não pelo total** | Medir a acurácia de nível por área com os 1.021 rótulos das Notas Técnicas e montar uma matriz de confusão (A–E e zero). Reportar "acerto de nível" além do MAE. |
| C6 | **Banco de teste fixo e regressão automática** | Congelar ~40 pleitos de validação, estratificados por setor, ente e credor. Rodar sempre no ambiente cego (`tools/make_blind_sandbox.py`) e comparar MAE, viés e acerto de nível a cada mudança da skill, com um runner único. |
| C7 | **Regra de precedência entre âncoras** | Ordem explícita: (1) rubrica e lente A.6 aplicadas ao orçamento calculado em C1; (2) critérios por objetivo do PPA; (3) cartão de setor (só faixa, n≥5); (4) achados transversais. Uma âncora setorial nunca sobrepõe a rubrica aplicada aos números da carta. |
| C8 | **Correções por modalidade com n crescente** | Monitorar os vieses já vistos, como reestruturação de dívida (+2,1, n=6) e fundos de repasse (sobre-estimação). Virar desconto numérico só com n≥10. |
| C9 | **Valores padrão para execução delegada** | Sem usuário disponível: fase 1 preenchida pelo arquivo, fase 9.5 com "reenvio desconhecido" e a próxima reunião ordinária como reunião-alvo. Os padrões usados ficam registrados no relatório. |
| C10 | **Intervalo calibrado** | Calcular a faixa pelos erros observados no banco de teste (ex.: ±1,0 em torno da nota esperada), e não pela soma dos extremos de cada item. No relatório, ela aparece como uma frase de segundo plano (seção 2.1). |

---

## 6. Aproveitamento dos pleitos de 2023–2024 e das Notas Técnicas do regime anterior

**O que existe.**
- **Cartas-consulta 2023–2024:** 205 pastas, com versões, em
  `Pleitos_Textos_MD/Pleitos_2023_2024`.
- **Notas Técnicas parte 1:** 582 arquivos das reuniões 165ª–180ª. As Notas Técnicas da SEAID
  sob a Resolução 17/2021 estão na faixa 168ª–178ª.
- **Fichas da skill:** já cobrem a maior parte desses pleitos (245 avaliações do regime
  anterior). Guardam só totais e uma narrativa, e o total do regime anterior não é comparável
  ao da RN 1/2024.

**O ativo mais valioso ainda não usado é a "análise técnica" pontuada item a item.** No regime
anterior, a SEAID dava nota oficial à qualidade da carta-consulta, com subitens 0/1 e uma
"Qualidade do Requisito" de 1 a 5. São 295 Notas Técnicas com esses itens:

| Item da análise técnica (Resolução 17/2021) | n | Média (% do máximo) | Abaixo de 70% | Item da revisão sênior equivalente |
|---|---|---|---|---|
| 1.1 Justificativa: coerência problema → solução → resultado | 284 | 92% | 3% | A.1 Teoria da Mudança |
| 1.2 Objetivos, componentes e produtos alinhados | 291 | 91% | 3% | A.1 / lente A.6 |
| 1.3 Coerência dos indicadores com os resultados | 176 | 82% | 15% | A.2 Marco de Resultados |
| 1.4 Prazo de desembolso e cronograma | 282 | 90% | 7% | A.4 Implementação |
| 1.5 Justificativa do financiamento externo e do credor | 286 | 91% (44% com nota cheia) | 7% | T4 |
| 2.1 Arranjo institucional e matriz de responsabilidades | 287 | 85% | 22% | A.4 Implementação |
| 2.2 Operação, manutenção e sustentabilidade financeira pós-projeto | 293 | **72%** | **42%** | A.5 Sustentabilidade |
| 2.3 Compatibilidade com as políticas do proponente | 283 | 91% | 7% | lente A.6 (objetivo geral) |

**Propostas de uso (todas anonimizadas, como padrões, nunca como casos):**

| # | Uso | Produto na skill |
|---|---|---|
| K1 | **Calibrar a revisão sênior com nota oficial** | Mapear cada subitem 0/1 e a "Qualidade do Requisito" (1–5) para FORTE/ADEQUADO/FRACO/AUSENTE e registrar as frases típicas de cada nível. Novo arquivo `calibration/technical-quality-r17.md`. |
| K2 | **Nota auxiliar "Qualidade técnica da carta"** | Diagnóstico interno que alimenta a revisão sênior e as perguntas do Grupo Técnico. Seguindo a seção 2.1, não aparece como número no resumo do TTL. |
| K3 | **Biblioteca de indicadores por setor com o veredito da Nota Técnica** | Indicadores aprovados e criticados por setor, com fórmula. Alimenta a tarefa R6 do plano de correção, os indicadores PDO da lente Banco Mundial e a skill cofiex-pleito-builder. |
| K4 | **Textos-modelo dos itens que mais perdem nota** | Para 2.2, 2.1 e 1.5, as estruturas que tiveram nota cheia: tabelas plurianuais de custo operacional com fonte, matriz de responsabilidades, comparativo de condições financeiras. |
| K5 | **Correspondência entre os itens estratégicos antigos (1.1–1.15) e os objetivos do PPA** | Amplia as taxas-base dos objetivos com n pequeno, como sinal fraco e só como faixa. |
| K6 | **Evolução entre versões da carta** | Mostra o que a SEAID pediu antes da reunião e complementa os 39 pares de reenvio. |
| K7 | **Pleitos que cruzaram regimes** | Testa se a qualidade técnica antiga prevê a Área Estratégica sob a RN 1/2024. |
| K8 | **Perguntas e condicionantes da STN e do Grupo Técnico** | Amplia a frequência calibrada em `gtec/questions.md`. |

**Cuidados.** As escalas dos dois regimes são diferentes. Não misturar totais nem usar notas
antigas como gabarito da RN 1/2024. Manter a anonimização e a regra de n<5.

---

## 7. Sequência recomendada

| Ordem | Pacote | Itens | Por quê nessa posição |
|---|---|---|---|
| 1 | **Fundamentos de calibração** | C6, C1, C7, C5, C10 | Sem banco de teste não dá para provar ganho. C1 ataca a maior fonte de erro. |
| 2 | **Dados objetivos** | C2, C3, C4 | Ganho rápido e mensurável; elimina cenários. |
| 3 | **Conhecimento do regime anterior** | K1, K3, K4 (depois K5–K8) | Calibra a revisão sênior e dá conteúdo ao plano de correção e à lente Banco Mundial. |
| 4 | **Produto para o TTL** | Regras da seção 2.1, T1, T2, T3/seção 4, T4, T7 | Depende de K1, K3 e K4 para ter conteúdo bom. |
| 5 | **Carteira e sublimite** | Seção 3, T5, T6 | Exige a tabela de sublimites atualizada a cada reunião. |

**Metas de calibração** (medidas sempre no banco de teste fixo, em ambiente cego):
- MAE da Nota Geral: de 1,44 para **≤1,0**.
- MAE da Área Estratégica: de 1,29 para **≤1,0**.
- Acerto do nível da área principal: ≥60%.
- Viés do Índice de Desenvolvimento Humano entre −0,1 e +0,1.
