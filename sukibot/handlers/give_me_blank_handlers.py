from sukibot.handlers import BaseIntent, HandlerInput, HandlerResponse
import random

def gamePickerlol():
    gameList = ["valorant", "overwatch", "apex", "minecraft","sea of theives", "rocket league", "valheim", "borderland 3", "phasmaphobia", "overcooked 2", "mario kart", "factorio", "don't starve"]
    game = random.choice(gameList)
    return(game)

class GiveMeSomethingIntent(BaseIntent):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return handler_input.message == "pick a game for me"

    def handle(self, handler_input: HandlerInput) -> HandlerResponse:
        response = handler_input.get_handler_response()
        return response.with_message("you should play: " + gamePickerlol())



