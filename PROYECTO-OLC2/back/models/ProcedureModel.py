from .Instruction import Instruction
from .Variable import Variable


class ProcedureModel:

    def __init__(self, id: str, parameters: [Variable], instructions: [Instruction]):
        self.id = id
        self.parameters = parameters
        self.instructions = instructions
