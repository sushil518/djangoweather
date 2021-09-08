from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get("http://api.airvisual.com/v2/city?city=Pune&state=Maharashtra&country=India&key=a00e5775-2ce6-44a9-a6ed-841255c322d9")

    try:
        api = json.loads(api_request.content)
    
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
