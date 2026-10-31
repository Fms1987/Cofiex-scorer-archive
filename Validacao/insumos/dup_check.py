import os, sys, subprocess, hashlib, collections
S = sys.argv[1]
deleted = set(p for p in open(f'{S}/deleted.z','rb').read().decode('utf-8').split('\0') if p)
idx = {}
for e in open(f'{S}/index.z','rb').read().decode('utf-8').split('\0'):
    if not e: continue
    meta, path = e.split('\t', 1)
    idx[path] = meta.split()[1]
sha_present = collections.defaultdict(list)
for p, s in idx.items():
    if p not in deleted:
        sha_present[s].append(p)
exact, rest = {}, []
for p in sorted(deleted):
    s = idx[p]
    if s in sha_present: exact[p] = sha_present[s][0]
    else: rest.append(p)
print('deleted', len(deleted), 'exact duplicate of another tracked file', len(exact), 'rest', len(rest))
# rest: look for same content anywhere in working tree (incl. nested/ignored) via size then sha1 of blob
sizes = {}
out = subprocess.run(['git','cat-file','--batch-check=%(objectname) %(objectsize)'], input='\n'.join(idx[p] for p in rest)+'\n', capture_output=True, text=True).stdout.split('\n')
for p, l in zip(rest, out):
    sizes[p] = int(l.split()[1])
want = collections.defaultdict(list)
for p in rest: want[sizes[p]].append(p)
found = {}
for root, dirs, fs in os.walk('.'):
    if '.git' in dirs: dirs.remove('.git')
    for f in fs:
        fp = os.path.join(root, f)
        try: sz = os.path.getsize(fp)
        except OSError: continue
        if sz in want:
            h = hashlib.sha1(b'blob %d\0' % sz + open(fp,'rb').read()).hexdigest()
            for p in want[sz]:
                if idx[p] == h: found[p] = fp
print('rest found elsewhere in working tree (same bytes)', len(found))
left = [p for p in rest if p not in found]
print('no identical copy anywhere', len(left))
import json
json.dump({'exact': exact, 'found': found, 'left': left}, open(f'{S}/res.json','w'), ensure_ascii=False, indent=0)
