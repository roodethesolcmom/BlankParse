from django import forms

from .models import Users, Items, PaymentHistory, ChatBase, Profiles, ReferalBase

class BaseForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('external_id', 'username')
        widgets = {
            'username': forms.TextInput
        }

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('name', 'price', 'description', 'cells', 'active_time')
        widgets = {
            'name': forms.TextInput,
            'price': forms.NumberInput,
            'description': forms.Textarea,
            'cells': forms.NumberInput,
            'active_time': forms.SelectDateWidget
        }

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = PaymentHistory
        fields = ('external_id', 'summ', 'comment')
        widgets = {
            'summ': forms.NumberInput,
            'comment': forms.Textarea,
        }

class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('external_id', 'ref_count', 'sub_ref_count', 'cells_count', 'cells_occupied', 'team_volume', 'team_occupied', 'wallet', 'chats')
        widgets = {
            'ref_count': forms.NumberInput,
            'sub_ref_count': forms.NumberInput,
            'cells_count': forms.NumberInput,
            'cells_occupied': forms.NumberInput,
            'team_volume': forms.NumberInput,
            'team_occupied': forms.NumberInput,
            'wallet': forms.NumberInput,
            'get_chats': forms.Textarea
        }

class ReferalsForm(forms.ModelForm):
    class Meta:
        model = ReferalBase
        fields = ('external_id', 'from_who', 'referals')
        widgets = {
            'from_who': forms.NumberInput,
            'referals': forms.Textarea
        }

class ChatForm(forms.ModelForm):
    class Meta:
        model = ChatBase
        fields = ('external_id', 'chat')
        widgets = {
            'chat': forms.TextInput
        }
