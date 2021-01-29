import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    
    def test_finds_player(self):
        player = self.statistics.search('Kurri')
        self.assertEqual(player.name, 'Kurri')
    
    def test_returns_none_if_player_not_found(self):
        player = self.statistics.search('Raipe')
        self.assertEqual(player, None)

    def test_finds_team(self):
        team = self.statistics.team('EDM')
        self.assertEqual(len(team), 3)
        self.assertTrue(any(player.name == 'Semenko' for player in team))

    def test_top_scorers_are_sorted(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertEqual(top_scorers[0].name, 'Gretzky')
        self.assertEqual(top_scorers[1].name, 'Lemieux')
