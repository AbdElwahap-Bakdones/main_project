# Generated by Django 3.0 on 2023-01-11 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20230111_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='player1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player11', to='core.Player'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='player2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player22', to='core.Player'),
        ),
    ]
