# How data is structured
genus	counts	color_label
0	Psychotria	74	yellowgreen
1	Protium	63	firebrick
2	Otoba	54	mediumpurple
3	Pouteria	41	deepskyblue
4	Triplaris	35	forestgreen
5	Brosimum	22	lightgray
6	Couepia	22	lightgray
7	Inga	22	orangered
8	Cordia	20	darkturquoise
9	Nectandra	16	lightgray

## YOUR SOLUTION HERE ##
fig = plt.figure(figsize=(18,16), facecolor='lightgray', tight_layout=True) 
fig.subplots_adjust(hspace=.6)
fig.suptitle('Species Counts in Primary, Secondary, and Selectively Logged Tapajos Forests', fontsize=18, y=1)

plt.subplot(3,1,1)
plt.bar(PF_data.genus, PF_data.counts, color=PF_data.color_label)
plt.xlabel('Primary Forest')
plt.ylim((0,105))
plt.xlim((-3,105))
plt.xticks(rotation=-90, fontsize=12)
plt.subplot(3,1,2)
plt.bar(SF_data.genus, SF_data.counts, color=SF_data.color_label)
plt.xlabel('Secondary Forest')
plt.ylim((0,105))
plt.xlim((-3,105))
plt.xticks(rotation=-90, fontsize=12)
plt.subplot(3,1,3)
plt.bar(SLF_data.genus, SLF_data.counts, color=SLF_data.color_label)
plt.xlabel('Selectively Logged Forest')
plt.ylim((0,105))
plt.xlim((-3,105))
plt.xticks(rotation=-90, fontsize=12)
plt.show()
