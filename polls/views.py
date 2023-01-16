from django.shortcuts import render
import requests
import json

# Browser request for home page
def home(request):
    if request.method == 'POST':
        ticker = request.POST['ticker'].upper()
        token = 'pk_e3e52d9ac09d4c269d065ece0f82fa3a'
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token="+token)
        api_request_graph = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/chart/6m?token="+token)
        try:
            api = json.loads(api_request.content)
            apig = json.loads(api_request_graph.content)
        except Exception as e:
            api = 'Error...'
        
        adate=[]
        price=[]
        for data in apig:
            adate.append(data['date'])
            price.append(data['uClose'])  
    
        return render(request, 'home.html', {'api': api,'error':"Could not access the api", 'adate':adate, 'price': price})        
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})           
