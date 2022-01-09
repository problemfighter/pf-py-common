from pf_py_common.pf_exception import PFException


def throw_exception():
    raise PFException("Something went wrong", "EXAMPLE") \
        .other_info(code="120", additional_info={"key": "value"}) \
        .add_additional_info("other", "value")


def handle_error():
    try:
        throw_exception()
    except PFException as e:
        print("Message: " + e.message)
        print("Code: " + e.code)
        print("Exception type: " + e.exception_type)
        print("Additional Information :")
        print(e.additional_info)


if __name__ == '__main__':
    handle_error()
