# Generated by Django 2.1.3 on 2018-11-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usuario_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
