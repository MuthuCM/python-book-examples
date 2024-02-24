# Example 6.3
# Finding the no. of times an item occurs in a List
movies = ["Sound of Music","Sound of Music","Mckennas Gold","Sound of Music", "Great Escape","Great Escape"]
count_items = dict()
for movie_name in movies:
  count_items[movie_name]=count_items.get(movie_name,0)+1
print(f"No. of times each movie name occurs in the List is:{count_items}")