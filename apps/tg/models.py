
from statistics import mode
from tabnanny import verbose
from time import time
from django.db import models

class Users(models.Model):
    time = models.DateTimeField(
        verbose_name='Дата и время регистрации (UTC)',
        auto_now_add=True,
        null=True
    )
    external_id = models.PositiveIntegerField(
        verbose_name='Telegram ID',
        unique=True,
        null=True
    )
    username = models.CharField(
        verbose_name='Ник',
        max_length=30,
        null=True
    )

    def __str__(self):
        return f'{self.external_id}'

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзеры'

class Items(models.Model):
    name = models.CharField(
        verbose_name='Название пакета',
        max_length=100,
        null=True
    )
    price = models.PositiveBigIntegerField(
        verbose_name='Цена пакета (в копейках, не меньше 10000)',
        null=True
    )
    description = models.CharField(
        verbose_name='Описание пакета',
        max_length=100,
        null=True
    )
    cells = models.PositiveBigIntegerField(
        verbose_name='Кол-во ячеек',
        null=True
    )
    active_time = models.DateTimeField(
        verbose_name='Срок действия',
        auto_now_add=False,
        null=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class PaymentHistory(models.Model):
    time = models.DateTimeField(
        verbose_name='Дата и время транзакции (UTC)',
        auto_now_add=True,
        null=True
    )
    external_id = models.PositiveIntegerField(
        verbose_name='Telegram ID',
        unique=False,
        null=True
    )
    summ = models.PositiveBigIntegerField(
        verbose_name='Сумма',
        null=True
    )
    comment = models.CharField(
        verbose_name='Комментарий',
        max_length=100,
        null=True
    )

    def __str__(self):
        return f'{self.external_id}', f'{self.summ}'

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

class ChatBase(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Telegram ID владельца',
        unique=True,
        null=True
    )
    chat = models.CharField(
        verbose_name='Название чата',
        max_length=512,
        null=True
    )

    class Meta:
        verbose_name = 'Чат база'
        verbose_name_plural = 'База чатов'

class Profiles(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Telegram ID',
        unique=True,
        null=True
    )
    ref_count = models.PositiveIntegerField(
        verbose_name='Рефералы',
        default=0
    )
    sub_ref_count = models.PositiveBigIntegerField(
        verbose_name='Суб-рефералы',
        default=0
    )
    cells_count = models.PositiveBigIntegerField(
        verbose_name='Кол-во ячеек (всего)',
        default=0
    )

    cells_occupied = models.PositiveBigIntegerField(
        verbose_name='Занято ячеек',
        default=0
    )
 
    team_volume = models.PositiveBigIntegerField(
        verbose_name='Размер комманды (всего)',
        default=1
    )

    team_occupied = models.PositiveBigIntegerField(
        verbose_name='Размер комманды',
        default=1
    )
    
    wallet = models.PositiveBigIntegerField(
        verbose_name='Кошелёк Голды',
        default=0
    )
    chats = models.ManyToManyField(ChatBase)

    def get_chats(self):
        return [ChatBase.chats for ChatBase in self.chats.all()]

    # def __int__(self):
    #     return self.ref_count, self.sub_ref_count, self.items_count, self.wallet

    class Meta:
        verbose_name = 'Профиль юзера'
        verbose_name_plural = 'Профили юзеров'

class ReferalBase(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Telegram ID',
        unique=True,
        null=True
    )
    from_who = models.PositiveIntegerField(
        verbose_name='Кто пригласил',
        null=True
    )
    referals = models.ManyToManyField(Users)

    def get_refs(self):
        return [Users.external_id for Users in self.referals.all()]


    class Meta:
        verbose_name = 'Рферал база'
        verbose_name_plural = 'База рефералов'

class Tags(models.Model):
    tag = models.CharField(
        verbose_name='Ключевое слово',
        max_length=512,
        null=False,
        unique=True
    )
    class Meta:
        verbose_name = 'Список ключевых слов'

class ParseSettings(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Telegram ID',
        null=True
    )
    chat = models.ManyToOneRel(ChatBase)
    tags = models.ManyToManyField(Tags)
    def get_tags(self):
        return [Tags.tag for Tags in self.tags.all()]
    class Meta:
        verbose_name = 'Настройки парсера'
