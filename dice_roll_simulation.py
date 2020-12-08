'''program to simulate the dice roll and visualize it through pygal'''
from random import randint
import pygal
#create a die class
class Die():
	def __init__(self, num_sides= 6):
		self.num_sides = num_sides

	def roll(self):
		'''method to roll the die'''
		return randint(1, self.num_sides)


#-------------------X---------------------------------X------------
#create an instance of die and simulate its rolling
die1 = Die()

result = [] #empty list to store results
for roll_num in range(100):
	roll = die.roll()
	result.append(roll)

# print(result)
# print('\r')

#Analyse the result by noting the frequency of certain results
frequency = {} #create an empty dictionary

for value in range(1,die.num_sides + 1):
	frequency[value] = result.count(value)

print(frequency)

#visualizing the results us ing pygal
#create an instance of histogram
histogram = pygal.Bar()

freq_list = list(frequency.values())
histogram.title = 'Results of rolling one die for 1000 times'
histogram.x_labels = list(range(1,die.num_sides + 1))

histogram.x_title = 'Results'
histogram.y_title = 'Frequency of results'

histogram.add('D6', freq_list)
histogram.render_to_file('die_roll_visual.svg')

