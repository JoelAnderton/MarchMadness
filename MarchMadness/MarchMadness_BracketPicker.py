#########################################################################
# Created by: Joel Anderton
# Created date: 3/2/2023
#
# Purpose: to randomly pick the March Madness bracket for all 67 games
#########################################################################
import random

### Weighted Coin Flip
def march_madness(matches):
    round_winners = []
    for match in matches:
        flips = [random.choice(['H', 'T']) for i in range(33)]
        #print(match)
        #print(flips)
        num_H = 0
        num_T = 0
        team1 = list(match.keys())[0]
        team2 = list(match.keys())[1]
        for flip in flips:
            if flip == 'H':
                num_H += 1
            else:
                num_T += 1
            if match[team1] == num_H:
                #print('Winner is:', team1)
                round_winners.append(team1)
                break
            elif match[team2] == num_T:
                #print('Winner is:', team2)
                round_winners.append(team2)
                break

    round_next = []
    for round in round_winners:
        #print(round)
        for match in matches:
            round_next.append({round : match[round]})
            matches.pop(0)
            break
        continue
    return [round_winners, round_next]


def round2(round_1_winners):
    round_2_matches = [{**round_1_winners[1][0], **round_1_winners[1][1]},
                       {**round_1_winners[1][2], **round_1_winners[1][3]},
                       {**round_1_winners[1][4], **round_1_winners[1][5]},
                       {**round_1_winners[1][6], **round_1_winners[1][7]}]
    return round_2_matches

def round3(round_2_winners):
    round_3_matches = [{**round_2_winners[1][0], **round_2_winners[1][1]},
                       {**round_2_winners[1][2], **round_2_winners[1][3]}]
    return round_3_matches

def round4(round_3_winners):
    round_4_matches = [{**round_3_winners[1][0], **round_3_winners[1][1]}]
    return round_4_matches

def print_winners(region, winners):
    print(region)
    for team in winners[0]:
        print(team)
    print()

# West Matches
first_four_west = [{'Rutgers': 11, 'Notre Dame': 11}]
ff_west_winner = march_madness(first_four_west)
matches_west = [{'Gonzaga': 1, 'Gorgia St.': 16},
                {'Boise St.': 8, 'Memphis': 9},
                {'UConn': 5, 'New Mexico': 12},
                {'Arkansas': 4, 'Vermont': 13},
                {'Alabama': 6, **ff_west_winner[1][0]},
                {'Texas Tech': 3, 'Montan St.':14},
                {'Michigan St': 7, 'Daivdson': 10},
                {'Duke': 2, 'Cal St Fullerton': 15}]

# East Matches
first_four_east = [{'Wyoming': 12, 'Indiana': 12}]
ff_east_winner = march_madness(first_four_east)
matches_east = [{'Baylor': 1, 'Norfolk': 16},
                {'North Carolina': 8, 'Marquette': 9},
                {'St. Marys': 5, **ff_east_winner[1][0]},
                {'UCLA': 4, 'Akron': 13},
                {'Texas': 6, 'Virginia Tech': 11},
                {'Purdue': 3, 'Yale':14},
                {'Murray St.': 7, ' San Francisco': 10},
                {'Kentucky': 2, 'St. Peters': 15}]
# South Matches
first_four_south = [{'Wright St.': 16, 'Bryant': 16}]
ff_south_winner = march_madness(first_four_south)
matches_south = [{'Arizona': 1, **ff_south_winner[1][0]},
                 {'Seton Hall': 8, 'TCU': 9},
                 {'Huston': 5, 'UAB': 12},
                 {'Illinois': 4, 'Chattanooga': 13},
                 {'Colorado St.': 6, 'Michigan': 11},
                 {'Tennessee': 3, 'Longwood':14},
                 {'Ohio St': 7, 'Loyola': 10},
                 {'Villanova': 2, 'Delaware': 15}]

# Midwest Matches
first_four_mw = [{'Texas Southern': 16, 'Texas A&M': 16}]
ff_mw_winner = march_madness(first_four_mw)
matches_mw = [{'Kansas': 1, **ff_mw_winner[1][0]},
              {'San Diego St.': 8, 'Creighton': 9},
              {'Iowa': 5, 'Richmond': 12},
              {'Providence': 4, 'South Dakota St.': 13},
              {'LSU': 6,'Iowa St.': 11},
              {'Wisconsin': 3, 'Colgate':14},
              {'USC': 7, 'Miami': 10},
              {'Auburn': 2, 'Jacksonville St.': 15}]

print('First Four - Winners:')
print('West -', ff_west_winner[0][0])
print('East -',ff_east_winner[0][0])
print('South -',ff_south_winner[0][0])
print('Midwest -',ff_mw_winner[0][0])
 
## Round 1
round_1_winners = march_madness(matches_west)
print()
print('Round 2:')
print_winners('West', round_1_winners)
 
## Round 2
round_2_matches = round2(round_1_winners)
round_2_winners = march_madness(round_2_matches)
print()
print('Round 3:')
print_winners('West', round_2_winners)

## Round 3
round_3_matches = round3(round_2_winners)
round_3_winners = march_madness(round_3_matches)
print()
print('Round 4 - Elite 8:')
print_winners('West', round_3_winners)
    
## Round 4
round_4_matches = round4(round_3_winners)
round_4_winners = march_madness(round_4_matches)
print()
print('Round 5 - Final 4:')
print_winners('West', round_4_winners)

