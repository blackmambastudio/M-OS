from . import constants

gamesession = None

class GameSession():
    def __init__(self):
        self.uid = 0 # something random
        self.date = None #current date
        self.mimo_machine_id = 0 # machine id

        self.news_played = []
        self.score = 0
        self.results = []
        self.time = 60 * constants.SESSION_TIME

        self.alert_displayed = False
        self.current_scene = None
        self.ended = False

    def update(self, dt):
        self.time -= dt
        if self.current_scene and self.time < 61 and not self.alert_displayed:
            self.alert_displayed = True
            self.current_scene.display_timeout_alert()
        if not self.ended and self.time < 0:
            self.current_scene.time_up()
            self.ended = True


def get_game_session():
    global gamesession
    if not gamesession:
        gamesession = GameSession()
    return gamesession

def close_session():
    pass

def save_results(news_results):
    self.results += news_results
