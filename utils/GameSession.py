
gamesession = None

class GameSession():
    def __init__(self):
        self.uid = 0 # something random
        self.date = None #current date
        self.mimo_machine_id = 0 # machine id

        self.news_played = []
        self.score = 0
        self.results = []

def new_game_session():
    gamesession = GameSession()

def close_session():
    pass

def save_results(news_results):
    self.results += news_results
