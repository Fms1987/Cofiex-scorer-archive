# Rodada 6: 20 cartas aleatórias (Res. Normativa 1/2024), versão congelada v1-beta-congelada

Sorteio: `random.seed(20261031)` sobre as 89 cartas do banco de teste (todas das reuniões 180ª a 189ª). Quatro agentes de 5 cartas, cada um numa cópia do skill sem as fichas, os cartões e as áreas da própria carta (`make_blind_sandbox.py`, braço A).
Atenção: as regras de B contra C, das tabelas de IDH e de bancos/empresas saíram destas mesmas 89 cartas; a rodada confere calibragem, não valida essas regras às cegas.

## Nota Geral (previsão esperada menos nota oficial)
- Erro médio absoluto 0,96; viés 0,00; mediana +0,05; na faixa 19 de 20; 8 de 20 com desvio acima de 1 ponto.
- Maior desvio: 1669197029 (−2,49, oficial 13,391; área principal 205 oficial A, prevista C). Seguem 1333701175 (+1,99), 3337273653 (+1,77) e 6385828597 (+1,26).
- Referência (rodada 5, as mesmas 20 cartas): erro médio 0,945, viés +0,26; nas 89 cartas: 0,908 e +0,15.

## Componentes
- Área Estratégica (20 cartas): erro médio 0,99, viés +0,14. Sobe demais quando a oficial é ≤5,5 (+1,56 em 5 cartas) e desce quando é ≥7 (−1,00 em 7).
- Dados objetivos, só onde a nota oficial dos componentes existe (13 cartas): Capacidade de Pagamento erro 0,077, Dívida 0,038, IDH 0,053. Em 7 cartas a base não traz os componentes e elas ficam fora.
- Piso do IDH estadual 0,739 e tabelas: IDH previsto acerta com erro até 0,04 nas estaduais com nota oficial.

## Área principal
- Mesma área principal: 16 de 20. Mesmo nível nessa área: 14 de 20 (rodada 5: 56 de 89, 63%).
- Níveis das áreas oficiais reproduzidos: 87 de 165 (53%).
- Erros de nível na principal: 111 C→B (1333701175, 7366456201, 9668114265), 205 A→C (1669197029), 111 B→C (6423305042), 205 B→não reconhecida (3337273653, previu 210).
