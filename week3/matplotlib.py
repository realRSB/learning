## YOUR SOLUTION HERE ##
plt.plot(line_data.month_name, line_data.alice_springs_avg_high, linestyle='dotted')
plt.plot(line_data.month_name, line_data.windhoek_avg_high, linestyle='dashed')
plt.plot(line_data.month_name, line_data.quito_avg_high, linewidth='2.5')
plt.plot(line_data.month_name, line_data.kodiak_avg_high)
plt.plot(line_data.month_name, line_data.samarqand_avg_high, linestyle='dotted')
plt.plot(line_data.month_name, line_data.london_avg_high, linestyle='dashed')
plt.show()
