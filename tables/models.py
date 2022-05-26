from django.db import models


# Create your models here.

class Citizen(models.Model):
    citizen_id = models.BigAutoField(primary_key=True)
    citizen_name = models.TextField()

    def __str__(self):
        return str(self.citizen_id)


class IncomeStatement(models.Model):
    income_statement_id = models.BigAutoField(primary_key=True)
    citizen_id = models.ForeignKey('Citizen', on_delete=models.CASCADE)
    income = models.IntegerField()
    expense = models.IntegerField()
    is_citizen_suspect = models.BooleanField(default=False)
