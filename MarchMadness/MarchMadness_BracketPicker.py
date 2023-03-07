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
        flips = [random.choice(['H', 'T']) for i in range(17)]
        print(match)
        print(flips)
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
                print('Winner is:', team1)
                round_winners.append(team1)
                break
            if match[team2] == num_T:
                print('Winner is:', team2)
                round_winners.append(team2)
                break
    return round_winners



matches = [{'Gonzaga': 1, 'Gorgia St': 16},
           {'Boise St': 8, 'Memphis': 9},
           {'UConn': 5, 'New Mexico': 12},
           {'Arkansas': 4, 'Vermont': 13},
           {'Alabama': 6, 'Rutgers': 11},
           {'Texas Tech': 3, 'Montan St':14},
           {'Michigan St':7, 'Daivdson': 10},
           {'Duke':2, 'Cal St Fullerton':15}]


## Round 1
round_1_winners = march_madness(matches)
print()
print('Round 1 Winners')
round2 = []
for round1 in round_1_winners:
    print(round1)
    for match in matches:
        round2.append({round1 : match[round1]})
        matches.pop(0)
        break
    continue
    

print(round2)
round2_matches = [{**round2[0], **round2[1]},
                  {**round2[2], **round2[3]},
                  {**round2[4], **round2[5]},
                  {**round2[6], **round2[7]}]

print(round2_matches)

## Round 2
round_2_winners = march_madness(round2_matches)
print()
print('Round 2 Winners')
round3 = []
for round2 in round_2_winners:
    print(round2)
    for round2_match in round2_matches:
        round3.append({round2 : round2_match[round2]})
        round2_matches.pop(0)
        break
    continue

print(round3)
round_3_matches = [{**round3[0], **round3[1]},
                   {**round3[2], **round3[3]}]
print(round_3_matches)
        
## Round 3
round_3_winners = march_madness(round_3_matches)
print()
print('Round 3 Winners - Sweet 16')
round4 = []
for round3 in round_3_winners:
    print(round3)
    for round3_match in round_3_matches:
        round4.append({round3: round3_match[round3]})
        round_3_matches.pop(0)
        break
    continue

print(round4)
round_4_matches = [{**round4[0], **round4[1]}]
print(round_4_matches)


## Round 4
round_4_winners = march_madness(round_4_matches)
print()
print('Round 4 Winners - Elite 8')
round5 = []
for round4 in round_4_winners:
    print(round4)
    for round4_match in round_4_matches:
        round5.append({round4: round4_match[round4]})
        round_4_matches.pop(0)
        break
    continue

print(round5)
round4 = [{**round5[0]}]
print(round5)