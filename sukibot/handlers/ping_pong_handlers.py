from sukibot.handlers import BaseIntent, HandlerInput, HandlerResponse


class PingPongIntent(BaseIntent):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return handler_input.message == "ping!"

    def handle(self, handler_input: HandlerInput) -> HandlerResponse:
        response = handler_input.get_handler_response()
        return response.with_message("pong!")
