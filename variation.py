import random
import individual


class TwoPointCrossover:

    def getTwoCrossoverPoints(self, parent):
        crossoverPoint1 = 0
        crossoverPoint2 = 0

        while (crossoverPoint1 == crossoverPoint2):
            crossoverPoint1 = random.randint(0, len(parent.instructionSet) - 2)
            crossoverPoint2 = random.randint(crossoverPoint1 + 1, len(parent.instructionSet) - 1)

        return crossoverPoint1,crossoverPoint2

    def createChild(self, parent1, parent2, p1CP1,p1CP2, p2CP1,p2CP2 ):

        childInstructionSet = parent1.instructionSet[:p1CP1 - 1]
        childInstructionSet = childInstructionSet + parent2.instructionSet[p2CP1: p2CP2]
        childInstructionSet = childInstructionSet + parent1.instructionSet[p1CP2 + 1:]

        child = individual.Individual(childInstructionSet)

        return child

    def crossover(self, parent1, parent2):

        p1CP1, p1CP2 = self.getTwoCrossoverPoints(parent1)
        p2CP1, p2CP2 = self.getTwoCrossoverPoints(parent2)

        child1 = self.createChild(parent1, parent2, p1CP1, p1CP2, p2CP1, p2CP2)

        child2 = self.createChild(parent2, parent1, p2CP1, p2CP2, p1CP1, p1CP2)

        if (not (child1.isValid())):
            child1 = None
        if (not (child2.isValid())):
            child2 = None

        return child1, child2

class Mutation:

    def swapMutation(self, child):
        pass
