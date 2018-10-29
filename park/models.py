from django.db import models
# from company.models import Company

# Create your models here.
class Park(models.Model):
    park_name = models.CharField(max_length = 20)
    park_count = models.IntegerField()
    park_register = models.DateTimeField()
    park_company = models.ForeignKey('company.Company')

    class Meta:
        db_table = 'parks'