# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:10:15 2019

@author: ASUA
"""

import numpy as np
eq_inputs=np.array([4,-2,3.5,5,-11,4.7])
pop_size=8
total_pop=(pop_size,len(eq_inputs))
new_pop=np.random.uniform(low=-4.0,high=4.0,size=total_pop)
print("New Population: ",new_pop)


def cal_fitness(eq_inputs,new_pop):
    fitness=np.sum(eq_inputs*new_pop,axis=1)
    return(fitness)
fitness=cal_fitness(eq_inputs,new_pop)
print("Fitness values: ",fitness)

num_parents=4
def selection(num_parents,fitness,new_pop):
    best_parents=[]
    for i in range(num_parents):
        best_index=np.argmax(fitness)
        best_parents.append(new_pop[best_index])
        fitness[best_index]=-999999
    return(best_parents)
best_parents=selection(num_parents,fitness,new_pop)
best_parents=np.array(best_parents)
print("Selected Parents: ",best_parents)

offspring_size=(4,len(eq_inputs))
def crossover(best_parents,offspring_size):
    cross_point=len(eq_inputs)//2
    offspring=np.empty(offspring_size)
    for i in range(offspring_size[0]):
        offspring[i,0:cross_point]=best_parents[i,0:cross_point]
        if(i+1==offspring_size[0]):
            offspring[i,cross_point:]=best_parents[0,cross_point:]
        else:
            offspring[i,cross_point:]=best_parents[i+1,cross_point:]
    return(offspring)
offspring=crossover(best_parents,offspring_size)
print("After Crossover: ",offspring)

num_mutations=2
def mutation(offspring,num_mutations):
    for i in range(num_mutations):
        pop_sel=np.random.randint(0,offspring.shape[0])
        gene_sel=np.random.randint(0,offspring.shape[1])
        value=np.random.uniform(low=-4.0,high=4.0,size=(1,1))
        offspring[pop_sel,gene_sel]=value
        print(pop_sel,gene_sel,value)
    return (offspring)
mut_offspring=mutation(offspring,num_mutations)
print("After Mutation: ",mut_offspring)

new_pop[0:best_parents.shape[0]]=best_parents[:]
new_pop[best_parents.shape[0]: ]=mut_offspring[:]
print("Population After Replacement: ",new_pop)
        
