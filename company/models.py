from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length = 20)
    company_count = models.IntegerField()
    company_address = models.CharField(max_length = 30)

    class Meta:
        db_table = 'company'
    company_register = models.DateTimeField()

    # def __str__(self):
    #     print('company_name---->'+self.company_name+'company_address-------->'+self.company_address+'company_count-------'+str(self.company_count))

