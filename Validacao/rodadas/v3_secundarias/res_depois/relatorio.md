# Regressão — v3_depois

Pleitos avaliados: 20 de 40 do banco.

| Métrica | Valor | Baseline |
|---|---|---|
| mae_nota_geral | 0.817 | 1.026 |
| vies_nota_geral | 0.13 | 0.316 |
| mediana_abs_nota_geral | 0.523 | 0.644 |
| mae_ae | 0.785 | 1.0 |
| vies_ae | 0.365 | 0.55 |
| mae_capag | 0.0 | 0.0 |
| mae_divida | 0.083 | 0.083 |
| mae_idh | 0.048 | 0.048 |
| vies_idh | -0.002 | -0.002 |
| cobertura_faixa | 1.0 | 0.95 |
| largura_mediana_faixa | 4.2 | 4.2 |
| acerto_nivel_area_principal | 0.5 | 0.4 |
| acerto_nivel_area_principal_1_degrau | 0.85 | 0.9 |
| acerto_nivel_todas_areas | 0.526 | 0.539 |

Faixa empírica: Nota Geral ±1.24 (80%), ±1.13 (70%); Área Estratégica ±1.5 (80%).

**MAE por estrato:**
- Federal|Federal: 0.5
- Geral|Estadual: 0.915
- Geral|Municipal: 0.929
- Subnacional-especifico|Estadual: 0.824
- Subnacional-especifico|Municipal: 0.663

**Matriz de confusão por área (linhas = oficial, colunas = previsto):**

| oficial \ previsto | A | B | C | D | E | 0 |
|---|---|---|---|---|---|---|
| A | 1 | 1 | 1 | 0 | 0 | 0 |
| B | 1 | 6 | 3 | 0 | 0 | 0 |
| C | 0 | 4 | 5 | 3 | 1 | 0 |
| D | 0 | 0 | 1 | 9 | 9 | 2 |
| E | 1 | 0 | 0 | 4 | 16 | 16 |
| 0 | 0 | 0 | 2 | 6 | 18 | 44 |

**Resultado:** sem regressão frente ao baseline
