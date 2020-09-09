from out_1_12_country_pr import print_country as pr
while True:
    city=input('City:')
    if city=='q':
        break
    county=input('county:')
    if county=='q':
        break
    pop=input('population:')
    if pop=='q':
        break
    allinfo=pr(city,county,pop)
    print(allinfo)