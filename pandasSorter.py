import pandas as pd

# read outMath1.csv

titles = ["People", "History", "Geography", "Arts", "Philosophy", "Everyday_life", "Social_sciences", "Biological_and_health_sciences", "Physical_sciences", "Technology", "Mathematics"]
#titles = ["People", "History", "Geography", "Arts", "Philosophy", "Everyday_life", "Social_sciences", "Biological_and_health_sciences", "Physical_sciences", "Technology", "Mathematics"]

types = {'words': str, 'g1': float, 'g2': float, 'g3': float, 'g4': float, 'g5': float, 'g6': float, 'g7': float, 'g8': float, 'g9': float, 'g10': float, 'g11': float, 'gmath1': float, 'gmath2': float, 'gmath3': float, 'gmath4': float, 'gmath5': float, 'gmath6': float, 'gmath7': float, 'gmath8': float, 'gmath9': float, 'gmath10': float, 'gmath11': float}
df = pd.read_csv('outConfirmInv.csv', dtype=types)

bestPercentages = []

for i in range(1, 12):
    # sort the dataframe by gmathi
    df = df.sort_values(by=f'gmath{i}', ascending=False)
    
    # print the top 10 words
    print(f"Top 25 words for {titles[i - 1]}, {i}")
    print(df['words'][:25] + " " + df[f'gmath{i}'][:25].astype(str))

    # append the top percentage to bestPercentages
    bestPercentages.append(df[f'gmath{i}'][:1].values[0])

print(bestPercentages)

anti = 1
for i in bestPercentages:
     anti *= (1 - i)
    
print(anti)

# save to csv
#df.to_csv('outSortAdj1.csv', index=False)

# born, military, mi, style, god, typically, social, species, energy, design, x 
# people, history, geography, arts, philosophy, everyday_life, social_sciences, biological_and_health_sciences, physical_sciences, technology, mathematics
# titles = ["People", "History, "Geography", "Arts", "Philosophy", "Everyday_life", "Social_sciences", "Biological_and_health_sciences", "Physical_sciences", "Technology", "Mathematics"]