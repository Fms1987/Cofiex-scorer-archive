# Regressão — v2_pacotes12

Pleitos avaliados: 20 de 40 do banco.

| Métrica | Valor | Baseline |
|---|---|---|
| mae_nota_geral | 1.138 | 1.348 |
| vies_nota_geral | 0.609 | 0.463 |
| mediana_abs_nota_geral | 0.87 | 1.127 |
| mae_ae | 1.175 | 1.373 |
| vies_ae | 0.825 | 0.482 |
| mae_capag | 0.0 | 0.188 |
| mae_divida | 0.036 | 0.166 |
| mae_idh | 0.038 | 0.255 |
| vies_idh | -0.011 | -0.253 |
| cobertura_faixa | 0.85 | 0.7 |
| largura_mediana_faixa | 4.2 | 3.1 |
| acerto_nivel_area_principal | 0.75 | — |
| acerto_nivel_area_principal_1_degrau | 0.9 | — |
| acerto_nivel_todas_areas | 0.517 | — |

Faixa empírica: Nota Geral ±1.9 (80%), ±1.19 (70%); Área Estratégica ±2.0 (80%).

**MAE por estrato:**
- Federal|Federal: 1.75
- Geral|Estadual: 0.853
- Geral|Municipal: 1.171
- Subnacional-especifico|Estadual: 1.048
- Subnacional-especifico|Municipal: 1.152

**Matriz de confusão por área (linhas = oficial, colunas = previsto):**

| oficial \ previsto | A | B | C | D | E | 0 |
|---|---|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 | 0 | 0 |
| B | 1 | 9 | 1 | 1 | 0 | 0 |
| C | 0 | 0 | 10 | 2 | 0 | 0 |
| D | 0 | 1 | 5 | 14 | 8 | 3 |
| E | 0 | 0 | 3 | 8 | 13 | 3 |
| 0 | 0 | 0 | 2 | 6 | 26 | 31 |

**Resultado:** sem regressão frente ao baseline
