# how the data looks like
year	solti_nominated	solti_won	beyonce_nominated	beyonce_won
0	1963	1	1	0	0
1	1964	1	0	0	0
2	1965	2	0	0	0
3	1966	1	0	0	0
4	1967	1	2	0	0


# first-draft chart
fig = plt.figure(figsize=(8,6), facecolor='aliceblue')
fig.suptitle('Comparing Georg Solti and Beyoncé', fontsize=20)
fig.subplots_adjust(hspace=0.5) 

plt.subplot(2, 1, 1)
plt.bar(grammys_data.year, grammys_data.solti_nominated, color='cornflowerblue', label='Solti Nominated')
plt.bar(grammys_data.year, grammys_data.solti_won, bottom=grammys_data.solti_nominated, color='orange', label='Solti Won')
plt.title('Georg Solti')
plt.ylim(0,11)
plt.xlim(1961, 2025)
plt.legend(frameon='False')
plt.axvline(x=1999.5, ymin=0, ymax=1, linewidth=2, dashes=(1,2), color='red')
plt.annotate('Solti: 31 wins, 74 nominations\nfrom 1963 to 1999', (2023.5, 3), ha='right')

plt.subplot(2, 1, 2)
plt.bar(grammys_data.year, grammys_data.beyonce_nominated, color='royalblue', label='Beyoncé Nominated')
plt.bar(grammys_data.year, grammys_data.beyonce_won, bottom=grammys_data.beyonce_nominated, color='pink', label='Beyoncé Won')
plt.title('Beyoncé')
plt.ylim(0,11)
plt.xlim(1961, 2025)
plt.xlabel(' ')
plt.legend(frameon='False')
plt.axvline(x=1999.5, ymin=0, ymax=1, linewidth=2, dashes=(1,2), color='green')
plt.annotate('Beyoncé: 32 wins, 88 nominations\nfrom 2000 to today', (1962.5, 3))

plt.show()
plt.savefig('beyoncevssolti.png')
