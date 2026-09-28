
def is_failing(grade):
    return grade >= 60
       


def can_ski_today(is_sunny, is_snowing):
    return is_sunny and not is_snowing


def is_in_zone(x, left_edge, right_edge):
    return left_edge < x < right_edge
    

def is_milan_event(venue_name):
    """Checking if venue is in the city of Milan"""
    if venue_name == 'Milan Speed Skating Area':
        return True
    elif venue_name == 'Milan Hockey Forum':
        return True
    elif venue_name == 'Olympic Stadium of Milan':
        return True
    else:
        return False
