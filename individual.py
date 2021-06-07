import myCongif
import numpy as np

class Individual:
    # Operators = [+, -, /2, *2]
    # Operators = [0, 1,  2 , 3]
    # instructionSet = [ Select | target Register | operator| source ]

    def __init__(self, instructionSet):
        self.instructionSet = instructionSet
        self.registers = [0] * myCongif.Config.TOTAL_OUTPUT_REGISTER
        self.fitnessScore = 0

    def reset(self):
        self.registers = [0] * myCongif.Config.TOTAL_OUTPUT_REGISTER

    def resetFitness(self):
        self.fitnessScore = 0

    def isValid(self):
        if( (len(self.instructionSet) > myCongif.Config.MIN_INSTRUCTION_SET_LENGTH) and (len(self.instructionSet) < myCongif.Config.MAX_INSTRUCTION_SET_LENGTH)):
            return True
        else:
            return False

    def runProgram(self, data):
        self.reset()
        for instruction in self.instructionSet:
            select = instruction[0]
            target = instruction[1]
            operator = instruction[2]
            source = instruction[3]

            if select == 0:
                source = data[source]
            else:
                source = self.registers[source]

            if operator == 0:
                self.registers[target] = self.registers[target] + source
            if operator == 1:
                self.registers[target] = self.registers[target] - source
            if operator == 2:
                self.registers[target] = self.registers[target] / 2
            if operator == 3:
                self.registers[target] = self.registers[target] * 2

    def predict(self, data, lable):

        self.runProgram(data)

        maxLableIndex = np.array(lable).argmax()
        maxRegisterIndex = np.array(self.registers[:len(lable)]).argmax()

        if maxLableIndex == maxRegisterIndex:
            return 1
        else:
            return 0