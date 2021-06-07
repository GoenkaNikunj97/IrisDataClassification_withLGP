import random
import individual, myCongif

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

    mutationTypes = 2

    def swapMutation(self, child):
        bit1 = random.randint(0, len(child.instructionSet) - 1)
        bit2 = random.randint(0, len(child.instructionSet) - 1)
        #print("Swapping bit: ",bit1, "and ", bit2)
        child.instructionSet[bit1], child.instructionSet[bit2] = child.instructionSet[bit2], child.instructionSet[bit1]

        return child

    def reverseMutation(self, child):
        bit1 = random.randint(0, len(child.instructionSet) - 2)
        bit2 = random.randint(bit1+1, len(child.instructionSet) - 1)

        mutatedChild = child.instructionSet[0:bit1] + child.instructionSet[bit2: bit1-1: -1] + child.instructionSet[bit2+1:]

        mutatedChild = individual.Individual(mutatedChild)

        return mutatedChild

    def mutateIndividual(self, childToMutate):
        child = childToMutate
        type = random.randint(0, self.mutationTypes - 1)
        if (random.randint(0, 100) < myCongif.Config.MUTATION_PROBABILITY):
            if (type == 0):
                child = self.swapMutation(child)
            if (type == 2):
                child = self.reverseMutation(child)

        return child
