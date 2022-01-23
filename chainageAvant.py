def Avant(Rules,Faits):
    NewFacts = [i for i in Faits]
    usedRules = []
    done = False
    while(not done):
        done = True
        for r in Rules:
            if(not r.Name in usedRules):
                exist = True
                for p in r.Param:
                    if(not p in NewFacts):
                        exist = False
                        break
                if(exist):
                    for res in r.Result:
                        NewFacts.append(res)
                    usedRules.append(r.Name)
                    done=False
        
    return usedRules, NewFacts
