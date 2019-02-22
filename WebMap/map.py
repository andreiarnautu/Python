import folium
import pandas


map = folium.Map(location = [45.101362, 24.359020], zoom_start = 6)

#  Add stuff to the map, using the add_child() procedure

#  Create a feature group, where we add all the locations using markers
feature_group_volcanoes = folium.FeatureGroup(name = "Volcano Map")

feature_group_volcanoes.add_child(folium.Marker(location = [45.101362, 24.359020], popup = "Hi, I am a marker", tooltip = "Home", icon = folium.Icon(color = "green")))

#  Get the latitude and longitude lists from the .txt file, representing the coordinates of the volcanoes
data = pandas.read_csv("Volcanoes.txt")
latitude_list = data["LAT"]
longitude_list = data["LON"]
elevation_list = data["ELEV"]
name_list = data["NAME"]

def give_color(height) :
  if height < 1500 :
    return "green"
  elif height < 3000 :
    return "orange"
  else :
    return "red"

#  Add the volcanoes to the map using markers
for x, y, h, name in zip(latitude_list, longitude_list, elevation_list, name_list) :
  feature_group_volcanoes.add_child(folium.CircleMarker(location = [x, y], popup = str(h) + " m", tooltip = '"' + name + '" ' + "Volcano ", radius = 6, 
                          fill_color = give_color(h), color = "grey", fill_opacity = 0.8, fill = True))

feature_group_country_coloring = folium.FeatureGroup(name = "Country Coloring")

#  Add a color layer for each country based on its population
feature_group_country_coloring.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(),
                                       style_function = lambda x : {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000
                                                                             else "yellow" if x["properties"]["POP2005"] < 20000000
                                                                             else "orange" if x["properties"]["POP2005"] < 50000000
                                                                             else "red"}))

map.add_child(feature_group_volcanoes)
map.add_child(feature_group_country_coloring)
map.add_child(folium.LayerControl())
map.save("Map1.html")