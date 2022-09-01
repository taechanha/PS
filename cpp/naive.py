

class Result:
    def __init__(self, current_rank, best_rank, worst_rank):
        self.current_rank = current_rank
        self.best_rank    = best_rank
        self.worst_rank   = worst_rank

class Player:
    def __init__(self, name):
        self.name = name
        self.totalScore = 0
        self.scoreHistory = dict()

# global vars
players: dict = dict() # { "kim": Player() }
problemToScore: dict = dict() # { "P1": 30 }
SUCCESS = 1
FAIL = 0

def init():
    players: dict = dict()
    problemToScore: dict = dict()

def newPlayer(playerName):
    players[playerName] = Player(name=playerName)

def newProblem(problemName, score):
    problemToScore[problemName] = score

def changeProblemScore(problemName, newScore):
    problemToScore[problemName] = newScore
    for _, player in players.items():
        if problemName in player.scoreHistory:
            oldScore = player.scoreHistory[problemName]
            player.totalScore -= oldScore
            player.totalScore += newScore
            player.scoreHistory[problemName] = newScore

def attemptProblem(playerName, problemName, attemptResult):
    if attemptResult == SUCCESS:
        player = players[playerName]
        score = problemToScore[problemName]
        player.scoreHistory[problemName] = score

def getRank(playerName) -> Result:
    global players
    current_rank: int = getNaiveRank(playerName, players) #
    best_rank: int = getBestRank(playerName) # 풀지 않은 문제 중 본인은 나머지를 모두 맞추고 다른 사람들은 다 틀린 경우
    worst_rank: int = getWorstRank(playerName) # 풀지 않은 문제 중 본인은 나머지를 모두 틀리고 다른 사람들은 다 맞은 경우

    return Result(current_rank, best_rank, worst_rank)

def getNaiveRank(playerName, players: dict) -> int:
    current_rank = 1
    player = players[playerName]
    for _, otherPlayer in players.items():
        if player.name == otherPlayer.name:
            continue
        if otherPlayer.totalScore > player.totalScore:
            current_rank += 1
    return current_rank

def getBestRank(playerName) -> int:
    global players, problemToScore
    targetPlayer = players[playerName]
    # copy players
    temp_players = deepcopy(players)
    print("BEST BEFORE: ", temp_players["seunghyun"].totalScore, temp_players["jinpyo"].totalScore)
    # for each player:
    for _, player in temp_players.items():
        # get player's un-solved problems
        problems = getUnsolvedProblems(player)
        # get their total score
        totalScore = getProblemsTotalScore(problems)
        # if current player
        if targetPlayer.name == player.name:
            # add the total score to player's total score
            player.totalScore += totalScore
        else:
            player.totalScore -= totalScore
    print("BEST BEFORE: ", temp_players["seunghyun"].totalScore, temp_players["jinpyo"].totalScore)
    return getNaiveRank(playerName, temp_players)

def getWorstRank(playerName) -> int:
    global players, problemToScore
    targetPlayer = players[playerName]
    # copy players
    temp_players = deepcopy(players)
    print("WORST BEFORE: ", temp_players["seunghyun"].totalScore, temp_players["jinpyo"].totalScore)
    # for each player:
    for _, player in temp_players.items():
        # get player's un-solved problems
        problems = getUnsolvedProblems(player)
        # get their total score
        totalScore = getProblemsTotalScore(problems)
        # if current player
        if targetPlayer.name == player.name:
            # add the total score to player's total score
            player.totalScore -= totalScore
        else:
            player.totalScore += totalScore
    print("WORST AFTER: ", temp_players["seunghyun"].totalScore, temp_players["jinpyo"].totalScore)
    return getNaiveRank(playerName, temp_players)

def getUnsolvedProblems(player): # -> string
    global players, problemToScore
    totalProblems = problemToScore.keys()
    playerSolvedProblems = player.scoreHistory.keys()
    return list(totalProblems - playerSolvedProblems)

def getProblemsTotalScore(problems):
    totalScore = 0
    for problem in problems:
        totalScore += problemToScore[problem]
    return totalScore

def deepcopy(players: dict):
    temp_players = dict()
    for k, v in players.items():
        p = Player(name=v.name)
        p.totalScore = v.totalScore
        p.scoreHistory = v.scoreHistory.copy()
        temp_players[k] = p
    return temp_players

def pprint(result: Result):
    print("curr: ", result.current_rank)
    print("best: ", result.best_rank)
    print("worst: ", result.worst_rank)

def main():
    init()
    newPlayer("seunghyun")
    newProblem("hardA", 50)
    newProblem("easyA", 10)
    newProblem("mediumA", 30)
    newPlayer("jinpyo")
    result = getRank("jinpyo") # -> return {1, 1, 2}
    pprint(result)

main()