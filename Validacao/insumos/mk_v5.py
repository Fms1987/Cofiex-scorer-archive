import csv, os, sys
S = sys.argv[1]
D = {180: '2025-06-18', 182: '2025-09-18', 184: '2025-12-11', 185: '2026-03-26', 187: '2026-06-18', 189: '2026-09-10'}
BS = chr(92)
tpl = open(f'{S}/v4_g1.txt', encoding='utf-8').read()
tpl = tpl.replace('blind_v4' + BS + 'skills' + BS + 'cofiex-scorer- Leia', 'blind_v5' + BS + 'skills' + BS + 'cofiex-scorer\n- Leia')
tpl = tpl.replace('fora de blind_v4', 'fora de blind_v5')
tpl = tpl.replace('com scripts/budget_by_area.py (Python',
                  'com scripts/budget_by_area.py, marcando a área dona de cada produto compartilhado conforme o passo 0 (Python')
head, rest = tpl.split('PASTA DE TRABALHO', 1)
_, tail = rest.split('Para CADA pleito', 1)
bank = list(csv.DictReader(open(f'{S}/bank_all/bank.csv', encoding='utf-8')))
base = r'C:\Users\fabri\Downloads\Cofiex Scorer\Cartas-Consultas\Pleitos_Textos_MD'
idx = {}
for root, _, fs in os.walk(base):
    for f in fs:
        idx[f] = os.path.join(root, f)
print('missing', [b['arquivo'] for b in bank if b['arquivo'] not in idx])
for g in range(0, len(bank), 5):
    k = g // 5 + 1
    wd = f'{S}/v5_work_g{k}'.replace('/', BS)
    lines = [f"- {idx[b['arquivo']]} — reunião {b['reuniao']} ({D[int(b['reuniao'].rstrip('ª'))]})" for b in bank[g:g + 5]]
    p = (head + f'PASTA DE TRABALHO (use SOMENTE esta para JSONs e arquivos intermediários dos scripts; não grave nada em outra pasta): {wd}\n'
         'Não gere .docx nem relatório completo: só o resumo curto e os blocos pedidos.\n\n'
         'Pleitos (reunião-alvo e data a usar no objective_lookup):\n' + '\n'.join(lines) + '\n\nPara CADA pleito'
         + tail.replace('os 5 blocos', f'os {len(lines)} blocos'))
    os.makedirs(f'{S}/v5_work_g{k}', exist_ok=True)
    open(f'{S}/v5_g{k}.txt', 'w', encoding='utf-8').write(p)
print(k)
