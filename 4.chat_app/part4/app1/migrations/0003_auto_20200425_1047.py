# Generated by Django 3.0 on 2020-04-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200424_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
