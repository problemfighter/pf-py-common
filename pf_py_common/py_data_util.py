class PyDataUtil:

    @staticmethod
    def get_dict_value(data: dict, key: str, default=None):
        if not data or not key:
            return default
        elif key in data:
            return data[key]
        return default
