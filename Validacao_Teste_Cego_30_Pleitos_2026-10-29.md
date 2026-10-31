# Validação por teste cego — 30 pleitos reais (2025–2026), skill cofiex-scorer V.1 BETA

Data: 2026-10-29. Metodologia: 30 cartas-consulta reais de `Cartas-Consultas/Pleitos_Textos_MD/Pleitos_2025_2026`
(última revisão de cada), avaliadas por 6 subagentes em paralelo, cada um seguindo a metodologia completa
da skill (SKILL.md + references/) **sem acesso a**: Notas Técnicas, `Resultados_Cofiex_md`,
`COFIEX_Base_Consolidada_165_189_PT.xlsx`, nem busca web pelo desfecho real — julgamento cego preservado em
todos os 30 casos (confirmado nas notas metodológicas de cada subagente).

Depois da pontuação cega, cruzei com o resultado oficial na base consolidada (reuniões 165ª–189ª, chave
N° PFE/Processo SEI). Amostra balanceada: 17 Aprovado, 10 Não aprovado, 3 Aprovado parcialmente — de 89
pleitos únicos com nota oficial disponível, de 118 pleitos únicos no total na pasta.

**Esta é uma amostra pequena (n=30) de uma avaliação de validação, não uma recalibração estatística — os
achados abaixo apontam onde investigar, não são conclusivos por si.**

## Resultado agregado

- **MAE (erro médio absoluto) da Nota Geral esperada vs. oficial: 1,43 pontos** (numa escala 0–15 → 9,6%).
- **Viés médio: -0,23** (leve subestimação, não sistemática — a maioria dos erros grandes vai nos dois
  sentidos, não um bias direcional dominante).
- **Mediana do erro absoluto: 1,00 ponto** — ou seja, metade dos 30 casos ficou a 1 ponto ou menos da
  nota oficial.

## Achado principal: nota não discrimina aprovação (reconfirmado com n maior)

| Resultado oficial | n | Nota oficial média | Min | Max |
|---|---|---|---|---|
| Aprovado | 17 | 9,49 | 6,00 | 11,95 |
| Não aprovado | 10 | 9,19 | 6,79 | 11,51 |
| Aprovado parcialmente | 3 | 7,68 | 7,22 | 8,59 |

As faixas de nota oficial de "Aprovado" e "Não aprovado" **se sobrepõem quase inteiramente** — o maior
"Não aprovado" da amostra (11,51) supera o menor "Aprovado" (6,00). Isso **reconfirma, com esta amostra
nova de 2025–2026**, o achado já documentado em `references/rubric/final-score.md` a partir da validação
v16.0 ("TOTAL médio foi estatisticamente indistinguível entre Aprovados e Não aprovados"). Não é um erro
do modelo — é uma propriedade real do processo COFIEX (a nota é necessária, nunca suficiente; o saldo do
sublimite na reunião-alvo decide). Nenhuma mudança de rubrica recomendada aqui; só reforça que a skill está
certa em nunca prometer aprovação a partir da nota isolada.

## Onde o modelo mais errou (|Δ| > 2,0 pontos — 6 de 30 casos, 20% da amostra)

| Pleito | Resultado oficial | Nota oficial | Nota cega (esperado) | Δ |
|---|---|---|---|---|
| 302427827 (BDMG TEC, estatal/fundo, Minas Gerais) | Não aprovado | 11,51 | 4,30 | **-7,21** |
| 3059847170 (garantia a PPP hospitalar, Mato Grosso do Sul) | Aprovado | 11,75 | 7,30 | **-4,45** |
| 8540142294 (rodovia CREMA/iRAP, Pernambuco) | Aprovado | 6,60 | 10,10 | **+3,50** |
| 6653317174 (PROFISCO III, Pernambuco) | Aprovado | 11,06 | 8,95 | **-2,11** |
| 6552151988 (drenagem/alerta de inundação, São Paulo) | Não aprovado | 7,09 | 9,20 | **+2,11** |
| 6385828597 (infraestrutura urbana, Alagoinhas/BA) | Aprovado | 8,54 | 10,60 | **+2,06** |

### 1. Maior erro de todos: dados objetivos indisponíveis para estatal/sociedade de economia mista (Δ=-7,21)

O pleito do BDMG (banco de desenvolvimento estadual) é avaliado sob regras de estatal subnacional
(Garantia-Ativo-Fixo/Retorno sobre Investimento em vez de Capacidade de Pagamento; Exigível/Patrimônio
Líquido em vez de Dívida Consolidada/Receita Corrente Líquida — `SKILL.md`, bloco "Sociedade de economia
mista municipal"). **A planilha oficial empacotada (`reference-data/External_Credit_Operations_Database...xlsx`)
não tem essas colunas para esse tipo de ente** — o subagente corretamente marcou `input_flag` e não atribuiu
pontos, então a Nota Geral cega ficou travada só na Nota de Área Estratégica (4,3), enquanto a nota oficial
(11,51) presumivelmente incluiu os componentes de Dados Objetivos por outra via (Nota Técnica/STN).

**Isto é uma lacuna real e corrigível da skill**: não há fonte oficial gratuita mapeada para Capacidade de
Pagamento/Dívida de estatais e sociedades de economia mista. Recomendo adicionar a `references/rubric/
official-data-sources.md` uma linha explícita sobre onde buscar isso (ex.: classificação de risco de bancos
de desenvolvimento estaduais pode constar em relatórios do próprio banco/STN ou agência de rating) — hoje a
skill não erra a nota, ela simplesmente não consegue pontuar, o que é o comportamento mais seguro mas deixa
a faixa artificialmente estreita e baixa.

### 2. Segundo maior erro: desconto por "modalidade de garantia" não confirmado (Δ=-4,45)

Para a garantia a uma PPP hospitalar (Mato Grosso do Sul), o subagente aplicou um desconto estrutural à
Nota de Área Estratégica citando "proporcionalidade" e o padrão do corpus de que "saúde hospitalar/PPP é
historicamente o setor mais fraco" — mas o resultado oficial foi um dos **mais altos de toda a amostra**
(11,75, Aprovado). `references/calibration/cross-cutting-findings.md` já instrui a pontuar essas operações
pela adequação do indicador de nível de serviço, não por desconto de modalidade — mas não existe uma regra
explícita dizendo "não aplicar desconto adicional de ceticismo sobre a modalidade de garantia em si". Vale
reforçar esse ponto na referência.

### 3. Maior superestimação: ancoragem excessiva em "referência internacional" (Δ=+3,50)

Para a rodovia estadual de Pernambuco com metodologia iRAP (segurança viária, referência internacional), o
subagente elevou a nota citando "arcabouço de referência internacional = indicadores SMART por construção"
(exatamente o padrão descrito em `cross-cutting-findings.md`, "Arcabouços setoriais SMART prontos... pontuam
mais alto"). Mas o resultado oficial foi baixo (6,60) — o **menor "Aprovado" da amostra por pouco**. Isso
sugere que esse atalho de calibração ("referência internacional nomeada → nota alta") precisa de mais
nuance: a presença da metodologia por si não garante nota alta se outros fatores (ex.: porte, proporção do
teto, qualidade real de execução dos indicadores específicos) pesarem contra.

### 4-6. Erros de magnitude média (|Δ|≈2,0-2,1), sem padrão único claro
PROFISCO em Pernambuco subestimado (-2,11) enquanto a mesma modalidade no Acre (pleito 9102009723, Δ=-1,70)
teve erro parecido — sugere subestimação sistemática leve do padrão PROFISCO nesta rodada, mas n=2 é pouco
para confirmar. Os outros dois (drenagem em São Paulo +2,11 Não aprovado; infraestrutura em Alagoinhas +2,06
Aprovado) não compartilham um padrão setorial comum nesta amostra.

## Recomendação

1. **Adicionar uma linha a `official-data-sources.md`** sobre a lacuna de dados objetivos para estatais/
   sociedades de economia mista (achado 1 — o mais claro e corrigível).
2. **Reforçar em `cross-cutting-findings.md`** que modalidades de garantia/PPP não devem receber desconto
   adicional de ceticismo além do que a adequação do indicador já captura (achado 2).
3. Não mudar a rubrica de setor "infrastructure_mobility" ou "fiscal" com base em 2-3 casos (achados 3-6) —
   registrar como observação, não como regra, até uma rodada maior.
4. Repetir esta validação com n maior (os outros ~59 pleitos únicos com nota oficial ainda não testados)
   antes de qualquer ajuste de rubrica baseado nos achados 3-6.
