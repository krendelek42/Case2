









































elif status == 'married couple':
    if 0 <= annual_income <= 18150:
        N = 0.1*(annual_income - 0 )
        print('Tax amount: ' , N)
    elif  18151 <= annual_income <= 73800:
        N = 0.1*(18151 -0) + 0.15*(annual_income - 18151)
        print('Tax amount: ', N)
    elif 73801 <= annual_income <= 148850:
        N = 0.1*(18151 -0) + 0.15*(73801 - 18151) + 0.25*(annual_income - 73801)
        print('Tax amount: ', N)
    elif 148851 <= annual_income <= 226850:
        N = 0.1*(18151 -0) + 0.15*(73801 - 18151) + 0.25*(148851 - 73801) + 0.28*(annual_income - 148851)
        print('Tax amount: ', N)
    elif 226851 <= annual_income <= 405100:
        N = 0.1*(18151 -0) + 0.15*(73801 - 18151) + 0.25*(148851 - 73801) + 0.28*(226851 - 148851) + 0.33*(annual_income - 226851)
        print('Tax amount: ', N)
    elif 405101 <= annual_income <=457600:
        N = 0.1*(18151 -0) + 0.15*(73801 - 18151) + 0.25*(148851 - 73801) + 0.28*(226851 - 148851) + 0.33*(405101 - 226851) + 0.35*(annual_income - 405101)
        print('Tax amount: ', N)
    else:
        N = 0.1*(18151 -0) + 0.15*(73801 - 18151) + 0.25*(148851 - 73801) + 0.28*(226851 - 148851) + 0.33*(405101 - 226851) + 0.35*(457601 - 405101) + 39.6*(annual_income - 457601)
        print('Tax amount: ', N)
