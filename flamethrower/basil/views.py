from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import *
from django.views.generic import View
import json

## tried making this like PlacesView with RESTfulView extended, but might not be ideal
## as this has foreign keys
def index(request):
    categories = Transaction_Category.objects.all()
    transactions = {}
    for c in categories:
        if len(Transaction.objects.filter(transaction_category=c)) > 0:
            transactions[c.name] = Transaction.objects.filter(transaction_category=c).order_by('date')

    data = {
        'transactions': transactions,
        'places': _get_json_for_class(PlacesView), #Payee.objects.all().order_by('name'),
    }
    return render(request, 'basil/_base.html', data)


def _get_json_for_class(cls):
    items = cls().retrieve()
    return json.dumps(items).encode('utf-8')


class RESTfulView(View):
    def get(self, request, *args, **kwargs):
        data = self.retrive()
        return HttpResponse(json.dumps(data), 
            content_type="application/json")

    # create
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        created = self.create(data)
        return HttpResponse(json.dumps(created),
            content_type="application/json")

    #update
    def put(self, request, id, *args, **kwargs):
        # TODO - somehow decode() fusses up... why!?
        #data = json.loads(request.body.decode("uft-8"))
        data = json.loads(request.body)
        self.update(id, data)
        return HttpResponse('{}',
            content_type="application/json")

    def delete(self, request, id, *args, **kwargs):
        self.destroy(id)
        return HttpResponse('{}', 
            content_type="application/json")


class PlacesView(RESTfulView):
    def create(self, data):
        place = Payee.objects.create(**data)
        place.save()
        return place.to_dict()

    def update(self, id, data):
        place = Payee.objects.get(pk=id)
        place.name = data['name']
        place.save()

    def destroy(self, id):
        place = Payee.objects.get(pk=id)
        place.delete()

    def retrieve(self):
        places = Payee.objects.all().order_by('name')
        return [p.to_dict() for p in places]

