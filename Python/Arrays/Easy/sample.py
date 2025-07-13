def test(S,T):
    nS = len(S)
    nT = len(T)
    check  = 0

    for i in range(nS):
        for j in range(nT):
            if S[i] == T[j]:
                check += 1
                break

    if check >= nT:
        return check
    else:
        return -1
    
S = "warrmmmiourh"
T = "warriour"
print(test(S,T))