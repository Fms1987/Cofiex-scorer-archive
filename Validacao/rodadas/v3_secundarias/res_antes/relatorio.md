# Regressão — v3_antes

Pleitos avaliados: 20 de 40 do banco.

| Métrica | Valor | Baseline |
|---|---|---|
| mae_nota_geral | 1.026 | — |
| vies_nota_geral | 0.316 | — |
| mediana_abs_nota_geral | 0.644 | — |
| mae_ae | 1.0 | — |
| vies_ae | 0.55 | — |
| mae_capag | 0.0 | — |
| mae_divida | 0.083 | — |
| mae_idh | 0.048 | — |
| vies_idh | -0.002 | — |
| cobertura_faixa | 0.95 | — |
| largura_mediana_faixa | 4.2 | — |
| acerto_nivel_area_principal | 0.4 | — |
| acerto_nivel_area_principal_1_degrau | 0.9 | — |
| acerto_nivel_todas_areas | 0.539 | — |

Faixa empírica: Nota Geral ±1.75 (80%), ±1.43 (70%); Área Estratégica ±1.5 (80%).

**MAE por estrato:**
- Federal|Federal: 0.25
- Geral|Estadual: 0.677
- Geral|Municipal: 1.296
- Subnacional-especifico|Estadual: 1.701
- Subnacional-especifico|Municipal: 0.342

**Matriz de confusão por área (linhas = oficial, colunas = previsto):**

| oficial \ previsto | A | B | C | D | E | 0 |
|---|---|---|---|---|---|---|
| A | 1 | 1 | 0 | 1 | 0 | 0 |
| B | 1 | 5 | 4 | 0 | 0 | 0 |
| C | 0 | 5 | 5 | 2 | 1 | 0 |
| D | 0 | 0 | 1 | 12 | 8 | 0 |
| E | 0 | 0 | 1 | 5 | 21 | 10 |
| 0 | 0 | 0 | 2 | 6 | 23 | 39 |

**Resultado:** sem baseline
