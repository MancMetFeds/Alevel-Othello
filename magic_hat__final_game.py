from random import shuffle
def decide(finalchoices):
	best_choice=[]
	largest_gain=0
	try:
		for i in finalchoices:
			#print("i: "+str(i))
			#print("largest gain "+str(largest_gain))
			if int(i[0]) > largest_gain:
				#print(i[0])
				del best_choice[:]
				best_choice.append(i)
				largest_gain=i[0]
			elif i[0]==largest_gain:
				best_choice.append(i)
			elif i[0]<largest_gain:
				None
		if len(best_choice)>1:
			#print("shuffling")
			shuffle(best_choice)
			#print(best_choice)
			return best_choice[0]
		else:
			#print("most points"+str(best_choice[0]))
			return(best_choice[0])
	except IndexError:
		return "pass"

"""
def magic_hat(in_hat):
	#print(in_hat)
	the_hat=[]
	item_in_hat=[]
	priority_to_calc=[]
	for i in in_hat:
		for collection in i:
			unit = []
			try:
				for content in collection:
					if str(content).isdigit() == True:
						unit.append(content)
						succession = int(collection.index(content)) + 1
						unit.append(collection[succession])
					elif content.isdigit() == False:
						unit.append(i[int(len(i))-1])
						priority_to_calc.append(unit)
						unit = []
			except TypeError:
				pass
	cells_to_choose=[]
	cell_choice=[]
	biggest_gain=0
	for cells in priority_to_calc:
		if int(cells[0])*int(cells[2])==biggest_gain:
			cell_choice.append(cells[0])
			cell_choice.append(cells[1])
			cells_to_choose.append(cell_choice)
			cell_choice=[]
		elif int(cells[0])*int(cells[2])>biggest_gain:
			for proposed_cells in cells_to_choose:
				del proposed_cells
			biggest_gain = int(cells[0])*int(cells[2])
			cell_choice.append(cells[0])
			cell_choice.append(cells[1])
			cells_to_choose.append(cell_choice)
			cell_choice=[]
		else:
			pass
	print(cells_to_choose)
	choice=randint(0, (len(cells_to_choose)-1))
	made_choice=cells_to_choose[choice]
	print(made_choice)
	return(made_choice)
"""
"""
def magic_hat(in_hat):
	the_hat=[]
	item_in_hat=[]
	priority_to_calc=[]
	for i in in_hat:
		for collection in i:
			unit = []
			try:
				for content in collection:
					if content.isdigit() == True:
						unit.append(content)
						succession = int(collection.index(content)) + 1
						unit.append(collection[succession])
					elif content.isdigit() == False:
						unit.append(i[int(len(i))-1])
						priority_to_calc.append(unit)
						unit = []
			except TypeError:
				pass
	cells_to_choose=[]
	cell_choice=[]
	biggest_gain=0
	for cells in priority_to_calc:
		if int(cells[0])*int(cells[2])==biggest_gain:
			cell_choice.append(cells[0])
			cell_choice.append(cells[1])
			cells_to_choose.append(cell_choice)
			cell_choice=[]
		elif int(cells[0])*int(cells[2])>biggest_gain:
			for proposed_cells in cells_to_choose:
				del proposed_cells
			biggest_gain = int(cells[0])*int(cells[2])
			cell_choice.append(cells[0])
			cell_choice.append(cells[1])
			cells_to_choose.append(cell_choice)
			cell_choice=[]
		else:
			pass
	print(cells_to_choose)
	choice=randint(0, (len(cells_to_choose)-1))
	made_choice=cells_to_choose[choice]
	print(made_choice)
	return(made_choice)
"""