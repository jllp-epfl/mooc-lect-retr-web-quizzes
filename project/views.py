from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import requests
from urllib.parse import quote

def index(request):
    return render(request, 'index.html')

@require_POST
def submit_form(request):

    form_data = request.POST

    question = form_data.get('question')
    print(f'question: {question}')

    num_results = form_data.get('num_results')
    print(f'num_results: {num_results}')

    base_url = 'http://localhost:8000/api/lectures/'

    # Encoding the question parameter using urllib.parse.quote twice to achieve %2520 and %253F
    encoded_question = quote(quote(question))
    url = f"{base_url}question/{encoded_question}/num_results/{num_results}/"
    print(f'url: {url}')

    response = requests.get(url)
    print(f'response: {response}')

    data = response.json()
    print(f'data: {data}')

    video_url = data['video_url']
    start_time = data['start_time']
    end_time = data['end_time']
    print(f'start_time: {start_time}')
    print(f'end_time: {end_time}')

    # solution: https://stackoverflow.com/questions/73403685/how-can-i-get-a-parameter-of-an-url-with-django-rest-framework
    return JsonResponse({'received_data': request.POST, 'video_url': video_url, 'start_time': start_time, 'end_time': end_time})
