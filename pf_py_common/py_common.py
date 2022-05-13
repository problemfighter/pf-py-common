import sys
import uuid
from pf_py_common.pf_exception import PFException


class PyCommon:

    @staticmethod
    def uuid() -> str:
        unique_id = str(uuid.uuid1())
        return unique_id.upper()

    @staticmethod
    def get_random(length=12) -> str:
        unique_id = PyCommon.uuid()
        unique_id = unique_id.replace("-", "")
        unique_id = unique_id[:length]
        return unique_id.lower()

    @staticmethod
    def import_from_string(import_name: str, silent: bool = False):
        if not import_name:
            return None
        import_name = import_name.replace(":", ".")
        try:
            try:
                __import__(import_name)
            except ImportError:
                if "." not in import_name:
                    raise
            else:
                return sys.modules[import_name]

            module_name, obj_name = import_name.rsplit(".", 1)
            module = __import__(module_name, globals(), locals(), [obj_name])
            try:
                if hasattr(module, obj_name):
                    return getattr(module, obj_name)
            except AttributeError as e:
                raise ImportError(e)

        except ImportError as e:
            if not silent:
                error = "Emport Name: " + import_name
                error += "\n" + str(e)
                raise PFException(error)

        return None
