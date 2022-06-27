#!/usr/bin/python3

#UEFA EURO 2016 RESULTS

def uefa_euro_2016(teams, scores):

    first = teams[0]
    second = teams[1]

    if (scores[0] > scores[1]):
        return('At match {} - {}, {} won!'.format(first, second, first))

    elif(scores[0] < scores[1]):
        return('At match {} - {}, {} won!'.format(first, second, second))

    else:
        return ('At match  {} - {}, teams played draw.'.format(first, second))


print(uefa_euro_2016(['Gambia', 'Senegal'], [2, 0]))
print(uefa_euro_2016(['Nigeria', 'Ghana'], [0, 2]))
print(uefa_euro_2016(['Gambia', 'Ukraine'], [0, 0]))
