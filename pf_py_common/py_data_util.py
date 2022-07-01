import inspect


class PyDataUtil:

    @staticmethod
    def get_dict_value(data: dict, key: str, default=None):
        if not data or not key:
            return default
        elif key in data:
            return data[key]
        return default

    @staticmethod
    def copy_dict_to_object(dictionary: dict, data_object: object):
        if dictionary and data_object:
            for dict_key in dictionary:
                value = dictionary[dict_key]
                if hasattr(data_object, dict_key):
                    setattr(data_object, dict_key, value)
        return data_object

    @staticmethod
    def get_object_fields(data_object: object):
        fields = []
        for field in dir(data_object):
            if not field.startswith('__'):
                fields.append(field)
        return fields

    @staticmethod
    def copy_object_to_object(source_object: object, dst_object: object):
        fields = PyDataUtil.get_object_fields(dst_object)
        if fields and source_object:
            for field in fields:
                if hasattr(source_object, field):
                    setattr(dst_object, field, getattr(source_object, field))
        return dst_object

    @staticmethod
    def get_class_attrs(class_or_object) -> dict:
        name_and_type = {}
        for attrs in inspect.getmembers(class_or_object):
            if len(attrs) == 2 and attrs[0] == "__annotations__":
                for attr_name in attrs[1]:
                    name_and_type[attr_name] = attrs[1][attr_name].__name__
                break
        return name_and_type
