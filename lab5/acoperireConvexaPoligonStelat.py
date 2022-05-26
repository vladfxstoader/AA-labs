def testOrientare(P, Q, R):
    if Q[0]*R[1] + R[0]*P[1] + P[0]*Q[1] - Q[0]*P[1] - R[0]*Q[1] - P[0]*R[1] == 0:
        return 'TOUCH'
    elif Q[0]*R[1] + R[0]*P[1] + P[0]*Q[1] - Q[0]*P[1] - R[0]*Q[1] - P[0]*R[1] < 0:
        return 'RIGHT'
    else:
        return 'LEFT'

def jumatateAcoperire(puncte, flag=False):
    if flag:
        directie = 'RIGHT'
    else:
        directie = 'LEFT'
    puncte.sort(key=lambda x: [x[0], x[1]])
    acoperire = [puncte[0], puncte[1]] #incep cu primele 2 puncte

    for i in range(2, len(puncte)): #pentru fiecare punct, adaug la acoperire urmatorul punct cel mai din stanga
        acoperire.append(puncte[i])

        while len(acoperire) > 2 and testOrientare(acoperire[-3], acoperire[-2], acoperire[-1]) != directie: #cat timp acoperirea are mai mult de
                                                                                                                      #2 puncte si ultimele 3 nu determina viraj la stanga/dreapta
                                                                                                                      #(in functie de jumatatea de acoperire)
            acoperire.remove(acoperire[-2])

    return acoperire


def graham_scan(puncte):
    acoperire_sup= jumatateAcoperire(puncte, True)
    acoperire_inf = jumatateAcoperire(puncte)

    acoperire_sup = acoperire_sup[1:-1]  # elimin duplicatele

    acoperire_sup.reverse()

    return acoperire_inf + acoperire_sup

n = int(input())
puncte = []
for i in range(n):
    x1, x2 = [int(x) for x in input().split()]
    puncte.append((x1,x2))

acoperire = graham_scan(puncte)

print(len(acoperire))
for punct in acoperire:
    print(punct[0], punct[1])