import numpy as np

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]

hot = porridge[porridge > 80]

just_right = porridge[(porridge >= 60) & (porridge <= 80)]

print(cold)
print(hot)
print(just_right)

import numpy as np

temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

temperatures_fixed = temperatures + 3
monday_temperatures = temperatures_fixed[0,:]
thursday_friday_morning = temperatures_fixed[3:5,1]

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]

print(temperatures_fixed)

import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])

recipes = np.genfromtxt('recipes.csv', delimiter=',')

eggs = recipes[:,2]
one_egg_recipes = eggs == 1

cookies = recipes[0,:]

double_batch = cupcakes * 2

grocery_list = cookies + double_batch
