class PlayerStats:

    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self.players:
            if (player.nationality == nationality):
                players.append(player)

        return sorted(players, key=lambda player : player.get_points(), reverse=True)
