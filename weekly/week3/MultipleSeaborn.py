## YOUR SOLUTION HERE ##
sns.pairplot(data=plants)
plt.show()

## YOUR SOLUTION HERE ##
sns.histplot(data=plants, x='Plant_height', hue='PH')
plt.show()

## YOUR SOLUTION HERE ##
sns.displot(kind='hist', data=plants, x='Plant_height', hue='PH', col='PH')
plt.show()

## YOUR SOLUTION HERE ##
sns.displot(kind='kde', data=plants, x='Plant_height', hue='PH', col='PH', fill=True)
plt.show()
