class Config:
    MAX_INSTRUCTION_SET_LENGTH = 256
    INIT_MAX_INSTRUCTION_SET_LENGTH = 128
    MIN_INSTRUCTION_SET_LENGTH = 8
    TOTAL_OUTPUT_REGISTER = 4
    TOTAL_OPERATIONS = 4

    #PAR TO TUNE!
    GAP_PERCENTAGE = 20
    MUTATION_PROBABILITY = 90
    CROSSOVER_PROBABILITY = 90
    POPULATION_SIZE = 120
    SAME_NUMBER_OF_ITERATIONS = 50