from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType


class FunctionModel:

    def __init__(self, id: str, parameters: [Variable], block: Instruction, return_type: VariableType):
        self.id = id
        self.parameters = parameters
        self.block = block
        self.return_type = return_type

    def __str__(self):
        return self.id
