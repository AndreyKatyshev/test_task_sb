from django.shortcuts import render
import folium

def nn(request):
    nn = folium.Map(location=[56.2540, 43.9378], zoom_start=11)

    nn.add_child(folium.LatLngPopup())

    homes = folium.FeatureGroup(name='Где я жил', control=True)
    my_home_tomorrow = folium.Marker(
        location=[56.3035, 43.9998],
        popup='Скоро здесь будет мой дом! Уже в этом Сентябре!',
        icon=folium.Icon(icon='home', color='green')
    ).add_to(homes)
    my_home_now = folium.Marker(
        location=[56.1624, 43.9222],
        popup='Пока, я живу здесь(',
        icon=folium.Icon(icon='home', color='red')
    ).add_to(homes)
    my_home_yesterday_1 = folium.Marker(
        location=[56.2857, 44.0720],
        popup='Здесь я жил когда то...',
        icon=folium.Icon(icon='icon', color='blue')
    ).add_to(homes)
    my_home_yesterday_2 = folium.Marker(
        location=[56.3401, 43.9303],
        popup='Здесь я жил когда то...',
        icon=folium.Icon(icon='icon', color='blue')
    ).add_to(homes)
    my_home_yesterday_3 = folium.Marker(
        location=[56.2666, 43.8747],
        popup='Здесь я жил когда то...',
        icon=folium.Icon(icon='icon', color='blue')
    ).add_to(homes)

    parks_and_recreation = folium.FeatureGroup(name='Парки и зоны отдыха', control=True)
    hutor = folium.Circle(
        radius=800,
        location=[56.2826, 44.0162],
        popup='Щёлоковский Хутор',
        color='green',
        fill=True,
    ).add_to(parks_and_recreation)

    nn.add_child(homes)  
    nn.add_child(parks_and_recreation)
    folium.TileLayer('Stamen Toner').add_to(nn)
    folium.TileLayer('Stamen Terrain').add_to(nn)

    folium.LayerControl().add_to(nn)
    
    nn.save('templates/map_nn_auto.html')
    return render(request, 'map_nn_auto.html')
