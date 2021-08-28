from django.shortcuts import render
from django.http import HttpResponse
import folium


# Create your views here.
def index(request):
    return render(request,'index.html')

def map(request):
    # create map
    map = folium.Map(location=[27.72590237450737,85.31215846538544,],zoom_start=7)
    folium.Marker(location=[27.72590237450737,85.31215846538544], tooltip='click for more', popup="utsab's house" ).add_to(map)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(map)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(map)
    folium.LayerControl().add_to(map)
    # get html representation of map
    m = map._repr_html_() 
    return render(request,'map.html',{'m':m})
