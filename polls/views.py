from django.shortcuts import render
import requests
import json

# Browser request for home page
def home(request):
    apig=None
    adate=None
    price=None
    apim = None
    if request.method == 'POST':
        ticker = request.POST['ticker'].upper()
        token = 'pk_e3e52d9ac09d4c269d065ece0f82fa3a'
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token="+token)
        api_request_graph_d = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/chart/6m?token="+token)
        api_request_graph_m = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/chart/1y?token="+token)
        try:
            api = json.loads(api_request.content)
            apig = json.loads(api_request_graph_d.content)
            apim = json.loads(api_request_graph_m.content)
            adate=[]
            price=[]
            m_date=[]
            m_price=[]
            for data in apig:
                adate.append(data['date'])
                price.append(data['uClose'])  

            for data1 in apim:
                m_date.append(data1['date'])
                m_price.append(data1['uClose'])
        except Exception as e:
            api = 'Error...'
        

    
        return render(request, 'home.html', {'api': api,'error':"Could not access the API or Wrong Ticker Name", 'adate':adate, 'price': price, 'm_date': m_date, 'm_price':m_price})        
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})           
