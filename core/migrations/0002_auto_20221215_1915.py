# Generated by Django 3.0 on 2022-12-15 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_stad', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Postion',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RateType',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('time', models.DateField()),
                ('duration_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Duration')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('club_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('has_legua', models.BooleanField(default=False)),
                ('size', models.FloatField()),
                ('section_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='')),
                ('deleted', models.BooleanField(default=True)),
                ('search_game', models.BooleanField(default=True)),
                ('temp', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField()),
                ('rateType_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.RateType')),
                ('user_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team_resevation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Reservation')),
                ('team_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Team_members',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('is_captin', models.BooleanField(default=True)),
                ('player_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Player')),
                ('position_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Postion')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='type_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='core.Type'),
        ),
        migrations.CreateModel(
            name='SubManager',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StadiumService',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
                ('service_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Service')),
                ('stad_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Stadium')),
            ],
        ),
        migrations.CreateModel(
            name='StadiumRate',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('rate_type_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.RateType')),
                ('stad_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Stadium')),
            ],
        ),
        migrations.AddField(
            model_name='stadium',
            name='type_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='core.Type'),
        ),
        migrations.AddField(
            model_name='section',
            name='subManager_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='core.SubManager'),
        ),
        migrations.CreateModel(
            name='Player_reservation',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Player')),
                ('reservation_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Reservation')),
            ],
        ),
        migrations.CreateModel(
            name='permission',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rule_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Rule')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_kind', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('reciver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='reciver_id', to=settings.AUTH_USER_MODEL)),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='sender_id', to=settings.AUTH_USER_MODEL)),
                ('team_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='core.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='duration',
            name='stad_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='core.Stadium'),
        ),
        migrations.AddField(
            model_name='club',
            name='manager_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='core.Manager'),
        ),
    ]
