import initializer,genotype
import random
from matplotlib import pyplot as plt

if __name__ == '__main__':

    #init data
    modelData = initializer.Initialize("iris.data")

    #init Population
    genotypeOb = genotype.Genotype()
    genotypeOb.createGenotype(modelData.X_train)
    accuracy = list()
    generationCount = 0
    GenerationAccuracy = 0

    while (GenerationAccuracy< 95 and generationCount < 250):

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




