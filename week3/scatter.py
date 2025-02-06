## YOUR SOLUTION HERE ##
plt.scatter(scatter_data.danceability, scatter_data.valence, color='teal', alpha=0.15)

plt.title('Mood and Danceability correlation in Spotify genres')
plt.xlabel('Danceability')
plt.ylabel('Valence / Mood (sadder to happier)')
plt.show()
