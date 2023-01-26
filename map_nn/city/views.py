from django.shortcuts import render
import folium

def style_geo_json(feature):
    return {
        'fillColor': 'yellow',
        'color': 'green',
    }

def nn(request):
    nn = folium.Map(
        # width=1800,
        # height=800,
        location=[56.2540, 43.9378], 
        zoom_start=11,
    )

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
        color='green',
        fill=True,
        tooltip='Щёлоковский Хутор',
    ).add_to(parks_and_recreation)
    folium.PolyLine(
        locations=[
            [56.2572, 43.9710],[56.2583, 43.9663],[56.2635,43.9700],[56.2848,43.9697],
            [56.2843, 43.9805], [56.2735, 43.9759],[56.2572, 43.9710]
        ],
        color='green',
        fill=True,
        tooltip='Парк Швейцария'
    ).add_to(parks_and_recreation)
    sormovski_park = folium.GeoJson(data={ 
    "type": "Polygon",
    "coordinates": [
       [ [43.8665, 56.3380], [43.8653, 56.3334], [43.8617, 56.3320], [43.8458, 56.3387],
       [43.8522, 56.3449], [43.8655, 56.3419], [43.8665, 56.3380] ]    
    ]},
    tooltip = 'Сормовский Парк',
    style_function=style_geo_json,
    ).add_to(parks_and_recreation)

    nn.add_child(homes)  
    nn.add_child(parks_and_recreation)

    folium.TileLayer('Stamen Toner').add_to(nn)
    folium.TileLayer('Stamen Terrain').add_to(nn)

    folium.LayerControl().add_to(nn)

    # nn.save('templates/map_nn_auto.html')
    # return render(request, 'map_nn_auto.html')

    map = nn._repr_html_()
    context = {
        'map': map
    }
    return render(request, 'map_2.html', context)
