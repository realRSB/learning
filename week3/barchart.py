## YOUR SOLUTION HERE ##
plt.bar(x = bar_data.PH, height = bar_data.average_leaf_width, width = 0.8, align = 'center')
plt.title('Effect of pH on Leaf Width')
plt.xlabel('pH')
plt.ylabel('Leaf Width (cm)')

plt.errorbar(x = bar_data.PH, y = bar_data.average_leaf_width, yerr = bar_data.error, fmt = 'o', color = 'orangered')

plt.show()
