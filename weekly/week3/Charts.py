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

## YOUR SOLUTION HERE ##
plt.plot(line_data.month_name, line_data.alice_springs_avg_high, color='green', linestyle='dotted', label='Alice Springs')
plt.plot(line_data.month_name, line_data.windhoek_avg_high, color='green', linestyle='dashed', label='Windhoek')
plt.plot(line_data.month_name, line_data.quito_avg_high, color='steelblue', linewidth=2.5, label='Quito')
plt.plot(line_data.month_name, line_data.samarqand_avg_high, color='darkorange', linestyle='dotted', label='Samarqand')
plt.plot(line_data.month_name, line_data.london_avg_high, color='darkorange', linestyle='dashed', label='London')
plt.plot(line_data.month_name, line_data.kodiak_avg_high, color='darkorange', linestyle='solid', label='Kodiak')
plt.title('Average High Temps Around the World, 2020')
plt.ylabel('Temperature (F)')
plt.xlabel('Month')
plt.tick_params(axis='x', labelrotation=45)
plt.legend(bbox_to_anchor = (1, .75))
plt.show()

plt.savefig('line_chart.png')

## YOUR SOLUTION HERE ##
plt.pie(pie_data.number_sold, labels=pie_data.model, startangle=60, 
        colors=['darkorange', 'gold', 'tomato', 'yellowgreen','darkmagenta',
               'teal', 'indigo',  'powderblue', 'royalblue'])
plt.title('Top 10 EVs sold in the US by count, 2021')
plt.show()

## YOUR SOLUTION HERE ##
plt.scatter(scatter_data.danceability, scatter_data.valence, color='teal', alpha=0.15)

plt.title('Mood and Danceability correlation in Spotify genres')
plt.xlabel('Danceability')
plt.ylabel('Valence / Mood (sadder to happier)')
plt.show()
