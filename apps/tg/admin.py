
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Users, Items, PaymentHistory, ChatBase, Profiles, ReferalBase
from .forms import BaseForm, ItemsForm, PaymentsForm, ProfilesForm, ReferalsForm, ChatForm

@admin.register(Users)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'time', 'external_id', 'username')
    form = BaseForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(Items)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'cells', 'active_time')
    form = ItemsForm

@admin.register(PaymentHistory)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'time', 'external_id', 'summ', 'comment')
    form = PaymentsForm

@admin.register(ChatBase)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'external_id', 'chat')
    form = ChatForm

@admin.register(Profiles)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'external_id', 'ref_count', 'sub_ref_count', 'cells_count', 'cells_occupied', 'team_volume', 'team_occupied', 'wallet', 'get_chats')
    form = ProfilesForm

@admin.register(ReferalBase)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'external_id', 'from_who', 'get_refs')
    form = ReferalsForm
