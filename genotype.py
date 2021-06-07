import random
import myCongif,individual,variation

class Genotype:

    def __init__(self):
        self.populationList = list()

    def getInstructionSet(self, dataLen):
        configOb = myCongif.Config()

        #randomly selecting the length of instruction set
        endIndex = random.randint(2,configOb.INIT_MAX_INSTRUCTION_SET_LENGTH)
        instructionSet = list()
        for i in range(endIndex):
            selectBit = random.randint(0,1)
            targetValue = random.randint(0,configOb.TOTAL_OUTPUT_REGISTER - 1)
            operator = random.randint(0,configOb.TOTAL_OPERATIONS - 1)
            source = random.randint(0,max(dataLen, configOb.TOTAL_OUTPUT_REGISTER ) - 1 )

            instruction = [selectBit, targetValue, operator, source]

            instructionSet.append(instruction)

        return instructionSet

    def createGenotype(self, X):
        dataLen = len(X[0])
        for i in range(myCongif.Config.POPULATION_SIZE):
            individualInstructionSet = self.getInstructionSet(dataLen)
            individualOb = individual.Individual(individualInstructionSet)
            self.populationList.append(individualOb)

        print(str(len(self.populationList)) + " individuals created.")

    def calculateFitness(self, data, lable):
        for person in self.populationList:
            correctPrediction = 0
            person.resetFitness()
            for i in range(len(data)):
                answer = person.predict(data[i] , lable[i])
                correctPrediction += answer

            fitness = 100*(correctPrediction/len(data))
            person.fitnessScore = fitness

    def getGapedPopulation(self):
        sortedPopulation = sorted(self.populationList, key=lambda x: x.fitnessScore, reverse=True)

        totalGap = (myCongif.Config.GAP_PERCENTAGE * len(sortedPopulation)) / 100

        gapedPopulation = sortedPopulation[: int(len(sortedPopulation)- totalGap)]
        return gapedPopulation

    def isChildReadyToPush(self, child,newPopulation):
        crossoverChance = random.randint(0, 100) < myCongif.Config.CROSSOVER_PROBABILITY

        if (crossoverChance and (not (child is None)) and (len(newPopulation) < len(self.populationList))):
            return True
        else:
            return False

    def breed(self, gapedPopulation):
        newPopulation = gapedPopulation[:]

        while (len(newPopulation) < len(self.populationList)):

            parent1 = random.choice(gapedPopulation)
            parent2 = random.choice(gapedPopulation)

            child1,child2 = variation.TwoPointCrossover().crossover(parent1, parent2)

            mutationOb = variation.Mutation()

            if (self.isChildReadyToPush(child1,newPopulation)):

                mutatedChild = mutationOb.mutateIndividual(child1)
                newPopulation.append(mutatedChild)

            if (self.isChildReadyToPush(child2,newPopulation)):

                mutatedChild = mutationOb.mutateIndividual(child2)
                newPopulation.append(mutatedChild)

        return newPopulation