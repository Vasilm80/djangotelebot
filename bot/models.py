from django.db import models



class User(models.Model):
    User_id = models.PositiveIntegerField(verbose_name='Идетификатор пользователя')
    name = models.CharField(max_length=300, verbose_name='Имя пользователя')

    class Meta():
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

class Message(models.Model):
    Message_id = models.IntegerField(verbose_name='Идентификатор сообщения')
    Message_text = models.TextField(verbose_name='Текст сообщения')
    Chat_id = models.IntegerField(verbose_name='Идентификатор чата')
    Message_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')
    User_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Идетификатор пользователя')

    class Meta():
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'




