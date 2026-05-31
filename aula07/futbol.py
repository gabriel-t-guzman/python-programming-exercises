
equipas = ["SLB", "SCP", "FCP"]

def perguntar():
    clubs = []
    while True:
        club = str(input("nome do club? :"))
        if club == "" : print(clubs);return clubs
        clubs.append(club)

def jogos(teams):
    clubs = teams
    l = []
    for i in clubs:
        for j in clubs:
            if i != j : l.append((i,j))
    return l

def result(jogos):
    d = {}
    for i in jogos:
        print (i)
        left = int(input("golos esquerda? :"))
        right = int(input("golos direita? :"))
        golos = (left, right)
        d.setdefault(i, golos)
    return d

def tabela(result):
    d = {}
    for i in result:
        d.setdefault(i[0], [0,0,0,0,0,0])
        d.setdefault(i[1], [0,0,0,0,0,0])
        if result[i][0] > result[i][1] :
          #vitoria/derrota     #pontos     
            d[i[0]][0] += 1; d[i[0]][5] += 3
            d[i[1]][2] += 1; d[i[1]][5] += 0
      
        elif result[i][0] < result[i][1] :
          #derrota/vitoria     #pontos
            d[i[0]][2] += 1; d[i[0]][5] += 0
            d[i[1]][0] += 1; d[i[1]][5] += 3
        else :
            # empate2
            d[i[0]][1] += 1; d[i[1]][1] += 1
            # pontos
            d[i[0]][5] += 1
            d[i[1]][5] += 1
        # golos sofridos
        d[i[0]][4] += result[i][1]; d[i[1]][4] += result[i][0]
        # golos feitos
        d[i[0]][3] += result[i][0]; d[i[1]][3] += result[i][1]
    
   # Posso por ca um sorted do diccionario, mas com key=d[i][5] reverse=True , algo asi masomenos
    print(d)
    return (d)

def ptable(tabela):
    print(f"{'Equipas':^7s} - {'Wins':^6s} - {'Empate':^8s} - {'Loses':^5s} - {'Golos_F':^7s} - {'Golos_S':^7s} - {'Pontos':^6s}")
    for i in tabela:
        print(f"{i:^7s} - {tabela[i][0]:^6} - {tabela[i][1]:^8} {tabela[i][2]:^5} - {tabela[i][3]:^7} - {tabela[i][4]:^7} - {tabela[i][5]:^6}")

def main():
   teams = perguntar()
   j = jogos(teams)
   res = (result(j))
   print (res)
   table = tabela(res)
   ptable(table)
   


main()




