from random import randint
import pygal

#create a die class
class Die():
	def __init__(self, num_sides= 6):
		self.num_sides = num_sides

	def roll(self):
		'''method to roll the die'''
		return randint(1, self.num_sides)

#-----------------X------------------X------------------
#create 2 dies
die1 = Die()
die2 = Die()

results = [] #empty list to store results
for roll_num in range(1000):
	result = die1.roll() + die2.roll()
	results.append(result)

# print('\r')

#Analysing die rolls by checking the frequncies
frequency = {} #create an empty dictionary
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1): 
	#(lower sum of outcomes = 2, (higher sum of outcomes = 6+6 =12)+1)
	frequency[value] = results.count(value)

print(frequency)
freq_list = list(frequency.values())
#visualizing the result using pygal
#create histogram instance
histogram = pygal.Bar()

histogram.title = 'Result of two dice rolling for 1000 times'
# histogram.x_labels = list(range(2, max_result + 1))
#using list comprehenstion to make the labels
histogram.x_labels = [str(x) for x in range(2, max_result + 1)]
histogram.x_title = 'Results'
histogram.y_title = 'frequency of results'

histogram.add('D6+D6',freq_list)
histogram.render_to_file('two_die_roll.svg')

