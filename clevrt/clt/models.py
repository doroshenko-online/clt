from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=100, verbose_name='страна', unique=True, error_messages={'unique': 'Такая страна уже существует'})

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.country

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город', unique=True, error_messages={'unique': 'Такой город уже существует'})

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
    name = models.CharField(max_length=100, unique=True, verbose_name='название службы', error_messages={'unique': 'Такой клиент уже существует'})
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name='страна')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, verbose_name='город')
    hostname = models.CharField(max_length=100, blank=True, default='', verbose_name='хостнейм сервера')
    gateway_info = models.CharField(max_length=250, default='', blank=True, verbose_name='информация о роутере')
    local_ip = models.CharField(max_length=40, blank=True, default='', verbose_name='локальный ip сервера')
    title_comment = models.CharField(max_length=50, blank=True, default='', verbose_name='комментарий клиента(виден в списке клиентов)')
    officeIp1 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP1')
    officeIp2 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP2')
    officeIp3 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP3')
    officeIp4 = models.CharField(max_length=16, blank=True, verbose_name='офисный IP4')
    client_status = models.CharField(max_length=3, choices=CLIENT_STATUS, default=POT, verbose_name='статус клиента')
    os_version = models.CharField(max_length=10, blank=True, default='', verbose_name='версия ос')
    ast_version = models.CharField(max_length=10, blank=True, default='', verbose_name='версия астериска')
    login_ccs = models.CharField(max_length=20, blank=True, default='', verbose_name='логин')
    secret_ccs = models.CharField(max_length=100, blank=True, default='', verbose_name='пароль')
    ccs_version = models.CharField(max_length=15, blank=True, default='', verbose_name='версия ccs')
    cphone_maxvers = models.CharField(max_length=20, blank=True, default='',
                                         verbose_name='максимальная версия C-Phone')
    vps_own = models.BooleanField(default=False, verbose_name='наша впс')
    hide = models.BooleanField(default=False, verbose_name='скрыт')
    additional_info = models.TextField(max_length=500, default='', blank=True, verbose_name='дополнительная информация')
    date_on = models.DateField(null=True, blank=True, verbose_name='дата подключения')
    date_off = models.DateField(null=True, blank=True, verbose_name='дата отключения')
    last_activity = models.DateTimeField(auto_now=True, verbose_name='последнее посещение')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def get_absolute_url(self):
        return reverse('clt:client', kwargs={'name': self.name})

    def __str__(self):
        return self.name

class Ip_List(models.Model):
    ip = models.CharField(max_length=16, null=True, blank=True, verbose_name='ip')
    port = models.CharField(max_length=6, null=True, blank=True, default='22', verbose_name='port')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')

    class Meta:
        verbose_name = 'IP-адрес'
        verbose_name_plural = 'IP-адреса'

    def __str__(self):
        return self.client.name

class Client_Number(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    name = models.CharField(max_length=50, verbose_name='имя')
    number = models.CharField(max_length=15, unique=True, verbose_name='номер телефона')
    comment = models.CharField(max_length=100, blank=True, verbose_name='комментарий')
    hide = models.BooleanField(default=False, verbose_name='скрыт')
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
        ('Gudwin', 'Gudwin'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    ip = models.CharField(max_length=16, null=True, blank=True, verbose_name='ip')
    port = models.CharField(max_length=6, null=True, blank=True, default='80', verbose_name='port')
    login = models.CharField(max_length=100, null=True, blank=True, verbose_name='логин')
    secret = models.CharField(max_length=100, null=True, blank=True, verbose_name='пароль')
    type_gateway = models.CharField(max_length=50, null=True, blank=True, choices=TYPES, default='', verbose_name='вендор оборудования')

    class Meta:
        verbose_name = 'Шлюз'
        verbose_name_plural = 'Шлюзы'

    def __str__(self):
        return self.type_gateway

class Columns(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="клиент")
    column_name = models.CharField(max_length=50, blank=True, default='', verbose_name='название колонны')
    column_key = models.CharField(max_length=50, blank=True, default='', verbose_name='ключ колонны')
    port_send = models.SmallIntegerField(blank=True, default='', verbose_name='порт отправки')
    port_listen = models.SmallIntegerField(blank=True, default='', verbose_name='порт приема')


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


class Office_Gateway(models.Model):
    type_gateway = models.CharField(max_length=50, choices=Client_Gateway.TYPES, default='Unknown', verbose_name='вендор оборудования')
    local_ip = models.CharField(max_length=16, verbose_name='локальный ip в офисе')
    port = models.CharField(max_length=16, verbose_name='порт')
    slots_count = models.SmallIntegerField(null=True, verbose_name="колличество слотов")
    comment = models.CharField(max_length=500, blank=True, default='', verbose_name="комментарий")

    class Meta:
        verbose_name = "Офисный шлюз"
        verbose_name_plural = "Офисные шлюзы"

    def __str__(self):
        text = str(self.type_gateway) + ""+str(self.slots_count)+" ("+str(self.local_ip)+")"
        return text

class Office_Simcard(models.Model):
    gateway = models.ForeignKey(Office_Gateway, on_delete=models.CASCADE, verbose_name="шлюз")
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, verbose_name="клиент")
    channel_name = models.CharField(max_length=30, verbose_name="название канала")
    sim_number = models.CharField(max_length=20, blank=True, default="", verbose_name="номер сим-карты")
    call_forwarding = models.CharField(max_length=20, blank=True, default="", verbose_name="на какой номер переадресация")
    in_use = models.BooleanField(default=False, verbose_name="в использовании?")

    class Meta:
        verbose_name = "сим-карта в офисе"
        verbose_name_plural = "сим-карты в офисе"

    def __str__(self):
        text = str(self.channel_name)+"("+str(self.sim_number)+") - "+str(self.client)
        return text
