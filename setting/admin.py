from setting.views import log_view
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Notification, SystemMailSetting, Log, TelegramSetting


class SystemMailSettingResource(resources.ModelResource):
    class Meta:
        model = SystemMailSetting
        skip_unchanged = True
        report_skipped = True


@admin.register(SystemMailSetting)
class SystemMailSettingAdmin(ImportExportModelAdmin):
    resource_class = SystemMailSettingResource

    list_display = [
        'mail_server', 'mail_port', 'mail_username', 'mail_sender',
        'mail_password'
    ]

    list_editable = ('mail_server', 'mail_port', 'mail_username',
                     'mail_sender', 'mail_password')

    list_display_links = None
    actions_on_top = True


class NotificatioResource(resources.ModelResource):
    class Meta:
        model = Notification
        import_id_fields = ('name', )
        exclude = ('id', )
        skip_unchanged = True
        report_skipped = True


@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
    resource_class = NotificatioResource

    list_display = ['name', 'type', 'content']
    list_editable = ('name', 'type', 'content')

    list_display_links = None
    actions_on_top = True


@admin.register(Log)
class FeedbackStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return log_view(request)


class TelegramSettingResource(resources.ModelResource):
    class Meta:
        model = TelegramSetting
        skip_unchanged = True
        report_skipped = True


@admin.register(TelegramSetting)
class TelegramSettingAdmin(admin.ModelAdmin):
    resource_class = TelegramSettingResource

    list_display = ['token']
    list_editable = ('token', )

    list_display_links = None
