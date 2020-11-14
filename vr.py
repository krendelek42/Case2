else:
    if 0 <= annual_income <= 12950:
        N = 0.1*(annual_income - 0 )
        print('Tax amount: ', N)
    elif 12951 <= annual_income <= 49400:
        N = 0.1 * (12951 - 0) + 0.15 * (annual_income - 12951)
        print('Tax amount: ', N)
    elif 49401 <= annual_income <= 127550:
        N = 0.1*(12951 -0) + 0.15*(49401 - 12951) + 0.25*(annual_income -49401)
        print('Tax amount: ', N)
    elif 127551  <= annual_income <= 206600:
        N = 0.1*(12951-0) + 0.15*(49401 - 12951) + 0.25*(127551 - 49401) + 0.28*(annual_income -127551 )
        print('Tax amount: ', N)
    elif 206601 <= annual_income <= 405100:
        N = 0.1*(12951-0) + 0.15*(49401 - 12951) + 0.25*(127551 - 49401) + 0.28*(206601 -127551 ) + 0.33*(annual_income - 206601)
        print('Tax amount: ', N)
    elif 405101 <= annual_income <= 432200:
        N =  0.1*(12951-0) + 0.15*(49401 - 12951) + 0.25*(127551 - 49401) + 0.28*(206601 -127551 ) + 0.33*(405101- 206601)+ 0.35*(annual_income - 405101)
        print('Tax amount: ', N)
    else:
        N =  0.1*(12951-0) + 0.15*(49401 - 12951) + 0.25*(127551 - 49401) + 0.28*(206601 -127551 ) + 0.33*(405101- 206601)+ 0.35*(432201 - 405101)+ 39.6*(annual_income - 432201)
        print('Tax amount: ', N)
