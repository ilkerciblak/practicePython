#region Task
'''
→ Explanation:
    An arcade game player wants to climb to the top of the
    leaderboard and track their ranking. The game uses Dense Ranking, so leaderboard works
    like:
    
    •The player with highest score is ranked number 1.
    •Player who have equal scores receive the same ranking number, and the next player(s) 
    recieve the immediately following ranking number.
---------------------------
→ Example:
    ranked = [100, 90, 90, 80]
    player = [70, 80, 105]

    The ranked players will have ranks 1, 2, 2, and 3 respectively. If the player's score are
    70, 80, 105, their rankings after each game are 4th 3rd and 1st. Thus return [4, 3, 1]

----------------------------
→ Input Format:
    •The 1st line contains an integer n, the number of players on the leaderboard already.
    •The 2nd line contains n space-separated integers ranked[i], the leaderboard scores in decreasing order.
    •The 3rd line contains an integer m, the number of games the player plays.
    •The 4th line contains m space-separated integers player[j], the each game's score.

→ Returns:
    •int[m]: the player's rank after each new score

'''
#endregion


def climbingLeaderboard(ranked, player):
    leaderBoardScoresSet = set(ranked)
    leaderBoardScoresList = sorted(list(leaderBoardScoresSet))
    ranks = []
    for playerScore in player:
        leaderBoardScoresList.append(playerScore)
        ranks.append(sorted(leaderBoardScoresList, reverse=True).index(playerScore)+1)
    
    return ranks
    '''
    for playerScore in player:
        for rank,rankedScore in enumerate(leaderBoardScoresList):
            if playerScore > rankedScore:
                continue
            ranks.append(len(leaderBoardScoresList)-rank)
    return ranks
  
    while kullandığın bir çözüm bulman gerek, alice her seferinde daha iyi bir skor yapıyor unutma
    '''
if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))