def field(goods, *args):
    ans = [{} for i in range(len(goods))]
    i=0; j=0
    for el in goods:
        for key in args:
            if key==None: continue
            if key in el.keys(): ans[i][key] = el[key]
        i+=1
    while j<i:
        if len(ans[j])==0:
            ans.pop(j); i-=1
        else: j+=1
    if len(args)==1:
        return [el[args[0]] for el in ans]
    return ans