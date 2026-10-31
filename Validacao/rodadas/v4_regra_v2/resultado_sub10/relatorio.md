# Regressão — v4_sub10

Pleitos avaliados: 10 de 10 do banco.

| Métrica | Valor | Baseline |
|---|---|---|
| mae_nota_geral | 1.042 | 1.138 |
| vies_nota_geral | -0.525 | 0.609 |
| mediana_abs_nota_geral | 0.973 | 0.87 |
| mae_ae | 1.02 | 1.175 |
| vies_ae | -0.52 | 0.825 |
| mae_capag | 0.0 | 0.0 |
| mae_divida | 0.0 | 0.036 |
| mae_idh | 0.06 | 0.038 |
| vies_idh | 0.009 | -0.011 |
| cobertura_faixa | 1.0 | 0.85 |
| largura_mediana_faixa | 4.2 | 4.2 |
| acerto_nivel_area_principal | 0.3 | 0.75 |
| acerto_nivel_area_principal_1_degrau | 0.8 | 0.9 |
| acerto_nivel_todas_areas | 0.573 | 0.517 |

Faixa empírica: Nota Geral ±1.52 (80%), ±1.5 (70%); Área Estratégica ±1.5 (80%).

**MAE por estrato:**
- Federal|Federal: 2.0
- Geral|Estadual: 0.849
- Geral|Municipal: 1.175
- Subnacional-especifico|Estadual: 0.49
- Subnacional-especifico|Municipal: 1.109

**Matriz de confusão por área (linhas = oficial, colunas = previsto):**

| oficial \ previsto | A | B | C | D | E | 0 |
|---|---|---|---|---|---|---|
| A | 0 | 0 | 0 | 0 | 0 | 0 |
| B | 0 | 2 | 3 | 2 | 0 | 0 |
| C | 0 | 0 | 3 | 4 | 0 | 0 |
| D | 0 | 0 | 0 | 6 | 5 | 2 |
| E | 0 | 0 | 2 | 4 | 13 | 3 |
| 0 | 0 | 0 | 0 | 2 | 11 | 27 |

**Resultado:** REGRESSÃO em acerto_nivel_area_principal: 0.75 → 0.3 (tolerância 0.05)
