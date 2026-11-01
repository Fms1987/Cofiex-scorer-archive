# Rodada 8: 20 cartas (10 já testadas + 10 novas), só Área Estratégica, duas versões do skill

Versões: última = commit 39d2ba3 (portão de pontuação, piso C, instrumento único, descida estreitada); congelada = tag v1-beta-congelada (7f50bf1, com a lista de B contra C original, sem o portão). Mesmas 20 cartas e mesmos lotes de 5 para as duas. Sorteio: `random.seed(20261102)` (10 das 40 das rodadas 6 e 7) e 10 das 49 restantes. Escopo: apenas Área Estratégica.

## Área Estratégica (previsto menos oficial)
| | n | erro médio | viés | desvio padrão | erros >1 |
|---|---|---|---|---|---|
| última, 20 | 20 | 1,245 | −0,775 | 1,33 | 10 |
| congelada, 20 | 20 | 1,075 | −0,625 | 1,18 | 8 |
| rodada 5 (rubric antigo), mesmas 20 | 20 | 1,050 | −0,150 | 1,30 | 5 |
| última, 10 novas | 10 | 1,12 | −0,88 | 1,29 | 4 |
| congelada, 10 novas | 10 | 1,05 | −0,55 | 1,19 | 5 |

Com 20 cartas e desvio padrão de cerca de 1,3, a diferença entre as versões (0,17) não é distinguível de ruído.

## Por componente (previsto menos oficial, em pontos)
| | última | congelada |
|---|---|---|
| área principal | −0,93 | −1,18 |
| soma das secundárias | +0,07 | +0,62 |
| zeros oficiais pontuados | 11 de 76 | 28 de 80 |
| erro médio da soma das secundárias | 0,72 | 1,12 |
| área principal certa / nível certo | 16 / 11 de 20 | 14 / 9 de 20 |

O viés total menor da congelada vem de erros que se compensam: secundárias acima, principal abaixo. A última acerta melhor cada parte, mas a principal continua baixa.

## Causas lidas nas Notas Técnicas
- Cinco das 20 áreas principais oficiais são A (25%; na base, 10%): `1669197029`, `3059847170`, `3605218738`, `2122866113`, `9409387221`. Nenhuma das duas versões previu A em nenhuma delas. A Nota Técnica justifica com "todos os componentes e recursos", "maioria dos recursos", impacto "transformador", "padrão máximo". Não há marca na carta que separe esses A dos B com a mesma fatia de recursos.
- Metrô (`3605218738`, `2122866113`): oficial 111 em A, com 100% dos recursos e impacto quantificado. O sinal (c), "só uma modalidade", desceu as duas para C (AE 2,5 e 2,8 contra 5,0). Falso positivo.
- Garantia de PPP hospitalar (`3059847170`): a área principal oficial é a 306 (A), porque o objetivo e o componente único são a garantia das obrigações fiscais do Estado; a 102 (saúde, a escolhida pelos agentes em B) ficou em E, "benefício indireto". Os agentes escolheram a área do ativo final em vez da do instrumento.
