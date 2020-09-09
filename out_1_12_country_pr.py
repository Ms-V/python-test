def print_country(city,county,pop=''):
    if pop:
        allinfo=city+' '+county+' '+'population is '+str(pop)
    else:
        allinfo=city+' '+county
    return allinfo