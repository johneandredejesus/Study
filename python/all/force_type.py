from functools import  wraps

class NotValidValueException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ValidateException(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def force_type(method):
    """Forces a valid value type for a method.

    All parameters must be annotated.

    The value type None is not accepted.

    Ex.:  

        @force_type
        def method(self, value: str,  value2: int):
            pass
    """

    @wraps(method)
    def get_value(*args, **kwargs):
        
        annotations_items  = method.__annotations__.items()

        if kwargs.__len__() < annotations_items.__len__():
            raise  ValidateException('All annotated parameters must be called.')

        params_types = tuple(annotations_items)

        params_types_values = tuple((((param_, type_), value_) for (param_, type_) in params_types
                                     for param_kwarg, value_ in kwargs.items() if param_ == param_kwarg))

        for (param_, type_), value_ in params_types_values:
            if value_ is  None or type(value_) is not type_:
                raise NotValidValueException(f'The param {param_} must be of type {type_}.')

        return method(*args, **kwargs)

    return get_value