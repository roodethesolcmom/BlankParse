# Generated by Django 4.0 on 2021-12-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0002_alter_profiles_items_count_alter_profiles_ref_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.PositiveBigIntegerField(max_length=100, null=True, verbose_name='Цена товара (в копейках, не меньше 10000)'),
        ),
        migrations.AlterField(
            model_name='items',
            name='volume',
            field=models.PositiveBigIntegerField(max_length=100, null=True, verbose_name='Кол-во сообщений'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='summ',
            field=models.PositiveBigIntegerField(max_length=100, null=True, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='items_count',
            field=models.PositiveBigIntegerField(default=0, max_length=100, verbose_name='Сообщения'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='ref_count',
            field=models.PositiveIntegerField(default=0, max_length=100, verbose_name='Рефералы'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='sub_ref_count',
            field=models.PositiveBigIntegerField(default=0, max_length=100, verbose_name='Суб-рефералы'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='wallet',
            field=models.PositiveBigIntegerField(default=0, max_length=100, verbose_name='Кошелёк'),
        ),
        migrations.AlterField(
            model_name='referalbase',
            name='from_who',
            field=models.PositiveIntegerField(max_length=100, null=True, verbose_name='Кто пригласил'),
        ),
        migrations.RemoveField(
            model_name='referalbase',
            name='referals',
        ),
        migrations.AddField(
            model_name='referalbase',
            name='referals',
            field=models.ManyToManyField(to='tg.Users'),
        ),
    ]
