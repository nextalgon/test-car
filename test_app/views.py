from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json
from .models import Cars, Clients, Orders, ExOrders
from .serializers import CarsSerializer, ClientsSerializer, ExOrdersSerializer, OrdersSerializer, TimeFindSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from datetime import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

date_format = "%m/%d/%Y"


class CarsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = CarsSerializer
    queryset = Cars.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CarDetialApi(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Cars.objects.get(car_id=id)

        except Cars.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        car = Cars.objects.get(car_id=id)
        serializer = CarsSerializer(car)
        return Response(serializer.data)

    def put(self, request, id):
        car = Cars.objects.get(car_id=id)
        serializer = CarsSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        car = Cars.objects.get(car_id=id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CliensView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = ClientsSerializer
    queryset = Clients.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ClientDetailApi(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Clients.objects.get(cliend_id=id)

        except Clients.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        client = Clients.objects.get(cliend_id=id)
        serializer = ClientsSerializer(client)
        return Response(serializer.data)

    def put(self, request, id):
        client = Clients.objects.get(cliend_id=id)
        serializer = ClientsSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        client = Clients.objects.get(cleind_id=id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class OrderDetailApi(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Orders.objects.get(order_id=id)

        except Orders.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        order = Orders.objects.get(order_id=id)
        serializer = OrdersSerializer(order)
        return Response(serializer.data)

    def put(self, request, id):
        order = Orders.objects.get(order_id=id)
        serializer = OrdersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        order = Orders.objects.get(order_id=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExOrderView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = ExOrdersSerializer
    queryset = ExOrders.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ExOrderDetailApi(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return ExOrders.objects.get(ex_order_id=id)

        except ExOrders.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        ex_order = ExOrders.objects.get(ex_order_id=id)
        serializer = ExOrdersSerializer(ex_order)
        return Response(serializer.data)

    def put(self, request, id):
        ex_order = ExOrders.objects.get(ex_order_id=id)
        serializer = ExOrdersSerializer(ex_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        ex_order = ExOrders.objects.get(ex_order_id=id)
        ex_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
@api_view(["GET", "POST"])
def car_bounty(request):
    if request.method == "GET":
        return Response({''})
    elif request.method == "POST":
        #mashinani nechi marta repeat bolgani va keltirgan summasi
        money_list = []
        repeat = 0
        data = Cars.objects.get(car_id=request.data)
        ser = CarsSerializer(data)
        money = (ser.data.get('rent_cost'))
        new = Orders.objects.filter(car_id=request.data)
        aaa = OrdersSerializer(new, many=True)
        jso = json.dumps(aaa.data)
        timmee = json.loads(jso)
        for i in timmee:
            repeat += 1
            a = i.get('from_date')
            b = i.get('to_date')
            time1 = datetime.strptime(a, date_format)
            time2 = datetime.strptime(b, date_format)
            delta = time2 - time1
            mon = delta.days*money
            money_list.append(mon)
        if money_list:
            for i in money_list:
                i += i
            di = {'money': i,
                  'repeat': repeat}
            return Response(di)
        return Response(aaa.data)


@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
@api_view(["GET", "POST"])
def order_exorder(request):
    if request.method == "GET":
        return Response({''})
    elif request.method == "POST":
        j = 0
        data = ExOrders.objects.filter(order_id=request.data)
        ser = ExOrdersSerializer(data, many=True)
        jso = json.dumps(ser.data)
        exorders = json.loads(jso)
        for i in exorders:
            j += 1
        if j:
            di = {'repeat': j}
            return Response(di)
        return Response({''})


@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
@api_view(["GET", "POST"])
def client_bounty(request):

    if request.method == "GET":
        return Response({''})

    elif request.method == "POST":
        #clientning Order summasi va repeati
        pay1 = 0
        repeat1 = 0
        repeat2 = 0
        lis = []
        car_ids = []
        from_dates = []
        to_dates = []
        di = {}
        day = []
        cost1 = []
        data = Orders.objects.filter(client_id=request.data)
        ser = OrdersSerializer(data, many=True)
        jso = json.dumps(ser.data)
        timmee = json.loads(jso)

        for i in timmee:
            car_id = i.get('car_id')
            from_date = i.get('from_date')
            to_date = i.get('to_date')
            di.update({repeat1: [car_id] + [from_date] + [to_date]})
            repeat1 += 1

        for a, b in di.items():
            car_ids.append(b[0])
            from_dates.append(b[1])
            to_dates.append(b[2])

        for i in car_ids:
            car_cost = Cars.objects.filter(car_id=i)
            serial = CarsSerializer(car_cost, many=True)
            money = serial.data
            json_format_cost = json.dumps(money)
            formate = json.loads(json_format_cost)
            for u in formate:
                lis.append(u.get('rent_cost'))

        for x, y in zip(from_dates, to_dates):
            time1 = datetime.strptime(x, date_format)
            time2 = datetime.strptime(y, date_format)
            delta = time2 - time1
            day.append(delta.days)

        for summa, da in zip(lis, day):
            cost1.append(summa*da)

        for i in cost1:
            pay1 += i

        #clientning exOrderi summasi va repeati
        new_data = ExOrders.objects.filter(client_id=request.data)
        new_ser = ExOrdersSerializer(new_data, many=True)
        new_jso = json.dumps(new_ser.data)
        new_time = json.loads(new_jso)
        new_from_date = []
        new_to_date = []
        new_order_id = []
        new_day = []
        new_car_id = []
        new_car_cost = []
        cost2 = []
        pay2 = 0

        for i in new_time:
            repeat2 += 1
            new_from_date.append(i.get('from_date'))
            new_to_date.append(i.get('to_date'))
            new_order_id.append(i.get('order_id'))

        for x, y in zip(new_from_date, new_to_date):
            time1 = datetime.strptime(x, date_format)
            time2 = datetime.strptime(y, date_format)
            delta = time2 - time1
            new_day.append(delta.days)

        for i in new_order_id:
            order = Orders.objects.filter(order_id=i)
            serial = OrdersSerializer(order, many=True)
            money = serial.data
            json_format_cost = json.dumps(money)
            formate = json.loads(json_format_cost)
            for u in formate:
                new_car_id.append(u.get('car_id'))

        for i in new_car_id:
            car = Cars.objects.filter(car_id=i)
            seri = CarsSerializer(car, many=True)
            money = seri.data
            cost = json.dumps(money)
            forma = json.loads(cost)
            for u in forma:
                new_car_cost.append(u.get('rent_cost'))

        for x, y in zip(new_day, new_car_cost):
            cost2.append(x*y)

        for i in cost2:
            pay2 += i

        #ExOrder + Order
        general_cost = pay1 + pay2
        repeat = repeat1 + repeat2
        return Response({"Obwaya summa etogo clienta": general_cost,
                         "Obwiy raz repeat Ordera i ExOrdera": repeat})


@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def find_time(request):
    if request.method == "GET":
        time_find = Orders.objects.all()
        serializer = TimeFindSerializer(time_find, many=True)
        json1 = json.dumps(serializer.data)
        json2 = json.loads(json1)
        return Response(json2)

    elif request.method == 'POST':
        time_find = Orders.objects.all()
        serializer = TimeFindSerializer(time_find, many=True)
        json1 = json.dumps(serializer.data)
        json2 = json.loads(json1)
        print(request.data)
        return Response({''})