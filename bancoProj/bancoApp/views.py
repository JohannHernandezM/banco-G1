import email
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseServerError

from .models import Customer, Account

def home(request):
    return HttpResponse("Bienvenida a su Banco")

def newCustomer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer = Customer(
                id = data["id"],
                firstName = data["firstName"],
                lastName = data["lastName"],
                email = data["email"],
                password = data["password"]
            )
            customer.save()
            return HttpResponse("Cliente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAllCustomers(request):
    if request.method == 'GET':
        try:
            customers = Customer.objects.all()
            if (not customers):
                return HttpResponseBadRequest("No existen usuarios cargados")
            allCustData = []
            for cust in customers:
                data = {"id": cust.id, "firstName": cust.firstName, "lastName": cust.lastName, "email": cust.email}
                allCustData.append(data)
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(allCustData)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getOneCustomer(request, id):
    if request.method == 'GET':
        try:
            cust = Customer.objects.filter(id = id).first()
            if (not cust):
                return HttpResponseBadRequest("No existe un usuario con ese documento")
            #print(customer)
            data = {"id": cust.id, "firstName": cust.firstName, "lastName": cust.lastName, "email": cust.email}
            resp = HttpResponse()
            resp.headers['Content-Type'] = 'text/json'
            resp.content = json.dumps(data)
            return resp
        except:
            return HttpResponseServerError("Error de servidor")
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
        
def updateCustomer(request, id):
    if request.method == 'PUT':
        try:
            cust = Customer.objects.filter(id = id).first()
            if (not cust):
                return HttpResponseBadRequest("No existe un usuario con ese documento")
            data = json.loads(request.body)
            cust.firstName = data["firstName"]
            cust.lastName = data["lastName"]
            cust.email = data["email"]
            cust.password = data["password"]
            cust.save()
            return HttpResponse("Cliente actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deleteCustomer(request, id):
    if request.method == 'DELETE':
        try:
            cust = Customer.objects.filter(id = id).first()
            if (not cust):
                return HttpResponseBadRequest("No existe un usuario con ese documento")
            
            cust.delete()
            return HttpResponse("Cliente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos recibidos")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")
