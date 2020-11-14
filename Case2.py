# Case-study #2
# Developers:   Dokukina K. (%),
#               Nazirova E. (%),
#               Shevchenko V. (%)


# string constants
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
QUESTION = 'What is your income for'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION,name_month[month], end =''))
    income = float(input())
    annual_income += income
print(annual_income)
tax_deduction = int(input('Enter the amount of tax deduction: '))
annual_income -= tax_deduction
status = input('What is your status? (one subject, married couple, single parent): ')
if status == 'one subject':
    if 0 <= annual_income <= 9075:
        N = 0.1*(annual_income - 0)
        print('Tax amount: ', N)
    elif 9076 <= annual_income <= 36900:
        N = 0.1*(9076 - 0) + 0.15*(annual_income - 9076)
        print('Tax amount: ', N)
    elif 36901 <= annual_income <= 89350:
        N = 0.1*(9076 - 0) + 0.15*(36901 - 9076) + 0.25*(annual_income - 36901)
        print('Tax amount: ', N)
    elif 89351 <= annual_income <= 186350:
        N = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28*(annual_income - 89351)
        print('Tax amount: ', N)
    elif 186351 <= annual_income <= 405100:
        N = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33*(annual_income - 186351)
        print('Tax amount: ', N)
    elif 405101<= annual_income <= 406750:
        N = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    405101 - 186351) + 0.35 * (annual_income - 405101)
        print('Tax amount: ', N)
    else:
        N = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                405101 - 186351) + 0.35 * (406751 - 405101) + 39.6 * (annual_income - 406751)
        print('Tax amount:', N)
elif status == 'married couple':
    if 0 <= annual_income <= 18150:
        N = 0.1 * (annual_income - 0)
        print('Tax amount: ', N)
    elif 18151 <= annual_income <= 73800:
        N = 0.1 * (18151 - 0) + 0.15 * (annual_income - 18151)
        print('Tax amount: ', N)
    elif 73801 <= annual_income <= 148850:
        N = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (annual_income - 73801)
        print('Tax amount: ', N)
    elif 148851 <= annual_income <= 226850:
        N = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (annual_income - 148851)
        print('Tax amount: ', N)
    elif 226851 <= annual_income <= 405100:
        N = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (
                    annual_income - 226851)
        print('Tax amount: ', N)
    elif 405101 <= annual_income <= 457600:
        N = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (
                    405101 - 226851) + 0.35 * (annual_income - 405101)
        print('Tax amount: ', N)
    else:
        N = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (
                    405101 - 226851) + 0.35 * (457601 - 405101) + 39.6 * (annual_income - 457601)
        print('Tax amount: ', N)
