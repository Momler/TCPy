from tcpy_parser.tcpy_attribute import TCPyAttribute
from tcpy_parser.tcpy_file import TCPyFile
from tcpy_exceptions.tcpy_exceptions import InvalidTypeError, InvalidFormatError

class TCPyParser:
    def __init__(self, filename: str):
        self.filename = filename

    def parse(self):
        attributes = []

        valid_types = {"int": int, "str": str, "float": float, "bool": bool, "bytes": bytes}

        with open(self.filename, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                
                if len(parts) == 3:
                    identifier, type_, size_str = parts
                    
                    if type_ not in valid_types:
                        raise InvalidTypeError(f"Invalid type '{type_}' in line: {line}")
                    
                    try:
                        size = int(size_str)
                    except ValueError:
                        size = size_str
                    
                    attributes.append(TCPyAttribute(identifier, type_, size))
                else:
                    raise InvalidFormatError(f"Invalid line format: {line}")

        return TCPyFile(self.filename, attributes)
