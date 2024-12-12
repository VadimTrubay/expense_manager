from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Sum
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.decorators import api_view


class ExpenseListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


@api_view(['GET'])
def expenses_by_date_range(request, user_id):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    if not (start_date and end_date):
        return Response({"error": "Please provide both start_date and end_date."}, status=status.HTTP_400_BAD_REQUEST)

    expenses = Expense.objects.filter(user_id=user_id, date__range=[start_date, end_date])
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_summary(request, user_id):
    month = request.query_params.get('month')

    if not month:
        return Response({"error": "Please provide a month in the format YYYY-MM."}, status=status.HTTP_400_BAD_REQUEST)

    expenses = (
        Expense.objects.filter(user_id=user_id, date__startswith=month)
        .values('category')
        .annotate(total=Sum('amount'))
    )
    return Response(expenses)
