def RuleExist(Target, Regles,usedRules=[]):
    for r in Regles:
        if(Target in r.Result and not (r.Name in usedRules)):
            return True, r
    return False, None

def Verify(Rule, Faits):
    for r in Rule.Param:
        if(not r in Faits):
            return False
    return True

def Arriere(Regles,Faits,Target, usedRules=[]):
    
    if(Target in Faits):
        return True, usedRules
    E = RuleExist(Target, Regles,usedRules)
    if(E[0]):
        usedRules.append(E[1].Name)
        V = Verify(E[1],Faits)
        if(V):
            for t in E[1].Result:
                Faits.append(t)
            return True, usedRules
        else:
            found = True
            for t in E[1].Param:
                found = found and Arriere(Regles,Faits,t,usedRules)[0]
            if(found):
                Faits.append(Target)
            return found, usedRules

    else:
        return False, usedRules




























    # if(Target in NewFacts):
    #     return True, usedRules, NewFacts
    # else:
    #     found = True
    #     for r in Regles:
    #         if(Target in r.Result):
    #             for d in r.Param:
    #                 tmp = Arriere([x for x in Regles if not x in usedRules],NewFacts,d)
    #                 found = (found and tmp[0])
    #                 if(tmp[0]):

                    
    #         if(found):
    #             return True
