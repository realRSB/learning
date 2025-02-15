Certainly! Here's a cleaner and more organized version of your code:

```python
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# Survey responses
survey_responses = [
    'Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 
    'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 
    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 
    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 
    'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 
    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 
    'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 
    'Kerrigan', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 
    'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 
    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 
    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos'
]

# Convert to NumPy array
survey = np.array(survey_responses)

# Calculate total votes for Ceballos
total_ceballos = (survey == 'Ceballos').sum()
print("Total votes for Ceballos:", total_ceballos)

# Calculate percentage of votes for Ceballos
percentage_ceballos = 100 * total_ceballos / len(survey)
print("Percentage of votes for Ceballos:", percentage_ceballos)

# Generate possible survey outcomes
possible_surveys = np.random.binomial(len(survey), 0.54, 10000) / len(survey)

# Plot histogram
plt.hist(possible_surveys, range=(0, 1), bins=20, color='lightblue')
plt.title("Distribution of Survey Outcomes")
plt.xlabel("Proportion of Votes for Ceballos")
plt.ylabel("Frequency")
plt.show
