from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, All, Not, HasAtLeast, HasFewerThan, PlaysIn, QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query_builder = QueryBuilder()
    query = query_builder.playsIn("NYR").hasAtLeast(5, 'goals').build()

    for player in stats.matches(query):
        print(player)

if __name__ == "__main__":
    main()
