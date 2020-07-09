
def perc_to_grade(perc):
    if perc >= 91:
        return 'AA'
    elif perc < 91 and perc >= 81:
        return 'AB'
    elif perc < 81 and perc >= 71:
        return 'BB'
    elif perc < 71 and perc >= 61:
        return 'BC'
    elif perc < 61 and perc >= 51:
        return 'CC'
    elif perc < 51 and perc >= 41:
        return 'CD'
    elif perc < 41 and perc >= 31:
        return 'DD'
    elif perc < 31 and perc >= 0:
        return 'F'
    else:
        return 'undefined'

def get_sub_grade(results):
    perc_sum = 0
    for res in results:
        perc_sum += res.get_contribution()
    return perc_to_grade(perc_sum)


        

