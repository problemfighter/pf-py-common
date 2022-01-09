class PFException(Exception):
    message_type: str = None
    message = None
    additional_info: dict = None
    code: str = None

    def __init__(self, message=None, message_type: str = None):
        super().__init__(message)
        self.message_type = message_type
        self.message = message

    def other_info(self, additional_info: dict = None, code: str = None):
        self.additional_info = additional_info
        self.code = code
        return self

    def add_additional_info(self, key: str, value):
        if not self.additional_info:
            self.additional_info = {}
        if key:
            self.additional_info[key] = value
        return self
