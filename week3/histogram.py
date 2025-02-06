## YOUR SOLUTION HERE ##
plt.hist(hist_data.carapace_length, bins=15, range=(75,155), color='gold')
plt.title('Lobsters tagged by size')
plt.ylabel('Number tagged')
plt.xlabel('Carapace length (mm)')
plt.show()
