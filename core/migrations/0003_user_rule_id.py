# Generated by Django 3.0 on 2022-12-15 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221215_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rule_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Rule'),
        ),
    ]
