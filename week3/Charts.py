## YOUR SOLUTION HERE ##
plt.bar(x = bar_data.PH, height = bar_data.average_leaf_width, width = 0.8, align = 'center')
plt.title('Effect of pH on Leaf Width')
plt.xlabel('pH')
plt.ylabel('Leaf Width (cm)')

plt.errorbar(x = bar_data.PH, y = bar_data.average_leaf_width, yerr = bar_data.error, fmt = 'o', color = 'orangered')

plt.show()

## YOUR SOLUTION HERE ##
plt.hist(hist_data.carapace_length, bins=15, range=(75,155), color='gold')
plt.title('Lobsters tagged by size')
plt.ylabel('Number tagged')
plt.xlabel('Carapace length (mm)')
plt.show()
