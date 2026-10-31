# Regressão — v5_area_dona

Pleitos avaliados: 89 de 89 do banco.

| Métrica | Valor | Baseline |
|---|---|---|
| mae_nota_geral | 0.908 | 0.954 |
| vies_nota_geral | 0.151 | -0.008 |
| mediana_abs_nota_geral | 0.695 | 0.917 |
| mae_ae | 0.927 | 0.93 |
| vies_ae | 0.253 | 0.137 |
| mae_capag | 0.024 | 0.0 |
| mae_divida | 0.048 | 0.023 |
| mae_idh | 0.058 | 0.047 |
| vies_idh | 0.003 | -0.004 |
| cobertura_faixa | 0.944 | 0.967 |
| largura_mediana_faixa | 4.2 | 4.2 |
| acerto_nivel_area_principal | 0.629 | 0.6 |
| acerto_nivel_area_principal_1_degrau | 0.944 | 0.9 |
| acerto_nivel_todas_areas | 0.558 | 0.539 |

Faixa empírica: Nota Geral ±1.49 (80%), ±1.07 (70%); Área Estratégica ±1.5 (80%).

**MAE por estrato:**
- Federal|Federal: 0.889
- Geral|Estadual: 1.03
- Geral|Municipal: 0.847
- Subnacional-especifico|Estadual: 1.073
- Subnacional-especifico|Municipal: 0.617

**Matriz de confusão por área (linhas = oficial, colunas = previsto):**

| oficial \ previsto | A | B | C | D | E | 0 |
|---|---|---|---|---|---|---|
| A | 3 | 4 | 0 | 1 | 1 | 0 |
| B | 0 | 48 | 6 | 1 | 1 | 0 |
| C | 0 | 21 | 22 | 16 | 4 | 0 |
| D | 0 | 4 | 10 | 42 | 40 | 13 |
| E | 0 | 1 | 7 | 29 | 80 | 45 |
| 0 | 0 | 1 | 1 | 16 | 98 | 209 |

**Resultado:** sem regressão frente ao baseline
