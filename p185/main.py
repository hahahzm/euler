import sys
import random
import time

original = []
original.append("5616185650518293")
original.append("3847439647293047")
original.append("5855462940810587")
original.append("9742855507068353")
original.append("4296849643607543")
original.append("3174248439465858")
original.append("4513559094146117")
original.append("7890971548908067")
original.append("8157356344118483")
original.append("2615250744386899")
original.append("8690095851526254")
original.append("6375711915077050")
original.append("6913859173121360")
original.append("6442889055042768")
original.append("2321386104303845")
original.append("2326509471271448")
original.append("5251583379644322")
original.append("1748270476758276")
original.append("4895722652190306")
original.append("3041631117224635")
original.append("1841236454324589")
original.append("2659862637316867")

value = []
value.append(2)
value.append(1)
value.append(3)
value.append(3)
value.append(3)
value.append(1)
value.append(2)
value.append(3)
value.append(1)
value.append(2)
value.append(3)
value.append(1)
value.append(1)
value.append(2)
value.append(0)
value.append(2)
value.append(2)
value.append(3)
value.append(1)
value.append(3)
value.append(3)
value.append(2)

def evaluate(str0):
	global original
	global value
	result = 0
	for i in range(0, len(original)): 
		correct = 0
		for j in range(0, 16):
			if str0[j] == original[i][j]:
				correct += 1
		if correct == value[i]:
			result += 1
	return result

def born(str1, str2):
	child = ""
	for i in range(0,16):
		if random.random() > .6:
			child += str1[i]
		else:
			child += str2[i]
	return child

def mutate(str0):
	result = ""
	for i in range(0,16):
		if random.random < .01:
			result += str(random.randint(0,9))
		else:
			result += str0[i]
	return result

random.seed()

parents = original

maximum = 0
previous_best = 6
itera = 0
while (maximum < 22):
	last_maximum = maximum
	#reproducing
	children = []
	for father in parents:
		for mother in parents:
			if father != mother:
				child = born(mother,father)
				child = mutate(child)
				children.append(child)

	#filtering
	survivor = []
	rank = []
	maximum = 0
	for child in children:
		correctness = evaluate(child)
		if correctness > maximum:
			maximum = correctness
		if correctness > (previous_best - 1):
			survivor.append(child)
			rank.append(correctness)

	#family gathering
	for parent in parents:
		correctness = evaluate(parent)
		if correctness > maximum:
			maximum = correctness
		if correctness > (previous_best - 1):
			survivor.append(parent)
			rank.append(correctness)

	#
	previous_best = maximum

	#lower filter
	if len(survivor) < 32:
		previous_best = 2
		continue

	#shrink population
	while len(survivor) > 64:
		new_parents = []
		new_rank = []
		for i in range(0, len(survivor)):
			if rank[i] != min(rank):
				new_parents.append(survivor[i])
				new_rank.append(rank[i])
		rank = new_rank
		survivor = new_parents

	#change generation
	parents = survivor

	#print section
	print "new population size: ", len(parents)
	print "best child has: ", maximum
	if (len(parents) > 0):
		best_c = parents[rank.index(maximum)]
		print best_c
	print "==============================================="


	#add blood
	for ancestor in original:
		parents.append(ancestor)

	#time.sleep(1)


