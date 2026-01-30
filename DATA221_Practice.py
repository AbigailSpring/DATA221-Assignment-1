from newsapi import NewsApiClient

news_api = NewsApiClient(api_key="189bbb2c5e02433ab320bd2ee324a53e")

articles = news_api.get_everything(q="artificial intelligence",language="en",page_size=3)
for article in articles["articles"]:
    print(article["title"])
    print(article["source"]["name"])

from sklearn.preprocessing import StandardScaler
data = [[10, 90], [12, 96], [9, 120], [13, 112], [8, 88]]
scaler = StandardScaler()
data = scaler.fit_transform(data)
print (data)


import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [5,0,7,3]

plt.plot(x, y, 'o-', label = 'line1', color = 'pink')
plt.legend()
plt.show()




import matplotlib.pyplot as plt

x = [1.5,1,3.5,2,2.7,2.2,3,3.2,1.5]
y = [5,3.5,1.5,4,3.6,2.2,2.2,1,2.5]

plt.scatter(x, y, label = 'samples',
color = 'purple')
plt.legend()
plt.show()



import matplotlib.pyplot as plt

x = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]

y = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]

heights = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
plt.contourf(x, y, heights)
plt.show()
