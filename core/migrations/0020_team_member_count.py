# Generated by Django 3.0 on 2023-01-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20230116_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='member_count',
            field=models.IntegerField(default=1),
        ),
    ]