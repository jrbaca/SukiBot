from sukibot.handlers import BaseIntent, HandlerInput, HandlerResponse


class CreateListIntent(BaseIntent):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return False

    def handle(self, handler_input: HandlerInput) -> HandlerResponse:
        pass
