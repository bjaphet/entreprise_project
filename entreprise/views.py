# entreprise/views.py
from django.shortcuts import render

def custom_permission_denied(request, exception=None):
    return render(request, "403.html", status=403)
