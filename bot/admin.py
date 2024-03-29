from django.contrib import admin

from bot.models import User, Message, Answers


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','User_id', 'name')

admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('Message_id', 'Message_text', 'User_id', 'Chat_id', 'Message_date')

admin.site.register(Message, MessageAdmin)

class AnsewrsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Answer_text', 'Message_id')

admin.site.register(Answers, AnsewrsAdmin)