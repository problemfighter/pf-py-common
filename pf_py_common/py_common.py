import uuid


class PyCommon:

    @staticmethod
    def uuid() -> str:
        unique_id = str(uuid.uuid1())
        return unique_id.upper()
