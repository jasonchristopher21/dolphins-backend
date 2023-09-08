from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=155)
    limit_bal = models.IntegerField()
    sex = models.PositiveSmallIntegerField()
    education = models.PositiveSmallIntegerField()
    marriage = models.PositiveSmallIntegerField()
    age = models.PositiveIntegerField()

    pay_0 = models.IntegerField()
    pay_2 = models.IntegerField()
    pay_3 = models.IntegerField()
    pay_4 = models.IntegerField()
    pay_5 = models.IntegerField()
    pay_6 = models.IntegerField()

    bill_amt1 = models.IntegerField()
    bill_amt2 = models.IntegerField()
    bill_amt3 = models.IntegerField()
    bill_amt4 = models.IntegerField()
    bill_amt5 = models.IntegerField()
    bill_amt6 = models.IntegerField()

    pay_amt1 = models.IntegerField()
    pay_amt2 = models.IntegerField()
    pay_amt3 = models.IntegerField()
    pay_amt4 = models.IntegerField()
    pay_amt5 = models.IntegerField()
    pay_amt6 = models.IntegerField()

    default_payment_next_month = models.BooleanField()

class Results(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    result = models.DecimalField(max_digits=6, decimal_places=4)

class ClientInsight(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    insights = models.JSONField()