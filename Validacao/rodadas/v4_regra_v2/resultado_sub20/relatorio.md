# Regressão — v4_sub20

Pleitos avaliados: 20 de 20 do banco.

| Métrica | Valor | Baseline |
|---|---|---|
| mae_nota_geral | 0.91 | 1.138 |
| vies_nota_geral | 0.25 | 0.609 |
| mediana_abs_nota_geral | 0.822 | 0.87 |
| mae_ae | 0.885 | 1.175 |
| vies_ae | 0.465 | 0.825 |
| mae_capag | 0.0 | 0.0 |
| mae_divida | 0.036 | 0.036 |
| mae_idh | 0.039 | 0.038 |
| vies_idh | -0.011 | -0.011 |
| cobertura_faixa | 0.95 | 0.85 |
| largura_mediana_faixa | 4.2 | 4.2 |
| acerto_nivel_area_principal | 0.75 | 0.75 |
| acerto_nivel_area_principal_1_degrau | 0.95 | 0.9 |
| acerto_nivel_todas_areas | 0.517 | 0.517 |

Faixa empírica: Nota Geral ±1.45 (80%), ±1.0 (70%); Área Estratégica ±1.0 (80%).

**MAE por estrato:**
- Federal|Federal: 2.25
- Geral|Estadual: 0.613
- Geral|Municipal: 0.81
- Subnacional-especifico|Estadual: 0.783
- Subnacional-especifico|Municipal: 0.816

**Matriz de confusão por área (linhas = oficial, colunas = previsto):**

| oficial \ previsto | A | B | C | D | E | 0 |
|---|---|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 | 0 | 0 |
| B | 1 | 10 | 1 | 0 | 0 | 0 |
| C | 0 | 0 | 10 | 1 | 1 | 0 |
| D | 0 | 1 | 4 | 12 | 13 | 1 |
| E | 0 | 0 | 3 | 6 | 12 | 6 |
| 0 | 0 | 0 | 0 | 6 | 23 | 30 |

**Resultado:** sem regressão frente ao baseline
