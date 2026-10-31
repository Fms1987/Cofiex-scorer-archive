# Regressão — v4_regra_v2

Pleitos avaliados: 30 de 30 do banco.

| Métrica | Valor | Baseline |
|---|---|---|
| mae_nota_geral | 0.954 | 1.138 |
| vies_nota_geral | -0.008 | 0.609 |
| mediana_abs_nota_geral | 0.917 | 0.87 |
| mae_ae | 0.93 | 1.175 |
| vies_ae | 0.137 | 0.825 |
| mae_capag | 0.0 | 0.0 |
| mae_divida | 0.023 | 0.036 |
| mae_idh | 0.047 | 0.038 |
| vies_idh | -0.004 | -0.011 |
| cobertura_faixa | 0.967 | 0.85 |
| largura_mediana_faixa | 4.2 | 4.2 |
| acerto_nivel_area_principal | 0.6 | 0.75 |
| acerto_nivel_area_principal_1_degrau | 0.9 | 0.9 |
| acerto_nivel_todas_areas | 0.539 | 0.517 |

Faixa empírica: Nota Geral ±1.5 (80%), ±1.21 (70%); Área Estratégica ±1.5 (80%).

**MAE por estrato:**
- Federal|Federal: 2.167
- Geral|Estadual: 0.691
- Geral|Municipal: 0.92
- Subnacional-especifico|Estadual: 0.686
- Subnacional-especifico|Municipal: 0.933

**Matriz de confusão por área (linhas = oficial, colunas = previsto):**

| oficial \ previsto | A | B | C | D | E | 0 |
|---|---|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 | 0 | 0 |
| B | 1 | 12 | 4 | 2 | 0 | 0 |
| C | 0 | 0 | 13 | 5 | 1 | 0 |
| D | 0 | 1 | 4 | 18 | 18 | 3 |
| E | 0 | 0 | 5 | 10 | 25 | 9 |
| 0 | 0 | 0 | 0 | 8 | 34 | 57 |

**Resultado:** REGRESSÃO em acerto_nivel_area_principal: 0.75 → 0.6 (tolerância 0.05)
