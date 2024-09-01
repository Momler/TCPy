from tcpy_parser.tcpy_attribute import TCPyAttribute

class TCPyFile:
    def __init__(self, filepath: str, attributes: list[TCPyAttribute]):
        self.filepath = filepath
        self.attributes = attributes

    def print(self):
        print(f"File Path: {self.filepath}")
        print("Attributes:")
        for attribute in self.attributes:
            print(attribute)

    def __repr__(self):
        return f"TCPyFile(filepath={self.filepath}, attributes={self.attributes})"
