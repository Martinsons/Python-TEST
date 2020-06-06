import folium
import pandas

data = pandas.read_csv("cities.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
pop = list(data["Population"])
city = list(data["City"])
html = """

Pilsēta:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Iedzīvotāju skaits: %s
"""

map = folium.Map(location=[57.006020, 24.236384], zoom_start=7)

fgc = folium.FeatureGroup(name="Pilsētas")

for lt, ln, pop, city in zip(lat, lon, pop, city):
    iframe = folium.IFrame(html=html % (
        city, city, pop), width=200, height=100)
    fgc.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(
        iframe), icon=folium.Icon(color='green')))


map.add_child(fgc)
map.add_child(folium.LayerControl())

map.save("Map1.html")
