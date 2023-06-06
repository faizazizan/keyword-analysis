#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas


df = pd.read_csv("Keyword_Stats.csv")

# Filter the DataFrame to include only rows where "Top of page bid (low range)" has a value
filtered_df = df[df['Top of page bid (low range)'].notnull()]

# Get the keywords from the filtered DataFrame
keywords_with_bid = filtered_df['Keyword'].tolist()

# Print the keywords that have a value in the "Top of page bid (low range)" column
for keyword in keywords_with_bid:
    print(keyword)


# In[ ]:


# Filter the DataFrame to include only rows where "Top of page bid (low range)" has a value
filtered_df = df[df['Top of page bid (low range)'].notnull()]

# Get the keywords from the filtered DataFrame
keywords_with_bid = filtered_df['Keyword'].tolist()

# Print the keywords that have a value in the "Top of page bid (low range)" column
for keyword in keywords_with_bid:
    print(keyword)


# In[ ]:


# Filter the DataFrame to include only rows where "Top of page bid (low range)" has a value
filtered_df = df[df['Top of page bid (low range)'].notnull()]

# Get the keywords from the filtered DataFrame
keywords_with_bid = filtered_df['Keyword'].tolist()

# Print the keywords that have a value in the "Top of page bid (low range)" column
for keyword in keywords_with_bid:
    print(keyword)


# In[ ]:


# Filter the DataFrame to include only rows where "Top of page bid (low range)" has a value
filtered_df = df[df['Top of page bid (low range)'].notnull()]

# Get the keywords from the filtered DataFrame
keywords_with_bid = filtered_df['Keyword'].tolist()

# Print the keywords that have a value in the "Top of page bid (low range)" column
for keyword in keywords_with_bid:
    print(keyword)


# In[ ]:


# Group the keywords based on their competition level
grouped_df = df.groupby('Competition')

# Get the keywords for each competition level
low_competition_keywords = grouped_df.get_group('Low')['Keyword'].tolist()
medium_competition_keywords = grouped_df.get_group('Medium')['Keyword'].tolist()
high_competition_keywords = grouped_df.get_group('High')['Keyword'].tolist()

# Print the keywords for each competition level
print("Keywords with low competition:")
for keyword in low_competition_keywords:
    print(keyword)



# In[ ]:


print("\nKeywords with medium competition:")
for keyword in medium_competition_keywords:
    print(keyword)



# In[ ]:


print("\nKeywords with high competition:")
for keyword in high_competition_keywords:
    print(keyword)


# In[ ]:


# Sort the DataFrame by 'Top of page bid (high range)' column in descending order
sorted_df = df.sort_values(by='Top of page bid (high range)', ascending=False)

# Get the top 30 keywords with the highest bid price
top_30_keywords = sorted_df.head(30)['Keyword'].tolist()

# Print the top 30 keywords
for keyword in top_30_keywords:
    print(keyword)


# In[ ]:


# Filter the DataFrame based on keywords containing specific terms
filtered_df = df[df['Keyword'].str.contains('malaysia|service|near', case=False, na=False)]

# Sort the filtered DataFrame by the 'Keyword' column
sorted_df = filtered_df.sort_values(by='Keyword')

# Print the sorted keywords
sorted_keywords = sorted_df['Keyword'].tolist()
for keyword in sorted_keywords:
    print(keyword)


# In[ ]:


# Get the number of keywords in the DataFrame
num_keywords = len(df)

# Print the number of keywords
print("Number of keywords:", num_keywords)


# In[ ]:


# Filter the DataFrame based on keywords containing specific terms
filtered_df = df[df['Keyword'].str.contains('malaysia|service|near', case=False, na=False)]

# Get the number of keywords in the DataFrame
num_keywords = len(df)

# Calculate the output divided by the number of keywords
output_percentage = len(filtered_df) / num_keywords * 100

# Print the output percentage
print("Output percentage:", output_percentage)


# In[ ]:


# Filter the DataFrame based on keywords containing specific terms
filtered_df = df[df['Keyword'].str.contains('malaysia|service|near', case=False, na=False)]

# Get the number of keywords in the DataFrame
num_keywords = len(df)

# Calculate the output divided by the number of keywords
output_percentage = len(filtered_df) / num_keywords * 100

# Calculate the percentage of non-matching keywords
non_matching_percentage = 100 - output_percentage

# Create labels for the pie chart
labels = ['Output Percentage', 'Non-Matching Percentage']

# Create data for the pie chart
data = [output_percentage, non_matching_percentage]

# Create a pie chart
plt.pie(data, labels=labels, autopct='%1.1f%%')

# Set aspect ratio to be equal so that pie is drawn as a circle
plt.axis('equal')

# Give the pie chart a title
plt.title('Keyword Filtering Results')

# Display the pie chart
plt.show()


# In[ ]:




