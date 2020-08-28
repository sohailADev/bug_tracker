from django.contrib import admin
from bug_tracker_app.models import CustomUserModel,TicketModel
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    #got code from stackoverflow
        fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field to show on admin',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (                    
                    'bio',              

                ),
            },
        ),
    )
admin.site.register(CustomUserModel,CustomUserAdmin)
admin.site.register(TicketModel)
