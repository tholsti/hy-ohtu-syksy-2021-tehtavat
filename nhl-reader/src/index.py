import requests
from player import Player

def sort_by_points(e):
    return e.goals + e.assists

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games'],
        )

        if (player.nationality == "FIN"):
            players.append(player)

    players.sort(key=sort_by_points, reverse=True)

    print("Oliot:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
