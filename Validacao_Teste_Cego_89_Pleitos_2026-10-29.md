# Validação por teste cego — 89 pleitos reais (2025–2026), skill cofiex-scorer V.1 BETA

Data: 2026-10-29. Rodada 2 (59 novos casos) somada à Rodada 1 (30 casos, mesmo dia) = **n=89**, de 118 pleitos
únicos disponíveis em `Cartas-Consultas/Pleitos_Textos_MD/Pleitos_2025_2026` (89 com nota oficial confirmada na
base consolidada 165ª–189ª). Metodologia idêntica à Rodada 1: cada subagente aplicou a skill completa
(SKILL.md + references/) **sem acesso** a Notas Técnicas, `Resultados_Cofiex_md`, a base consolidada, nem
busca web pelo desfecho — julgamento cego preservado em todos os 89 casos. A Rodada 2 já incorporou as duas
correções aprovadas após a Rodada 1 (regra do ente mantenedor para estatais; proibição de desconto extra por
"modalidade de garantia/PPP").

Cruzamento automatizado via `tools/parse_blind_results.py` na Rodada 2 (blocos estruturados
`===PLEITO===...===FIM===`); Rodada 1 permanece manual (`validation_30_results.csv`). Script e metodologia
de pareamento (`tools/match_pleitos_to_results.py`) comitados no repositório como ferramentas de regressão.

## Resultado agregado (n=89)

- **MAE: 1,44 pontos** (escala 0–15 → 9,6%) — **idêntico** ao MAE da Rodada 1 isolada (1,43/9,6%). O erro
  médio absoluto não mudou com o dobro da amostra, o que é um bom sinal de que a Rodada 1 não era um acaso
  de amostragem favorável.
- **Viés médio: +0,23** (leve sobre-estimação) — inverteu de sinal frente à Rodada 1 isolada (-0,23,
  sub-estimação leve). Combinando as duas rodadas o viés já era pequeno; agora praticamente se cancela,
  reforçando que não há um viés direcional sistemático forte, só ruído em ambas as direções.
- **Mediana do erro absoluto: 1,10 ponto.**

## Achado principal (reconfirmado com o dobro do n): nota não discrimina aprovação

| Resultado oficial | n | Nota oficial média | Min | Max |
|---|---|---|---|---|
| Aprovado | 74 | 9,15 | 2,00 | 13,41 |
| Não aprovado | 12 | 9,07 | 6,79 | 11,51 |
| Aprovado parcialmente | 3 | 7,68 | 7,22 | 8,59 |

As médias de "Aprovado" (9,15) e "Não aprovado" (9,07) ficam **ainda mais próximas** do que na Rodada 1
(9,49 vs. 9,19) — com a amostra maior a sobreposição é total. O menor "Aprovado" da base (nota oficial 2,00
— pleito 9194096568, fundo de repasse federal) é mais baixo que **todos os "Não aprovado"** da amostra.
Confirma, agora com n maior, que a nota é necessária mas nunca suficiente — o saldo do sublimite na
reunião-alvo decide. Nenhuma mudança de rubrica recomendada neste ponto.

## Maiores erros da Rodada 2 (|Δ| > 3,0 — 7 de 59 novos casos, ~12%)

| Pleito | Resultado oficial | Nota oficial | Nota cega (esperado) | Δ |
|---|---|---|---|---|
| 3337273653 (SUAPE, transição energética, ente mantenedor PE) | Não aprovado | 7,23 | 11,40 | **+4,17** |
| 9443031498 (PROEFIS Manaus, reestruturação de dívida) | Aprovado | 5,71 | 9,80 | **+4,09** |
| 9194096568 (fundo repasse privado, Min. Integração) | Aprovado | 2,00 | 6,00 | **+4,00** |
| 3090938102 (PPP travessias hídricas, SP) | Aprovado | 5,70 | 9,20 | **+3,50** |
| 6187395338 (PROFISCO III, Paraná) | Aprovado | 13,41 | 10,15 | **-3,26** |
| 4848871835 (Piauí, reestruturação de dívida fiscal) | Aprovado | 6,73 | 9,90 | **+3,17** |
| 1333701175 (Casa Fácil, Paraná, habitação) | Aprovado | 7,41 | 10,50 | **+3,09** |

### Achado confirmado: sobre-estimação sistemática em reestruturação de dívida (investigação adicional, 2026-10-29)

Busquei no corpus completo (322 arquivos, todas as revisões) por operações cuja finalidade real é
reestruturação de dívida (não apenas uma menção de contexto histórico) e cruzei com a base consolidada.
Achei mais 2 casos já testados nas rodadas 1/2 que também são reestruturação (Fortaleza e Belém, confirmado
pela própria narrativa dos subagentes), totalizando **6 casos com nota oficial completa**:

| Pleito | Resultado oficial | Nota oficial | Nota cega esperada | Δ |
|---|---|---|---|---|
| 9443031498 (Manaus, PROEFIS) | Aprovado | 5,71 | 9,80 | **+4,09** |
| 4848871835 (Piauí) | Aprovado | 6,73 | 9,90 | **+3,17** |
| 5095230048 (Salvador) | Aprovado | 8,61 | 11,50 | **+2,89** |
| 5904123987 (Fortaleza) | Aprovado | 5,61 | 8,30 | **+2,69** |
| 5682006131 (Belém) | Aprovado | 6,69 | 7,60 | +0,92 |
| 7330904301 (Bahia, BIRD) | Aprovado | 7,63 | 6,50 | -1,13 |

**5 de 6 casos (83%) sobre-estimados**, com uma sobre-estimação média de **+2,10 pontos** no grupo — bem
acima do viés médio geral da amostra (+0,23). Isso confirma a hipótese com mais evidência do que o n=4
inicial: mesmo após o desconto estrutural à Nota de Área Estratégica já previsto em
`ae-ranges-and-sectors.md` (banda 3,0–5,5) para essa modalidade, a Nota Geral final ainda tende a sair alta
demais — provavelmente porque o componente de Dados Objetivos (Capacidade de Pagamento/Dívida/Índice de
Desenvolvimento Humano) não é descontado da mesma forma e acaba inflando o total quando a Área Estratégica
já está (corretamente) deprimida.

Também verifiquei mais 3 candidatos de reestruturação no corpus (São Paulo, USD 1,275 bi; e dois pleitos da
Bahia — operação geral e precatórios) — mas nenhum tem Nota Geral oficial completa na base consolidada:
são operações que, por estarem isentas de concorrer pelo limite (Art. 30 da RN 1/2024), só têm o
componente de Área Estratégica registrado (ex.: São Paulo = 4,5, sem Dados Objetivos lançados) ou não
constam nas planilhas de pontuação. Não servem como gabarito de Nota Geral, então ficaram fora da tabela
acima.

**Recomendação de rubrica (agora com n=6, padrão direcional forte):** considerar reforçar
`cross-cutting-findings.md` com uma nota explícita de que, em reestruturação de dívida, o componente de
Dados Objetivos tende a inflar a Nota Geral mesmo com a Área Estratégica corretamente descontada — e que a
expectativa de Nota Geral para essa modalidade deveria ficar mais perto do piso da banda (próxima da soma
pura da Área Estratégica descontada + componentes mínimos), não do meio/topo. Ainda é prudente não fixar um
desconto numérico específico com n=6, mas o padrão já é forte o suficiente para orientar o próximo ajuste.

### Erros de valor extremo em intermediação financeira/fundos de repasse (2 casos)

- 9194096568 (fundo de repasse a projetos privados, USD 500M): nota oficial 2,00 — a mais baixa de toda a
  amostra de 89 — vs. esperado 6,00 (Δ+4,00). O subagente já havia sinalizado risco de porte/atribuição
  causal fraca, mas a nota ficou muito acima do real.
- 8192057868 (Desenvolve SP, estatal, aplicada regra do ente mantenedor): não está entre os maiores erros,
  mas no mesmo padrão de intermediação financeira — sugere que operações de repasse/fundo, mesmo com
  indicadores aparentemente bem estruturados, tendem a pontuar na prática mais baixo do que a rubrica
  atual projeta. Observação qualitativa, não conclusiva com este n.

### Confirmação do achado da Rodada 1: nenhum padrão isolado deve virar regra ainda
Os outros 3 maiores erros (SUAPE, PPP travessias SP, PROFISCO PR, Casa Fácil PR) não compartilham setor,
modalidade ou ente comum — tratá-los como ruído de amostra pequena, não como lacuna de rubrica, é a leitura
mais honesta.

## Recomendação

1. **Investigar com mais casos a hipótese de reestruturação de dívida** (achado novo, n=4, direção
   consistente em 3/4): se confirmado em mais exemplos, considerar aumentar o desconto estrutural ou revisar
   como os Dados Objetivos interagem com a Área Estratégica já descontada nessas operações.
2. **Não mudar nenhuma outra regra de rubrica com base nesta rodada** — MAE estável em 1,44 com o dobro do n
   indica que a skill está bem calibrada no geral; os erros grandes restantes são dispersos, sem padrão
   setorial ou de modalidade comum.
3. Reforça-se o achado estrutural já documentado: nota geral não deve nunca ser comunicada como preditor
   isolado de aprovação — a sobreposição completa entre Aprovado/Não aprovado persiste com n=89.
