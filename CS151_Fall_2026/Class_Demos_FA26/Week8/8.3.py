ballroom = ['Miss Scarlet', 'Mr. Green', 'Prof Plum']
hall = ['Mrs. Peacock', 'Col. Mustard']
study = ['Mrs. White']
house = [ballroom, hall, study]
hall  += study
for character in ballroom:
    if character[0] == 'P':
        house[1][0] = character
print("*"* 10)
print(hall)