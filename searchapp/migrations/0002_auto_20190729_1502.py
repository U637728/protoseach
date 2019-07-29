# Generated by Django 2.1.9 on 2019-07-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorytbl',
            options={'verbose_name_plural': 'カテゴリマスタ'},
        ),
        migrations.AlterModelOptions(
            name='goodstbl',
            options={'verbose_name_plural': '商品マスタ'},
        ),
        migrations.AlterModelOptions(
            name='highcategorytbl',
            options={'verbose_name_plural': '上位カテゴリマスタ'},
        ),
        migrations.AlterField(
            model_name='categorytbl',
            name='categoryid',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='カテゴリID'),
        ),
        migrations.AlterField(
            model_name='highcategorytbl',
            name='highcategoryid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='上位カテゴリID'),
        ),
        migrations.AlterUniqueTogether(
            name='goodstbl',
            unique_together={('productno', 'sizename', 'colorname')},
        ),
    ]
