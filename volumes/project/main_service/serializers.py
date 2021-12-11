
from rest_framework import serializers
from .models import vgSales


class VgSalesSerialier(serializers.ModelSerializer):

    class Meta:
        model = vgSales
        fields = "__all__"