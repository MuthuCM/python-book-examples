# Example 4.7 
# Bar Plot using Seaborn
# Import Libraries
#%matplotlib inline
import seaborn as sns
# Specify Data
movies = ["Annie Hall","Ben-Hur","Casablanca","Gandhi","WestSide Story"]
num_oscars = [5,11,3,8,10]
palette_color = sns.color_palette('bright')
# Draw a Bar Chart
sns.barplot(x = movies, y = num_oscars, color = 'g')
#plt.bar(range(0,len(movies)),num_oscars, color = colors, align = 'center')
plt.title("My Favourite Movies")
plt.xlabel("Movie Name")
plt.ylabel("No. of Oscar Awards")
#plt.xticks(range(0,len(movies)), movies)
plt.show()