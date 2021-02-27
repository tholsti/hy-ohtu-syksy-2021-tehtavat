SCORE = [
    'Love',
    'Fifteen',
    'Thirty',
    'Forty'
]

GAME_WINNER_POINT = 4
DIFF_NEEDED_TO_WIN = 2

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.leader = None

    def _set_leader(self):
        leader = self.player1
        if self.player2.get_points() == self.player1.get_points():
            leader = None
        if self.player2.get_points() > self.player1.get_points():
            leader = self.player2
        self.leader = leader

    def _get_score_when_even(self):
        if (self.player1.get_points() >= GAME_WINNER_POINT):
            return 'Deuce'
        else:
            return f'{SCORE[self.player1.get_points()]}-All'
    
    def _get_score_after_winner_point(self):
        if abs(self.player1.get_points() - self.player2.get_points()) >= DIFF_NEEDED_TO_WIN:
            return f"Win for {self.leader.get_name()}"
        else:
            return f"Advantage {self.leader.get_name()}"
    
    def won_point(self, player):
        player.add_point()
        self._set_leader()

    def get_score(self):
        if not self.leader:
            return self._get_score_when_even()
        
        elif self.leader.get_points() >= GAME_WINNER_POINT:
            return self._get_score_after_winner_point()

        else:
            return f"{SCORE[self.player1.get_points()]}-{SCORE[self.player2.get_points()]}"
