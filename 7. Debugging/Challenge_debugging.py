# Debug this program

def plant_recommendation(care):
    if care = 'low':  # This Error is Synatx Error The equal sign (=) mean assignemnt the value of RHS to LHS but it must be a double equal (==) for equality
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'medium': # This Error is a Logic Error care == 'medium' must be care == 'high'
        print('orchid')

plant_rec('low') # This Error is a RunTime Error function name isn't complete it must be plant_recommendation
plant_recommendation('medium')
plant_recommendation('high')

