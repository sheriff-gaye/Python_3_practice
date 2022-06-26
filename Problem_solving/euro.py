
def uefa_euro_2016(teams, scores):
    for i in teams:
        first=teams[0]
        second=teams[1]
    for i in scores:
        if scores[0]>scores[1]:
            return('At match {} - {}, {} won!'.format(first,second,first))
        
        elif(scores[0]<scores[1]):
            return('At match {} - {}, {} won!'.format(first,second,second))

        else:
            return ('At match Republic of {} - {}, teams played draw.'.format(first,second))
    




print(uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]))
print(uefa_euro_2016(['Nigeria', 'Ghana'],[0, 2]))
print(uefa_euro_2016(['Gambia', 'Ukraine'],[0, 0]))