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
    # first_four_west = [{'Al': 16, 'Wagner': 16}]
    # ff_west_winner = march_madness(first_four_west)
    matches_west = [{'Florida': 1, 'Norfolk St.': 16},
                    {'UConn': 8, 'Oklahoma': 9},
                    {'Memphis': 5, 'Colorado St.': 12},
                    {'Maryland': 4, 'Grand Canyon': 13},
                    {'Missouri': 6, 'Drake': 11},
                    {'Texas Tech': 3, 'UNC Wilmigton':14},
                    {'Kansas': 7, 'Arkansas': 10},
                    {'St. John': 2, 'Omaha': 15}]

    # East Matches
    first_four_east = [{'American': 16, 'Mt. St.Marys': 16}]
    ff_east_winner = march_madness(first_four_east)  
    matches_east = [{'Duke': 1, **ff_east_winner[1][0]},
                    {'Mississippi St.': 8, 'Baylor': 9},
                    {'Oregon': 5, 'Liberty': 12},
                    {'Arizona': 4, 'Akron': 13},
                    {'BYU': 6, 'VCU': 11},
                    {'Wisconsin': 3, 'Montana':14},
                    {'St. Marys': 7, 'Vanderbil': 10},
                    {'Alabama': 2, 'Robert Morris': 15}]
    # South Matches
    # first_four_south = [{'Alabama St.': 10, 'St. Franscis': 10}] --  not needed in 2025
    # ff_south_winner = march_madness(first_four_south)
    matches_south = [{'Auburn': 1, 'Alabama St.': 16},
                     {'Lousiville': 8, 'Creighton': 9},
                     {'Michigan': 5, 'UC San Diego': 12},
                     {'Texas A&M': 4, 'Yale': 13},
                     {'Ole Mills': 6, 'North Caroloina': 11},
                     {'Iowa St.': 3, 'Lipscomb': 14},
                     {'Marquette': 7, 'New Mexico': 10},
                     {'Michigan St.': 2, 'Bryant': 15}]

    # Midwest Matches
    first_four_mw1 = [{'Texans': 11, 'Xavier': 11}]
    ff_mw_winner1 = march_madness(first_four_mw1)
    # first_four_mw2 = [{'Montana St.': 16, 'Grambling': 16}] --  not needed in 2025
    # ff_mw_winner2 = march_madness(first_four_mw2)
    matches_mw = [{'Houston': 1, 'SIU Edwardsvill': 16 },
                  {'Gonzaga': 8, 'Georgia': 9},
                  {'Clemson': 5, 'McNeese': 12},
                  {'Purdue': 4, 'High Point': 13},
                  {'Illinois': 6, **ff_mw_winner1[1][0]},
                  {'Kentucky': 3, 'Troy': 14},
                  {'UCLA': 7, 'Utah St.': 10 },
                  {'Tennessee': 2, 'Wofford': 15}]

    print('First Four - Winners:')
    # print('West -', ff_west_winner[0][0])  -- not needed in 2025
    print('East -', ff_east_winner[0][0]) 
    # print('South -', ff_south_winner[0][0]) -- not needed in 2025
    print('Midwest -', ff_mw_winner1[0][0])
    # print('Midwest 16 seed -', ff_mw_winner2[0][0]) -- not needed in 2025

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
