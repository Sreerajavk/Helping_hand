from django.contrib import admin

# Register your models here.


from .models import  *


@admin.register(donor_details)
class Admin_donor(admin.ModelAdmin):

    list_display = ['user' , 'email_status' , 'phone' , 'points' ,'points']



@admin.register(institution_details)
class Admin_institution(admin.ModelAdmin):

    list_display = ['user' , 'email_status' , 'phone'  ]


@admin.register(post)
class Admin_post(admin.ModelAdmin):

    list_display = ['user' , 'title' , 'body' , 'is_satisfied' ,'rating' ]


