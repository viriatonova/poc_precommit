from django.http import JsonResponse


def index(request):
    response = {'status': 'api is running' }
    return JsonResponse(response)
