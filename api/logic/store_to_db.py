from django.db import transaction
from api.models import Client, Results, ClientInsight
from api.serializers import ResultsSerializer

@transaction.atomic
def store_to_db(client_data, results):
    for client in client_data:
        client_obj = Client.objects.create(**client)
        results_obj = Results.objects.create(client=client_obj, result=results[client['id']])
    return {'client_data': client_data, 'results': results}