######################################################################################
# Created by: Joel Anderton
# Created date: 3/2/2023
#
# Purpose: uses a weighted coin flip to pick the March Madness bracket for all 67 games
#######################################################################################
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
    for team in round_winners:
        #print(round)
        for match in matches:
            round_next.append({team: match[team]})
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


stop_final_four = 0
count = 0
while stop_final_four < 12:
    count += 1
    # West Matches
    first_four_west = [{'Arisona St.': 11, 'Nevada': 11}]
    ff_west_winner = march_madness(first_four_west)
    matches_west = [{'Kanasas': 1, 'Howard': 16},
                    {'Arkansas': 8, 'Illinois': 9},
                    {'St. Marys': 5, 'VCU': 12},
                    {'UConn': 4, 'Iona': 13},
                    {'TCU': 6, **ff_west_winner[1][0]},
                    {'Gonzaga': 3, 'Grand Canyon':14},
                    {'Northwestern': 7, 'Boise St.': 10},
                    {'UCLA': 2, 'UNC Asheville': 15}]

    # East Matches
    first_four_east = [{'Texas Southern': 16, 'F. Dickinson': 16}]
    ff_east_winner = march_madness(first_four_east)
    matches_east = [{'Purdue': 1, **ff_east_winner[1][0]},
                    {'Memphish': 8, 'Florida Atlantic': 9},
                    {'Duke': 5, 'Oral Roberts': 12},
                    {'Tennessee': 4, 'Louisiana': 13},
                    {'Kentucky': 6, 'Providence': 11},
                    {'Kansas St.': 3, 'Montana St.':14},
                    {'Michigan St.': 7, 'USC': 10},
                    {'Marquette': 2, 'Vermont': 15}]
    # South Matches
    first_four_south = [{'Texas A&M-CC': 16, 'SE Missouri St.': 16}]
    ff_south_winner = march_madness(first_four_south)
    matches_south = [{'Alabama': 1, **ff_south_winner[1][0]},
                     {'Maryland': 8, 'West Virginia': 9},
                     {'San Diego St.': 5, 'Charleston': 12},
                     {'Virginia': 4, 'Furman': 13},
                     {'Creighton': 6, 'NC State': 11},
                     {'Baylor': 3, 'UCSB':14},
                     {'Missouri': 7, 'Utah St.': 10},
                     {'Arizona': 2, 'Princeton': 15}]

    # Midwest Matches
    first_four_mw = [{'Mississippi St.': 11, 'Pittsburgh': 11}]
    ff_mw_winner = march_madness(first_four_mw)
    matches_mw = [{'Houston': 1, 'Northern Ky.': 16},
                  {'Iowa': 8, 'Auburn': 9},
                  {'Miami': 5, 'Drake': 12},
                  {'Indiana': 4, 'Kent St.': 13},
                  {'Iowa St.': 6, **ff_mw_winner[1][0]},
                  {'Xavier': 3, 'Kennesaw St.':14},
                  {'Texas A&M': 7, 'Penn St.': 10},
                  {'Texas': 2, 'Colgate': 15}]

    print('First Four - Winners:')
    print('West -', ff_west_winner[0][0])
    print('East -', ff_east_winner[0][0])
    print('South -', ff_south_winner[0][0])
    print('Midwest -', ff_mw_winner[0][0])


    ## Round 1
    round_1_winners_west = march_madness(matches_west)
    round_1_winners_east = march_madness(matches_east)
    round_1_winners_south = march_madness(matches_south)
    round_1_winners_mw = march_madness(matches_mw)

    # Check for at least one 5 seed vs. 12 seed upset
    if  round_1_winners_west[0][2] == 'VCU' or  round_1_winners_east[0][2] == 'Oral Roberts' or round_1_winners_south[0][2] == 'Charleston' or round_1_winners_mw[0][2] == 'Drake':
        print()
        print('Round 2:')
        print_winners('West', round_1_winners_west)
        print_winners('East', round_1_winners_east)
        print_winners('South', round_1_winners_south)
        print_winners('MidWest', round_1_winners_mw)

        ## Round 2
        round_2_matches_west = round2(round_1_winners_west)
        round_2_matches_east = round2(round_1_winners_east)
        round_2_matches_south = round2(round_1_winners_south)
        round_2_matches_mw = round2(round_1_winners_mw)
        round_2_winners_west = march_madness(round_2_matches_west)
        round_2_winners_east = march_madness(round_2_matches_east)
        round_2_winners_south = march_madness(round_2_matches_south)
        round_2_winners_mw = march_madness(round_2_matches_mw)
        print()
        print('Round 3:')
        print_winners('West', round_2_winners_west)
        print_winners('East', round_2_winners_east)
        print_winners('South', round_2_winners_south)
        print_winners('MidWest', round_2_winners_mw)

        ## Round 3
        round_3_matches_west = round3(round_2_winners_west)
        round_3_matches_east = round3(round_2_winners_east)
        round_3_matches_south = round3(round_2_winners_south)
        round_3_matches_mw = round3(round_2_winners_mw)
        round_3_winners_west = march_madness(round_3_matches_west)
        round_3_winners_east = march_madness(round_3_matches_east)
        round_3_winners_south = march_madness(round_3_matches_south)
        round_3_winners_mw = march_madness(round_3_matches_mw)
        print()
        print('Round 4 - Elite 8:')
        print_winners('West', round_3_winners_west)
        print_winners('East', round_3_winners_east)
        print_winners('South', round_3_winners_south)
        print_winners('MidWest', round_3_winners_mw)

        ## Round 4
        round_4_matches_west = round4(round_3_winners_west)
        round_4_matches_east = round4(round_3_winners_east)
        round_4_matches_south = round4(round_3_winners_south)
        round_4_matches_mw = round4(round_3_winners_mw)
        round_4_winners_west = march_madness(round_4_matches_west)
        round_4_winners_east = march_madness(round_4_matches_east)
        round_4_winners_south = march_madness(round_4_matches_south)
        round_4_winners_mw = march_madness(round_4_matches_mw)
        print()
        print('Round 5 - Final 4:')
        print_winners('West', round_4_winners_west)
        print_winners('East', round_4_winners_east)
        print_winners('South', round_4_winners_south)
        print_winners('MidWest', round_4_winners_mw)

        # check that at least 1 team in the Final Four is a 1 seed and that the total of the Final Four seeds >=12
        if round_4_winners_west[1][0][round_4_winners_west[0][0]] == 1 or round_4_winners_east[1][0][round_4_winners_east[0][0]] == 1 or round_4_winners_south[1][0][round_4_winners_south[0][0]] == 1 or round_4_winners_mw[1][0][round_4_winners_mw[0][0]] == 1:
            stop_final_four = (round_4_winners_west[1][0][round_4_winners_west[0][0]] +
                               round_4_winners_east[1][0][round_4_winners_east[0][0]] +
                               round_4_winners_south[1][0][round_4_winners_south[0][0]] +
                               round_4_winners_mw[1][0][round_4_winners_mw[0][0]])

        ## Round 5 - Semifinals
        round5_matches_left = round4([[round_4_winners_south[0][0], round_4_winners_east[0][0]], [round_4_winners_south[1][0], round_4_winners_east[1][0]]])
        round5_winners_left = march_madness(round5_matches_left)
        round5_matches_right = round4([[round_4_winners_mw[0][0], round_4_winners_west[0][0]], [round_4_winners_mw[1][0], round_4_winners_west[1][0]]])      
        round5_winners_right = march_madness(round5_matches_right)
        print()
        print('Round 6 - Semi-Finals:')
        print_winners('Left', round5_winners_left)
        print_winners('Right', round5_winners_right)

        # Round 6 - Final
        print('Round 7 - Finals:')
        round6_match = round4([[round5_winners_left[0][0], round5_winners_right[0][0]], [round5_winners_left[1][0], round5_winners_right[1][0]]])
        round6_winner = march_madness(round6_match)
        print_winners('WINNER!!', round6_winner)

print('Done!')
print('Sum of Final Four Seeds:', stop_final_four)
print('Number of interations:', count)
