class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, 'title') and isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception 
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        pass
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
        pass
    
    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0
        pass