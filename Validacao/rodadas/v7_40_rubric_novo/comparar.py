import csv,re,sys,glob,statistics as st,collections,json
S=sys.argv[1]
PT={"A":5.0,"B":3.0,"C":2.0,"D":1.0,"E":0.5,"0":0.0}
tr={r["pleito_id"]:r for r in csv.DictReader(open("banco_teste_v3_89/truth.csv",encoding="utf-8"))}
ta=collections.defaultdict(list)
for r in csv.DictReader(open("banco_teste_v3_89/truth_areas.csv",encoding="utf-8")): ta[r["pleito_id"]].append(r)
sel={r["pleito_id"]:r for r in csv.DictReader(open(f"{S}/r7/selecao.csv",encoding="utf-8"))}
def parse(texts):
    P={}
    for t in texts:
        for b in re.findall(r"===PLEITO===(.*?)===FIM===",t,re.S):
            b="\n".join(l.strip() for l in b.splitlines() if l.strip())
            i=re.search(r"ID:\s*(\d+)",b).group(1)
            if i not in tr: continue
            g=lambda k:float(re.search(rf"^{k}:\s*([\d.]+)",b,re.M).group(1))
            ar=[]
            for l in b.splitlines():
                if l.startswith("AREA:"):
                    c,n=[x.strip() for x in l[5:].split("|")]
                    if n in PT: ar.append((c,n))
            P[i]={"ae":g("AE"),"ng":g("NOTA_GERAL_ESP"),"min":g("NOTA_GERAL_MIN"),"max":g("NOTA_GERAL_MAX"),"areas":ar}
    return P
v7=parse(open(p,encoding="utf-8").read() for p in glob.glob(f"{S}/r7/w*/blocos.md"))
v6=parse(open(p,encoding="utf-8").read() for p in glob.glob(f"{S}/r6/w*/blocos.md"))
v5=parse(open(p,encoding="utf-8",errors="replace").read() for p in glob.glob("rodadas/v5_area_dona/blocos/*.md"))
print("v7",len(v7),"v6",len(v6),"v5",len(v5))
f=lambda x:float(x) if x not in ("",None) else None
def stats(P,ids,key,lab):
    e=[P[i][key]-float(tr[i]["ae"] if key=="ae" else tr[i]["nota_geral"]) for i in ids if i in P]
    print(f"{lab:38s} n={len(e):2d} MAE {st.mean(map(abs,e)):.3f} viés {st.mean(e):+.3f} dp {st.stdev(e):.3f} |erro|>1: {sum(abs(x)>1 for x in e)}")
old=[i for i in v7 if sel[i]["origem"]=="r6"]; new=[i for i in v7 if sel[i]["origem"]=="nova"]
for key,name in (("ae","Área Estratégica"),("ng","Nota Geral")):
    print("==",name)
    stats(v7,list(v7),key,"v7 (40)")
    stats(v7,old,key,"v7 nas 20 da rodada 6")
    stats(v6,old,key,"v6 nas mesmas 20")
    stats(v5,old,key,"v5 nas mesmas 20")
    stats(v7,new,key,"v7 nas 20 novas")
    stats(v5,new,key,"v5 nas mesmas 20 novas")
# soma de níveis
def sumlv(d): return min(10,sum(PT[n] for c,n in d["areas"]))
for nome,P,ids in (("v7 40",v7,list(v7)),("v5 mesmas 40",v5,list(v7))):
    e=[sumlv(P[i])-float(tr[i]["ae"]) for i in ids]; print(nome,"soma dos níveis MAE",round(st.mean(map(abs,e)),3),"viés",round(st.mean(e),3))
# níveis
def mat(P,ids):
    C=collections.defaultdict(collections.Counter); prin=[0,0,0]; sec_o=[];sec_p=[]; zeros=[0,0]
    for i in ids:
        off={a["codigo_ppa"]:a["nivel"] for a in ta[i]}; pr=dict(P[i]["areas"])
        for c in set(off)|set(pr): C[off.get(c,"0")][pr.get(c,"0")]+=1
        top=sorted(ta[i],key=lambda a:-float(a["pontos"]))
        if top:
            pc=top[0]["codigo_ppa"]; prin[0]+=1; prin[1]+= (pr.get(pc,"0")==top[0]["nivel"]); 
            best=min((a for a in pr.items() if a[1] in "ABCDE"),key=lambda a:"ABCDE".index(a[1]),default=None)
            prin[2]+= bool(best and best[0]==pc)
            so=sum(float(a["pontos"]) for a in top[1:]); sp=sum(PT[n] for c,n in P[i]["areas"] if c!=pc); sec_o.append(so); sec_p.append(sp)
    return C,prin,sec_o,sec_p
for nome,P in (("v7",v7),("v5",v5)):
    C,prin,so,sp=mat(P,list(v7))
    z=sum(C["0"].values()); zp=sum(v for k,v in C["0"].items() if k!="0")
    print(nome,"| área principal certa",prin[2],"/",prin[0],"; nível certo na principal",prin[1],"/",prin[0],"| secundárias oficial",round(st.mean(so),2),"previsto",round(st.mean(sp),2),"MAE soma sec",round(st.mean(abs(a-b) for a,b in zip(so,sp)),2),"| áreas oficiais 0 que receberam pontos:",zp,"/",z)
    for o in "ABCDE":
        t=sum(C[o].values()); 
        if t: print("   oficial",o,"n",t,"previsto",dict(sorted(C[o].items())))
# por carta
rows=[]
for i in v7:
    rows.append((abs(v7[i]["ae"]-float(tr[i]["ae"])),i,sel[i]["origem"],tr[i]["ae"],v7[i]["ae"],v6.get(i,{}).get("ae"),v5[i]["ae"]))
rows.sort(reverse=True)
print("maiores erros de AE: |erro| id origem oficial v7 v6 v5")
for r in rows[:14]: print(r)
json.dump({"v7":v7,"v6":v6,"v5":v5},open(S+"/r7/all.json","w"))
