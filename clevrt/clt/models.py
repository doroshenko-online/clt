from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=100, verbose_name='страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country

class City(models.Model):
    city = models.CharField(max_length=100, verbose_name='город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city

class Client(models.Model):
    ON = 'On'
    OFF = 'Off'
    POT = 'Pot'
    CLIENT_STATUS = [
        (ON, 'Активный'),
        (OFF, 'Отключенный'),
        (POT, 'Потенциальный'),
    ]
    name = models.CharField(max_length=100, verbose_name='название службы')
    country = models.ForeignKey(Country, max_length=100, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='страна')
    city = models.ForeignKey(City, max_length=100, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='город')
    hostname = models.CharField(max_length=100, blank=True, default='', verbose_name='хостнейм сервера')
    title_comment = models.CharField(max_length=50, blank=True, default='', verbose_name='комментарий клиента(виден в списке клиентов)')
    officeIp1 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP1')
    officeIp2 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP2')
    officeIp3 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP3')
    officeIp4 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP4')
    client_status = models.CharField(max_length=3, choices=CLIENT_STATUS, default=POT, verbose_name='статус клиента')
    hide = models.BooleanField(default=False, verbose_name='Скрыт')
    additional_info = models.TextField(max_length=500, default='', blank=True, verbose_name='дополнительная информация')
    connection_date = models.DateField(null=True, blank=True, verbose_name='дата подключения')
    last_activity = models.DateTimeField(auto_now=True, verbose_name='последнее посещение')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name

class Ip_List(models.Model):
    ip = models.CharField(max_length=16, verbose_name='ip')
    port = models.CharField(max_length=6, default='22', verbose_name='port')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')

    class Meta:
        verbose_name = 'IP-адрес'
        verbose_name_plural = 'IP-адреса'

    def __str__(self):
        return self.client.name

class Client_Number(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    name = models.CharField(max_length=50, verbose_name='имя')
    number = models.CharField(max_length=15, verbose_name='номер телефона')
    comment = models.TextField(max_length=100, blank=True, verbose_name='комментарий')
    add_date = models.DateField(auto_now_add=True, verbose_name='дата добавления номера')

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.client.name

class Client_Gateway(models.Model):
    TYPES = [
        ('GoIp', 'GoIp'),
        ('Openvox', 'Openvox'),
        ('Dinstar', 'Dinstar'),
        ('Yeastar', 'Yeastar'),
        ('Grandstream', 'Grandstream'),
        ('D-link', 'D-link'),
        ('Cisco', 'Cisco'),
        ('SPRUT', 'SPRUT'),
        ('Unknown', 'Unknown'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    ip = models.CharField(max_length=16, verbose_name='ip')
    port = models.CharField(max_length=6, blank=True, null=True, verbose_name='port')
    login = models.CharField(max_length=100, verbose_name='логин')
    secret = models.CharField(max_length=100, verbose_name='пароль')
    type_gateway = models.CharField(max_length=50, choices=TYPES, default='Unknown', verbose_name='вендор оборудования')

    class Meta:
        verbose_name = 'Шлюз'
        verbose_name_plural = 'Шлюзы'

    def __str__(self):
        return self.type

class Log(models.Model):
    username = models.ForeignKey(User, max_length=20, on_delete=models.DO_NOTHING, verbose_name='пользователь')
    pub_date = models.DateField(verbose_name='дата публикации')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

    def __str__(self):
        log = str(self.username) + " " + str(self.pub_date)
        return log

class Log_String(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, verbose_name='лог')
    username = models.ForeignKey(User, max_length=20, on_delete=models.DO_NOTHING, verbose_name='пользователь')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, verbose_name='клиент')
    info = models.TextField(max_length=1000, verbose_name='информация')

    class Meta:
        verbose_name = 'Лог строка'
        verbose_name_plural = 'Лог строки'

    def __str__(self):
        return self.client

class User_Setting(models.Model):
    KITTY = 'kitty'
    PUTTY = 'putty'
    PROGRAMM = [
        (KITTY, 'kitty'),
        (PUTTY, 'putty'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    programm = models.CharField(max_length=6, choices=PROGRAMM, blank=True, default=KITTY, verbose_name='программа для ssh')
    path = models.CharField(max_length=200, blank=True, null=True, verbose_name='путь к kitty или putty')

    class Meta:
        verbose_name = 'Настройка пользователя'
        verbose_name_plural = 'Настройки пользователя'

    def __str__(self):
        return self.user