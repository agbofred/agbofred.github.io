from manifest import MANIFEST
# print("Original Manifest", len(MANIFEST))

new_passengers= ['Bill Yu', 43, '15C', 'Jackie Yu', 39, '15B', 'Hayden Yu', 12, '15A']

MANIFEST += new_passengers


def is_seat_available(seat, full_manifest):
    """Predicate function to determine if a seat is available.

    Args:
        seat (str): The seat number and letter to check
        full_manifest (list): The full passenger manifest

    Returns:
        (bool): Whether the target seat is currently unoccupied
    """
    target_seat = full_manifest[2::3]
    return seat not in target_seat

def avg_age_window_seats(full_manifest):
    """Computes the average age of all individuals in a window seat.

    Args:
        full_manifest (list):The full passenger manifest

    Returns:
        (float): The average age
    """
    count = 0
    ages = 0
    for i in range(0, len(full_manifest), 3):
        name = full_manifest[i]
        age = full_manifest[i+1]
        seat = full_manifest[i+2]
        if seat[-1] == "A" or seat[-1] == "F":
            ages += age
            print(ages)
            count +=1
    average_age = ages/count
    return average_age

def test_is_seat_available():
    """Some checks for the is_seat_available function"""
    assert not is_seat_available("24A", MANIFEST)
    assert not is_seat_available("8F", MANIFEST)
    assert is_seat_available("22D", MANIFEST)
    assert is_seat_available("16E", MANIFEST)


if __name__ == "__main__":
    print(is_seat_available("10A", MANIFEST))
    # test_is_seat_available()
    # print(avg_age_window_seats(MANIFEST))
    
