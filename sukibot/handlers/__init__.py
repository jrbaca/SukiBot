class HandlerInput:

    def __init__(self, message: str):
        self._handler_response = HandlerResponse()
        self.message: str = message

    def get_handler_response(self):
        return self._handler_response


class HandlerResponse:
    def __init__(self):
        self.message = None

    def with_message(self, message: str) -> 'HandlerResponse':
        self.message = message
        return self


class BaseIntent:

    def can_handle(self, handler_input: HandlerInput) -> bool:
        raise NotImplementedError

    def handle(self, handler_input: HandlerInput) -> HandlerResponse:
        raise NotImplementedError
