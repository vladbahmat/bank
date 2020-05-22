def survey():
    c = [[0] * 4 for i in range(4)]
    a=['BYN','USD','EUR','RUB']
    b=['BYN','USD','EUR','RUB']
    choose_list=[]
    for i in range(4):
        for j in range(i,4):
            if i!=j:
                print('1 ',a[i],'or 2 ',b[j])
                choose=input("Please, enter number: ")
                if int(choose)==1:
                    choose_list.append(a[i])
                    c[i][j]=1
                elif int(choose)==2:
                    choose_list.append(b[j])
                    c[j][i]=1
    byn=choose_list.count("BYN")
    usd=choose_list.count("USD")
    eur=choose_list.count("EUR")
    rub=choose_list.count("RUB")




