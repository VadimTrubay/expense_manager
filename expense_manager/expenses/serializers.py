from rest_framework import serializers
from .models import Expense
from django.contrib.auth.models import User


class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Expense
        fields = ['id', 'user', 'title', 'amount', 'date', 'category']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive.")
        return value
