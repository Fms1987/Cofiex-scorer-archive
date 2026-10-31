# Rodada 7: 40 cartas (20 da rodada 6 + 20 novas) com o rubric novo de Área Estratégica

Skill: commit 5e4d072 (portão de pontuação, piso C nas secundárias, instrumento único, tabela dos quatro sinais). Sorteio das 20 novas: `random.seed(20261101)` entre as 69 restantes das 89. Oito agentes de 5 cartas, cópia do skill sem as fichas, os cartões e as áreas da própria carta.

## Resultado (previsto menos oficial)
| | n | erro médio Área Estratégica | viés | erro médio Nota Geral | viés |
|---|---|---|---|---|---|
| v7 (todas) | 40 | 1,02 | −0,56 | 1,11 | −0,73 |
| v7 nas 20 da rodada 6 | 20 | 0,945 | −0,51 | 0,97 | −0,65 |
| v6 nas mesmas | 20 | 0,99 | +0,14 | 0,96 | 0,00 |
| v7 nas 20 novas | 20 | 1,10 | −0,62 | 1,25 | −0,82 |
| v5 nas mesmas 20 novas | 20 | 1,00 | +0,15 | 0,92 | −0,14 |

## O que melhorou
- Áreas que a nota oficial zerou e o skill pontuou: 38 de 138 (28%), contra 50 de 130 (38%) na rodada 5 nas mesmas 40 cartas.
- Soma das secundárias: previsto 3,54 contra oficial 3,36 (rodada 5: 3,92); erro médio 1,02 contra 1,11.
- Instrumento único: o fundo `1669197029` saiu A na área 205 (oficial A), AE 9,5 contra 9,0.

## O que piorou
- Nível certo na área principal: 15 de 40 (rodada 5: 27 de 40). Das 28 áreas principais oficiais em B, 16 saíram C (rodada 5: 3).
- Causa: sinais (b) alcance restrito e (d) falha de indicador, aplicados a cada carta, derrubaram para C áreas que a Nota Técnica deixou em B. Nos relatórios dos agentes, (b) isolado: 2 acertos de C (`9668114265`, `5924531231`) e pelo menos 8 erros (`8746753920`, `2486162808`, `9836205829`, `1264789166`, `5502586403`, `6788985859`, `8838019731`, `6385828597`); (d) isolado: 1 acerto (`7788406591`, D) e pelo menos 8 erros (`5911407114`, `2059210710`, `2872607461`, `6187395338`, `5864638957`, `2289026039` e outros). A Nota Técnica deu B nesses casos citando "maioria dos recursos", "alto impacto", mesmo com bairros nomeados ou linha de base ausente.
- O sinal (c) (só habitação, na área 111) acertou: `1333701175` AE 3,0 igual ao oficial.

## Contrafactual aproximado
Descer a principal para C só com (c) ou com (b) e (d) juntos (as demais descidas voltam a B, +1,0 de Área Estratégica): erro médio 0,85, viés −0,11, contra 1,02 e −0,56 como rodou. Aproximação: soma 1,0 sem refazer as secundárias.
