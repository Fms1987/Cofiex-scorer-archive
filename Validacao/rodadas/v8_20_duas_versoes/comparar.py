import csv,re,sys,glob,statistics as st,collections,json
S=sys.argv[1]
PT={"A":5.0,"B":3.0,"C":2.0,"D":1.0,"E":0.5,"0":0.0}
tr={r["pleito_id"]:r for r in csv.DictReader(open("banco_teste_v3_89/truth.csv",encoding="utf-8"))}
ta=collections.defaultdict(list)
for r in csv.DictReader(open("banco_teste_v3_89/truth_areas.csv",encoding="utf-8")): ta[r["pleito_id"]].append(r)
sel={r["pleito_id"]:r for r in csv.DictReader(open(f"{S}/r8/selecao.csv",encoding="utf-8"))}
def parse(texts):
    P={}
    for t in texts:
        for b in re.findall(r"===PLEITO===(.*?)===FIM===",t,re.S):
            b="\n".join(l.strip() for l in b.splitlines() if l.strip())
            i=re.search(r"ID:\s*(\d+)",b).group(1)
            if i not in tr: continue
            ae=float(re.search(r"^AE:\s*([\d.]+)",b,re.M).group(1))
            ar=[]
            for l in b.splitlines():
                if l.startswith("AREA:"):
                    c,n=[x.strip() for x in l[5:].split("|")]
                    if n in PT: ar.append((c,n))
            P[i]={"ae":ae,"areas":ar}
    return P
L=parse(open(p,encoding="utf-8").read() for p in glob.glob(f"{S}/r8/a*/blocos.md"))
F=parse(open(p,encoding="utf-8").read() for p in glob.glob(f"{S}/r8/f*/blocos.md"))
print("última",len(L),"congelada",len(F))
d7=json.load(open(S+"/r7/all.json")); V7=d7["v7"]; V5=d7["v5"]
ids=sorted(sel)
def st_(P,sub,lab):
    e=[P[i]["ae"]-float(tr[i]["ae"]) for i in sub if i in P]
    print(f"{lab:34s} n={len(e):2d} MAE {st.mean(map(abs,e)):.3f} viés {st.mean(e):+.3f} dp {st.stdev(e):.3f} |erro|>1: {sum(abs(x)>1 for x in e)}")
for grupo,sub in (("todas (20)",ids),("10 já testadas",[i for i in ids if sel[i]["origem"]=="testada"]),("10 novas",[i for i in ids if sel[i]["origem"]=="nova"])):
    print("==",grupo)
    st_(L,sub,"última versão"); st_(F,sub,"v1-beta-congelada")
    if grupo!="10 novas":
        st_(V7,sub,"rodada 7 (rubric 5e4d072)")
    st_(V5,sub,"rodada 5 (89 cartas, rubric antigo)")
def level_stats(P,sub,lab):
    prin=[0,0,0]; sec_o=[];sec_p=[]; zp=[0,0]; C=collections.defaultdict(collections.Counter)
    for i in sub:
        off={a["codigo_ppa"]:a["nivel"] for a in ta[i]}; pr=dict(P[i]["areas"])
        for c in set(off)|set(pr): C[off.get(c,"0")][pr.get(c,"0")]+=1
        top=sorted(ta[i],key=lambda a:-float(a["pontos"]))
        if not top: continue
        pc=top[0]["codigo_ppa"]; prin[0]+=1; prin[1]+=(pr.get(pc,"0")==top[0]["nivel"])
        best=min((a for a in pr.items() if a[1] in "ABCDE"),key=lambda a:"ABCDE".index(a[1]),default=None)
        prin[2]+=bool(best and best[0]==pc)
        sec_o.append(sum(float(a["pontos"]) for a in top[1:])); sec_p.append(sum(PT[n] for c,n in P[i]["areas"] if c!=pc))
    z=sum(C["0"].values()); zpv=sum(v for k,v in C["0"].items() if k!="0")
    print(f"{lab:22s} área principal certa {prin[2]}/{prin[0]}, nível certo {prin[1]}/{prin[0]} | secundárias oficial {st.mean(sec_o):.2f} previsto {st.mean(sec_p):.2f} (MAE {st.mean(abs(a-b) for a,b in zip(sec_o,sec_p)):.2f}) | zeros oficiais pontuados {zpv}/{z} | oficial B previsto {dict(C['B'])}")
print("== níveis (20 cartas)")
level_stats(L,ids,"última versão"); level_stats(F,ids,"v1-beta-congelada")
level_stats(V7,[i for i in ids if i in V7],"rodada 7 (mesmas)"); level_stats(V5,ids,"rodada 5 (mesmas)")
print("== por carta: oficial | última | congelada | r7 | r5")
rows=[]
for i in ids:
    o=float(tr[i]["ae"]); rows.append((i,sel[i]["origem"],o,L[i]["ae"],F[i]["ae"],V7.get(i,{}).get("ae"),V5[i]["ae"]))
for r in sorted(rows,key=lambda r:-max(abs(r[3]-r[2]),abs(r[4]-r[2]))): print(r)
json.dump({"L":L,"F":F},open(S+"/r8/all.json","w"))
