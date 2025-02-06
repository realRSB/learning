## YOUR SOLUTION HERE ##
plt.bar(avg_heights.family, avg_heights.trunk, width = 0.35, color='tan')
plt.bar(avg_heights.family, avg_heights.leaves, bottom=avg_heights.trunk, width = 0.45, color='forestgreen')
plt.title('Trunk, Crown, and Total Height')
plt.xlabel('Family')
plt.ylabel('Average Height (m)')
plt.show()
