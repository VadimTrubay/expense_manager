from django.urls import path
from .views import (
    ExpenseListCreateView,
    ExpenseDetailView,
    expenses_by_date_range,
    category_summary,
)

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expenses/<int:user_id>/date-range/', expenses_by_date_range, name='expenses-by-date-range'),
    path('expenses/<int:user_id>/category-summary/', category_summary, name='category-summary'),
]
