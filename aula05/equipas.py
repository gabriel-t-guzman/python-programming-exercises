team1 = ["FCP","SCP","SLB"]
team2 = ["FCP","SCP","SLB","BRC"]

def allmatches (equipas) :
    matches = []
    assert len(equipas) >= 2
    for i in equipas :
        for j in equipas :
            if i == j : continue
            matches.append((i,j))
    return matches

print (allmatches(team1))
print (allmatches(team2))
a = ['A','B']
print (allmatches(a))




