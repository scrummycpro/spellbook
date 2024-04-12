from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text data
text_data = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Pellentesque cursus odio nec nunc aliquet, ac faucibus magna dapibus. 
Sed in lectus non nisi commodo ultrices. 
Vivamus auctor semper est, et vestibulum urna consectetur nec. 
Proin scelerisque feugiat ultrices. 
Sed euismod est sed felis ullamcorper, et fringilla felis accumsan. 
"""

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

# Save the generated word cloud as a PNG file
wordcloud.to_file('wordcloud.png')

# Display the generated word cloud using matplotlib (optional)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()

