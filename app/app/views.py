from django.http import JsonResponse


def index(request):
    response = {'status': 'api is running' }
    var = 1
    return JsonResponse(response)
