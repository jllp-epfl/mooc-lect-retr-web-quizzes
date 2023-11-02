
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import requests

def index(request):
    return render(request, 'index.html')

@require_POST
def submit_form(request):
    # Handle form submission here
    # For example, you can retrieve the form data and process it
    # In this example, I'll just return the received data
    form_data = request.POST
    # return JsonResponse({'received_data': form_data})

    question = form_data.get('inputField')
    print(f'question: {question}')

    headers = {
        'accept': '*/*',
    }
    # url = f'http://127.0.0.1:8000/lectures/?question=<{question}>'
    # url = f'http://127.0.0.1:8000/<lectures>/<{question}>'
    url = f'http://127.0.0.1:8000/<{question}>'

    response = requests.get(url, headers=headers)
    print(f'response: {response}')
    data = response.json()
    print(f'data: {data}')

    # video_url = "https://tube.switch.ch/download/video/de94a7a1"
    video_url = data['video_url']
    start_time = data['start_time']
    end_time = data['end_time']
    print(f'start_time: {start_time}')
    print(f'end_time: {end_time}')


    # solution: https://stackoverflow.com/questions/73403685/how-can-i-get-a-parameter-of-an-url-with-django-rest-framework
    # /maps/?idfield=<id>,
    return JsonResponse({'received_data': request.POST, 'video_url': video_url, 'start_time': start_time, 'end_time': end_time})
