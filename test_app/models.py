from django.db import models


class Clients(models.Model):
    cliend_id = models.IntegerField(primary_key=True, verbose_name='client id')
    passport_series = models.CharField(verbose_name='passport seriya', max_length=20)
    first_name = models.CharField(verbose_name='name', max_length=30)
    last_name = models.CharField(verbose_name='surname', max_length=30)
    phone = models.CharField(verbose_name='contact', max_length=15)

    def __str__(self):
        return str(self.first_name)


class Cars(models.Model):
    car_id = models.IntegerField(primary_key=True, verbose_name='car_id')
    brand = models.CharField(verbose_name='brend', max_length=30)
    model = models.CharField(verbose_name='model', max_length=30)
    rent_cost = models.FloatField(verbose_name='cost')

    def __str__(self):
        return str(self.model)


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True, verbose_name='order id')
    client_id = models.ForeignKey(Clients, verbose_name='client id', on_delete=models.PROTECT)
    car_id = models.ForeignKey(Cars, verbose_name='car id', on_delete=models.PROTECT)
    timestamp = models.DateField(auto_now_add=True)
    from_date = models.DateField(verbose_name='from date')
    to_date = models.DateField(verbose_name='to date')

    def __str__(self):
        return str(self.order_id)


class ExOrders(models.Model):
    order_id = models.ForeignKey(Orders, verbose_name='ex order id', on_delete=models.CASCADE)
    client_id = models.ForeignKey(Clients, verbose_name='ex client id', on_delete=models.CASCADE)
    from_date = models.DateField(verbose_name='ex from date')
    to_date = models.DateField(verbose_name='ex to date')

    def __str__(self):
        return str(self.order_id)
