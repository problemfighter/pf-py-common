class PFException(Exception):
    exception_type: str = None
    message = None
    additional_info: dict = None
    code: str = None
    data: any = None

    def __init__(self, message=None, exception_type: str = None):
        super().__init__(message)
        self.exception_type = exception_type
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

    def add_data(self, data: any):
        self.data = data
        return self
