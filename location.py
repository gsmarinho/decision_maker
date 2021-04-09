import requests
r = requests.get('https://api.ipdata.co?api-key=ac38ee14ba0d81375f9c13a487df6a8f8f4a9ceb424c9490c28fdaeb').json()
print(r['city'])
