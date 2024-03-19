######################################################################################
# Created by: Joel Anderton
# Created date: 3/2/2023
#
# Purpose: uses a weighted coin flip to pick the March Madness bracket for all 67 games
#
# - Checks:
#    - Must have at least one 5 seed vs. 12 seed upset
#    - Must have at least one 1 seed in the Final Four
#    - The sum of the seeds in the Final Four must be >= 12
#######################################################################################
import random

### Weighted Coin Flip
def march_madness(matches):
    round_winners = []
    for match in matches:
        flips = [random.choice(['H', 'T']) for i in range(37)]
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
    first_four_west = [{'Howard': 16, 'Wagner': 16}]
    ff_west_winner = march_madness(first_four_west)
    matches_west = [{'North Carolina': 1, **ff_west_winner[1][0]},
                    {'Mississippi St.': 8, 'Michigan St.': 9},
                    {'St. Marys': 5, 'Grand Canyon': 12},
                    {'Alabama': 4, 'Charleston': 13},
                    {'Clemson': 6, 'New Mexico': 11},
                    {'Baylor': 3, 'Colgate':14},
                    {'Dayton': 7, 'Nevada': 10},
                    {'Arizona': 2, 'Long Beach St.': 15}]

    # East Matches
    #first_four_east = [{'Texas Southern': 16, 'F. Dickinson': 16}]
    #ff_east_winner = march_madness(first_four_east) -- not needed in 2024
    matches_east = [{'UConn': 1, 'Stetson':16},
                    {'Florida Atlantic': 8, 'Northwestern': 9},
                    {'San Diego St.': 5, 'UAB': 12},
                    {'Auburn': 4, 'Yale': 13},
                    {'BYU': 6, 'Duquesene': 11},
                    {'Illinois': 3, 'Morehead St.':14},
                    {'Washington St.': 7, 'Drake': 10},
                    {'Iowa St.': 2, 'South Dakota St.': 15}]
    # South Matches
    first_four_south = [{'Boise St.': 10, 'Colorado': 10}]
    ff_south_winner = march_madness(first_four_south)
    matches_south = [{'Houston': 1, 'Longwood': 16},
                     {'Nebraska': 8, 'Texas A&M': 9},
                     {'Wisconsin': 5, 'James Madison': 12},
                     {'Duke': 4, 'Vermont': 13},
                     {'Texas Tech': 6, 'NC State': 11},
                     {'Kentucky': 3, 'Oakland': 14},
                     {'Florida': 7, **ff_south_winner[1][0]},
                     {'Marquette': 2, 'Western Kentucky': 15}]

    # Midwest Matches
    first_four_mw1 = [{'Virginia': 10, 'Colorado St': 10}]
    ff_mw_winner1 = march_madness(first_four_mw1)
    first_four_mw2 = [{'Montana St.': 16, 'Grambling': 16}]
    ff_mw_winner2 = march_madness(first_four_mw2)
    matches_mw = [{'Purdue': 1, **ff_mw_winner2[1][0]},
                  {'Utah St.': 8, 'TCU': 9},
                  {'Gonzaga': 5, 'McNeese': 12},
                  {'Kansas': 4, 'Samford': 13},
                  {'South Carolina': 6, 'Oregon': 11},
                  {'Creighton': 3, 'Akron': 14},
                  {'Texas': 7, **ff_mw_winner1[1][0]},
                  {'Tennessee': 2, 'St. Peters': 15}]

    print('First Four - Winners:')
    print('West -', ff_west_winner[0][0])
  # print('East -', ff_east_winner[0][0]) -- not need in 2024
    print('South -', ff_south_winner[0][0])
    print('Midwest 10 seed -', ff_mw_winner1[0][0])
    print('Midwest 16 seed -', ff_mw_winner2[0][0])

    ## Round 1
    round_1_winners_west = march_madness(matches_west)
    round_1_winners_east = march_madness(matches_east)
    round_1_winners_south = march_madness(matches_south)
    round_1_winners_mw = march_madness(matches_mw)

    # Check for at least one 5 seed vs. 12 seed upset
    if  round_1_winners_west[0][2] == 'Grand Canyon' or  round_1_winners_east[0][2] == 'UAB' or round_1_winners_south[0][2] == 'James Madison' or round_1_winners_mw[0][2] == 'McNeese':
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
        round5_matches_left = round4([[round_4_winners_west[0][0], round_4_winners_east[0][0]], [round_4_winners_west[1][0], round_4_winners_east[1][0]]])
        round5_winners_left = march_madness(round5_matches_left)
        round5_matches_right = round4([[round_4_winners_mw[0][0], round_4_winners_south[0][0]], [round_4_winners_mw[1][0], round_4_winners_south[1][0]]])      
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
