class TCPyAttribute:
    def __init__(self, name: str, type_: str, size: int):
        self.name_ = name
        self.type_ = type_
        self.size_ = size

    def __eq__(self, other):
        return (
            isinstance(other, TCPyAttribute) and
            self.name_ == other.name_ and
            self.type_ == other.type_ and
            self.size_ == other.size_
        )

    def __repr__(self):
        return f"TCPyAttribute(name={self.name_}, type={self.type_}, size={self.size_})"
