from django.db import models

class vgSales(models.Model):
    # Rank = models.IntegerField(null=False, default=0)
    Name = models.CharField(max_length=200)
    Platform = models.CharField(max_length=200)
    Year = models.IntegerField(null=True)
    Genre = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=200)
    NA_Sales = models.FloatField()
    EU_Sales = models.FloatField()
    JP_Sales = models.FloatField()
    Other_Sales = models.FloatField()
    Global_Sales = models.FloatField()