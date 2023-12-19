from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType


class FunctionModel:

    def __init__(self, id: str, parameters: [Variable], instructions: [Instruction], return_type: VariableType):
        self.id = id
        self.parameters = parameters
        self.instructions = instructions
        self.return_type = return_type

    def dot(self):
        pass
        
    def c3d(self,scope):
        pass