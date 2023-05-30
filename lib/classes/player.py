class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception 
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
        pass
    
    def played_game(self, game):
        if game in self._games_played:
            return True 
        else:
            return False
        pass
    
    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])
        pass
    
    @classmethod
    def highest_scored(cls, game):
            if cls.all:
                highest_player = None
                highest_score = 0
                for player in cls.all:
                    if game.average_score(player) > highest_score:
                        highest_player = player
                        highest_score = game.average_score(player)
                    return highest_player
                return None

        
