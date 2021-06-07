import initializer,genotype
import random
from matplotlib import pyplot as plt
import myCongif

if __name__ == '__main__':
    fileName = "tic-tac-toe.data"

    #  iris.data ========= tic-tac-toe.data
    #init data
    modelData = initializer.Initialize(fileName)

    #init Population
    genotypeOb = genotype.Genotype()
    genotypeOb.createGenotype(modelData.X_train)
    accuracy = list()
    generationCount = 0
    GenerationAccuracy = 0
    desiredAccuracy = 95
    if (fileName == "tic-tac-toe.data"):
        desiredAccuracy = 75

    while (GenerationAccuracy< desiredAccuracy and generationCount < 250):
        #shuffle all individual to have randomness
        random.shuffle(genotypeOb.populationList)

        genotypeOb.calculateFitness(modelData.X_train, modelData.Y_train)

        gapedPopulation = genotypeOb.getGapedPopulation()
        accuracy.append(gapedPopulation[0].fitnessScore)
        print("Generation " , generationCount+1 , " Accuracy = ", accuracy[generationCount])

        newPopulation = genotypeOb.breed(gapedPopulation)
        genotypeOb.populationList = newPopulation
        GenerationAccuracy = gapedPopulation[0].fitnessScore
        generationCount += 1

        if (generationCount > myCongif.Config.SAME_NUMBER_OF_ITERATIONS):
            sublist = accuracy[-(myCongif.Config.SAME_NUMBER_OF_ITERATIONS):]

            if(sublist.count(sublist[0]) == len(sublist)):
                print("Same Accuracy for last ", myCongif.Config.SAME_NUMBER_OF_ITERATIONS, " iterations")
                break

    mostFitIndividual = genotypeOb.populationList[0]

    correctPrediction = 0
    mostFitIndividual.resetFitness()
    data = modelData.X_test
    lable = modelData.Y_test
    for i in range(len(data)):
        answer = mostFitIndividual.predict(data[i], lable[i])
        correctPrediction += answer

    fitness = 100 * (correctPrediction / len(data))

    print("Test Accuracy is : ", fitness)

    plt.plot(range(len(accuracy)), accuracy , linestyle='dashed', linewidth = 1, marker='o',markersize=1)
    plt.ylim(0, 100)
    plt.xlabel("Generations")
    plt.ylabel("Accuracy")
    plt.title('Accuracy Curve')

    plt.show()




