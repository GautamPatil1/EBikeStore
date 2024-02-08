from django.http import HttpResponse
from django.shortcuts import render
import json
from .forms import BikeDetailForm


def index(request):
    bike_data =     mongo_uri = "your_mongodb_atlas_connection_string"
    client = MongoClient(mongo_uri).get_database()
    bike_data = client.get_database('bike_data')
    for scooter in bike_data:
        scooter["Price"] = scooter["Price"].replace("Rs", "").replace("RS", "")
        
    if request.method == 'POST':
        form = BikeDetailForm(request.POST)
        if form.is_valid():
            # Get data from the form
            company = form.cleaned_data['company']
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            range = form.cleaned_data['range']
            speed = form.cleaned_data['speed']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            power = form.cleaned_data['power']
            colors = form.cleaned_data['colors']
            image = form.cleaned_data['image']
            warranty = form.cleaned_data['warranty']
            time = form.cleaned_data['time']
            max_power = form.cleaned_data['max_power']
            touches = form.cleaned_data['touches']
            # Add more fields as needed

            # Render a new HTML page with the data
            return render(request, 'bike_detail.html', {
                'company': company,
                'name': name,
                'price': price,
                'range': range,
                'speed': speed,
                'weight': weight,
                'height': height,
                'power': power,
                'colors': colors,
                'image': image,
                'warranty': warranty,
                'time': time,
                'max_power' : max_power,
                'touches' : touches
                
                # Add more data from the JSON or other sources
            })
    else:
        form = BikeDetailForm()
    return render(request, 'base.html', {'data': bike_data, 'form': form})