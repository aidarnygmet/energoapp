from django import forms
from .models import kotel_status
class kotel_statusForm:
    class Meta:
        model = kotel_status
        fields = ['kotel_id', 'kotel_status', 'begin', 'end']
