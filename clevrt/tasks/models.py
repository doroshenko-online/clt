from django.db import models
from django.contrib.auth.models import User
from clt.models import Client

# Create your models here.

class Task_Category(models.Model):
    name = models.TextField(max_length=100, verbose_name='категория задания')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Task(models.Model):
    OPEN = 'open'
    CLOSED = 'closed'
    IN_WORK = 'in_work'

    STATUS = [
        (OPEN, 'Открыто'),
        (CLOSED, 'Закрыто'),
        (IN_WORK, 'В работе'),
    ]

    name = models.CharField(max_length=100, verbose_name='название задачи')
    client = models.ForeignKey(Client, default='cleverty', on_delete=models.DO_NOTHING, verbose_name='клиент')
    category = models.OneToOneField(Task_Category, on_delete=models.DO_NOTHING, verbose_name='категория')
    username_create = models.ForeignKey(User, related_name='username_create', max_length=20, on_delete=models.DO_NOTHING, verbose_name='создал задачу')
    who_permit = models.ManyToManyField(User, verbose_name='добавленные пользователи')
    accountable = models.ForeignKey(User, related_name='accountable', on_delete=models.DO_NOTHING, verbose_name='отвественный')
    status = models.TextField(max_length=15, choices=STATUS, verbose_name='статус задачи')
    description = models.TextField(max_length=5000, blank=True, verbose_name='описание задачи')
    image = models.ImageField(blank=True, null=True, verbose_name='изображение')
    pud_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name

class Task_Comment(models.Model):
    task = models.OneToOneField(Task, on_delete=models.DO_NOTHING, verbose_name='Задача')
    username_create = models.ForeignKey(User, max_length=20, on_delete=models.DO_NOTHING, verbose_name='Автор')
    comment = models.TextField(max_length=5000, verbose_name='Комментарий')
    image = models.ImageField(verbose_name='Изображение')
    pud_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Комментарий к задаче'
        verbose_name_plural = 'Комментарии к задаче'

    def __str__(self):
        return str(self.username_create) + " " + str(self.pud_date) + "({0})".format(str(self.task))