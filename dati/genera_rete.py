# Rigenera dati/rete.json dai CSV.
# Uso (dalla cartella del repository): python dati/genera_rete.py dati dati/rete.json
import csv,json,collections,statistics,sys
src=sys.argv[1]
n=list(csv.DictReader(open(src+'/nodi_1965-1999.csv',encoding='utf-8')))
e=list(csv.DictReader(open(src+'/relazioni_1965-1999.csv',encoding='utf-8')))
nodes={r['Id']:{'n':r['Label'].strip(),'r':r['ruolo'].strip()} for r in n}
albums={}
bad=0
for r in e:
    s,t,y=r['Source'],r['Target'],int(r['Anno'])
    if s not in nodes or t not in nodes: bad+=1; continue
    if nodes[t]['r']!='album':
        if nodes[s]['r']=='album': s,t=t,s
        else: bad+=1; continue
    a=albums.setdefault(t,{'y':y,'c':[]})
    if s not in a['c']: a['c'].append(s)
print('bad',bad,'albums',len(albums),file=sys.stderr)
# performer per album
out_alb=[]
for aid,a in albums.items():
    out_alb.append([int(aid),nodes[aid]['n'],a['y'],[int(c) for c in a['c']]])
out_alb.sort(key=lambda x:(x[2],x[1]))
used=set(c for a in out_alb for c in a[3])
out_nodes={int(k):[v['n'],v['r']] for k,v in nodes.items() if int(k) in used}
json.dump({'albums':out_alb,'nodes':out_nodes},open(sys.argv[2],'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
# stats
by_year=collections.defaultdict(list)
for a in out_alb: by_year[a[2]].append(len(a[3]))
for y in sorted(by_year): print(y,len(by_year[y]),round(statistics.mean(by_year[y]),1))
deg=collections.Counter(c for a in out_alb for c in a[3])
roles=collections.defaultdict(list)
for k,v in deg.most_common():
    roles[nodes[str(k)]['r']].append((nodes[str(k)]['n'],v))
for r,l in roles.items(): print(r,l[:6])
# performers per album count
perf=[a for a in out_alb if not any(nodes[str(c)]['r']=='performer' for c in a[3])]
print('albums without performer',len(perf),[p[1] for p in perf[:5]])
print('nodes',len(out_nodes),'distinct roles',collections.Counter(v[1] for v in out_nodes.values()))
