import initializer,genotype
import random
from matplotlib import pyplot as plt
import myCongif

if __name__ == '__main__':
    fileName = "iris.data"

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
        accuracy.append( round(gapedPopulation[0].fitnessScore, 2))
        print("Generation " , generationCount+1 , " Accuracy = ", accuracy[generationCount])

        newPopulation = genotypeOb.breed(gapedPopulation)
        genotypeOb.populationList = newPopulation
        GenerationAccuracy = gapedPopulation[0].fitnessScore
        generationCount += 1

        if (generationCount > myCongif.Config.SAME_NUMBER_OF_ITERATIONS):
            if(accuracy[-(myCongif.Config.SAME_NUMBER_OF_ITERATIONS)] == accuracy[-1]):
                print("Same Accuracy for last ", myCongif.Config.SAME_NUMBER_OF_ITERATIONS, " iterations")
                break

    mostFitIndividual = genotypeOb.populationList[0]

    correctPrediction = 0
    mostFitIndividual.resetFitness()
    data = modelData.X_test
    lable = modelData.Y_test
    classwiseAccuracy = dict()

    for i in range(len(data)):
        answer = mostFitIndividual.predict(data[i], lable[i])
        if( answer == 1):
            if(tuple(lable[i]) in classwiseAccuracy ):
                classwiseAccuracy[tuple(lable[i])] = classwiseAccuracy[tuple(lable[i])] + 1
            else:
                classwiseAccuracy[tuple(lable[i])] = 1

        correctPrediction += answer

    fitness = 100 * (correctPrediction / len(data))

    print("Test Accuracy is : ", fitness)

    plt.plot(range(len(accuracy)), accuracy , linestyle='dashed', linewidth = 1, marker='o',markersize=1)
    plt.ylim(0, 100)
    plt.xlabel("Generations")
    plt.ylabel("Accuracy")
    plt.title('Accuracy Curve')

    plt.show()




