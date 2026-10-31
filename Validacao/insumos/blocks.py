import re, sys
t = open(sys.argv[1], encoding='utf-8', errors='replace').read()
t = re.sub(r'\\+n', '\n', t)
bl = {}
for b in re.findall(r'===PLEITO===.*?===FIM===', t, re.S):
    b = '\n'.join(l.strip() for l in b.splitlines() if l.strip())
    m = re.search(r'ID:\s*(\d+)', b)
    if m and 'NOTA_GERAL_ESP: <' not in b:
        bl[m.group(1)] = b
open(sys.argv[2], 'w', encoding='utf-8').write('\n\n'.join(bl.values()) + '\n')
print(sys.argv[2], list(bl))
