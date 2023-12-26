from .Instruction import Instruction
from .Variable import Variable


class ProcedureModel:

    def __init__(self, id: str, parameters: [Variable], block: Instruction):
        self.id = id
        self.parameters = parameters
        self.block = block
