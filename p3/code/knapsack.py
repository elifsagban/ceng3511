import random
# import matplotlib.pyplot as plt for graphic part


# reading files


fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')


# global access to some variables
global parents
global next_generation
global k
global n
global mutProb


c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

popSize = int(input('Size of population : '))
genNumber = int(input('Max number of generation : '))


#creating population


def get_population(pop_size):
    population = []

    for chromosome in range(pop_size):
        temp = []
        for bit in range(len(w)):
            temp.append(random.randint(0, 1))
        population.append(temp)
    return population


created_population = get_population(popSize) # store population


def calculate_items(population):   # calculate weight, value and fitness value for each

    items_tuple = []
    fitness_value = 0
    for idx, chromo in enumerate(population):
        value_total = 0
        weight_total = 0

        for j, gene in enumerate(chromo):
            value_total += gene * v[j]
            weight_total += gene * w[j]

            if weight_total > c:
                fitness_value = 0
            else:
                fitness_value = value_total

        items_tuple.append((idx + 1, chromo, value_total, weight_total, fitness_value))
    return items_tuple


# print the population values

fitness_list = []
for item in calculate_items(created_population):
    print(item[0:4])
    val = item[4]
    fitness_list.append(val)


# this is for roulette wheel

def get_probability_list():
    total_fit = (sum(fitness_list))
    relative_fitness = [f/total_fit for f in fitness_list]
    probabilities = [sum(relative_fitness[:i+1])
                     for i in range(len(relative_fitness))]
    return probabilities


def roulette_wheel_pop(population, probabilities, number):
    chosen = []
    for q in range(number):
        r = random.random()
        for (i, individual) in enumerate(population):
            if r <= probabilities[i]:
                chosen.append(list(individual))
                break
    return chosen


 #print(roulette_wheel_pop(created_population, get_probability_list(), popSize))

def k_tournament_wheel_pop(population, k_, number):
    chosen = []
    temp_list = []

    for n in range(number):
        for k_ in range(0, k_):
            temp_list.append(list(random.choice(population)))

        tmp = calculate_items(temp_list)
        tmp_sorted = sorted(tmp, key=lambda  x: int(x[4]), reverse=True)

        chosen.append(tmp_sorted[0][1])
        tmp.clear()
        tmp_sorted.clear()

    return chosen


print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))

if parentSelection == 1:
    parents = roulette_wheel_pop(created_population, get_probability_list(), popSize)

if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(len(w)) + ') '))
    parents = k_tournament_wheel_pop(created_population, k, popSize)


def crossover(parent, num, size):
    children = []
    c_father = 0
    c_mother = 0
    crossover_pointer_list = random.sample(range(0, len(w)), k=num)

    for pop in range(size):
        for item_point in crossover_pointer_list:
            father = random.choice(parent)
            mother = random.choice(parent)
            for pointer in range(item_point):
                father[pointer], mother[pointer] = mother[pointer], father[pointer]

                c_father = father
                c_mother = mother

        children.append(c_father)
        children.append(c_mother)

    return children


print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))

childrens = crossover(parents, n, popSize)

print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))


def mutation(children_arr, given_p):

    for j in range(len(children_arr)):
        rnd = random.randint(0, 1)
        if rnd == given_p:
            lucky = children_arr[j]
            lucky_random = random.randint(0, len(w))
            lucky[lucky_random] = 1 - lucky[lucky_random]  # if it's 1, 1-1 = 0 or 1-0 = 1 CHANGING BITS


mutation(childrens, mutProb)


def age_based_selection(gen):
    keep_gen = elitism_cal(gen)
    next_gen = []

    for current_gen in gen:
        next_gen.append(current_gen)

    next_gen[0] = keep_gen

    return next_gen


def fitness_based_selection(gen):
    gen_tuple = calculate_items(gen)
    gen_sorted = sorted(gen_tuple, key=lambda  x: int(x[4]), reverse=True)
    next_gen = []

    for current_gen in range(popSize):
        next_gen.append(gen_sorted[current_gen][1])

    return next_gen


def elitism_cal(children_els):
    elitism_tuple = calculate_items(children_els)
    elitism_sorted = sorted(elitism_tuple, key=lambda  x: int(x[4]), reverse=True)
    best_individual = elitism_sorted[0][1]

    return best_individual


print('\nSurvival Selection\n---------------------------')
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))

if survivalSelection == 1:
    next_generation = age_based_selection(childrens)


if survivalSelection == 2:
    next_generation = fitness_based_selection(childrens)

elitism = bool(input('Elitism? (Y or N) '))


def genLoop(g, gnumber, p_selection, surv_selection):
    fitness_plot_list = []
    best_gen = ""
    weight = 0
    value = 0

    for loop in range(gnumber):
        if p_selection == 1:
            next_parents = roulette_wheel_pop(g, get_probability_list(), popSize)
            next_childrens = crossover(next_parents, n, popSize)
            mutation(next_childrens, mutProb)
            if surv_selection == "1":
                g = age_based_selection(next_childrens)

            else:
               g = fitness_based_selection(next_childrens)

        else:
            next_parents = k_tournament_wheel_pop(g, k, popSize)
            next_childrens = crossover(next_parents, n, popSize)
            mutation(next_childrens, mutProb)
            if surv_selection == "1":
                g = age_based_selection(next_childrens)

            else:
                g = fitness_based_selection(next_childrens)

        fitness_next_gen = calculate_items(g)
        fitness_next_gen_sorted = sorted(fitness_next_gen, key=lambda  x: int(x[4]), reverse=True)

        fitness_plot_list.append(fitness_next_gen_sorted[0][4])

    for a in g[0]:
        best_gen = best_gen + str(a)

    for j, gene in enumerate(g[0]):
        value += gene * v[j]
        weight += gene * w[j]

    fout.write("chromosome " + best_gen + "\n")
    fout.write("value " + str(value) + "\n")
    fout.write("weight  " + str(weight) + "\n")

    #plt.plot(fitness_plot_list)
    #plt.ylabel("fitness values")
    #plt.show()


genLoop(next_generation, genNumber, parentSelection, survivalSelection)





