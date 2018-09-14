from django.db import models
from django.utils import timezone

# Наследуем класс от Model чтобы django понял что он должен сохранить его в бд
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)#Ссылка на другую модель
    title = models.CharField(max_length=200) #Текстовое поле с ограниченным числом символов
    text = models.TextField() #Текстовое поле с неограниченным числом символов
    created_date = models.DateTimeField(default=timezone.now())
    # blank=True означает что поле может быть пустым, по умолчанию всегда False
    # null = True означает что пустое поле будет записано в бд как null, по умолчание все поля в бд not null
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
