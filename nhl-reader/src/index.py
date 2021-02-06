from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    
    players = reader.get_players()
    stats = PlayerStats(players)

    finnish_top_scorers = stats.top_scorers_by_nationality('FIN')

    for player in finnish_top_scorers:
        print(player)

if __name__ == "__main__":
    main()
