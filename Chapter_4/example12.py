# Example 4.12
# Swarm Plot using Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = [8,6]
sns.set_style("darkgrid")
titanic_data = sns.load_dataset('titanic')
sns.swarmplot(x='alone', y='age', hue='sex',data=titanic_data)