from django.db import models
# from auth_app.models import ClientUser
# from ca/rt.models import Cart
# Create your models here.
import datetime

class ProductOrder(models.Model):
    # order_id = models.CharField(max_length=120)
    customer_id = models.CharField(max_length=120)
    cart_id = models.CharField(max_length=120)

    address = models.CharField(max_length=450, verbose_name='Укажите свой адрес')
    delivery_time = models.CharField(max_length=122, verbose_name= 'Желаемое время доставки')
    comment = models.CharField(max_length=400, verbose_name='Комментарий')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        hr_created_time = datetime.datetime.strptime(str(self.created_date)[:10], '%Y-%m-%d').strftime('%d-%m-%Y')
        return 'Заказ #{} от {}'.format(self.pk, hr_created_time)


    # def save(self,**kwargs):
    #     super(ProductOrder, self).save(**kwargs)
