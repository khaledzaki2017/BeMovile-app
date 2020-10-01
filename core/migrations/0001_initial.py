# Generated by Django 2.2 on 2020-09-30 22:44

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='phoneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile', models.IntegerField()),
                ('isVerified', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WizardForm',
            fields=[
                ('email', models.EmailField(default='', max_length=254, primary_key=True, serialize=False, unique=True)),
                ('_type', models.CharField(max_length=100, null=True)),
                ('personal_id', models.TextField(max_length=250, null=True)),
                ('firstname', models.CharField(max_length=250, null=True)),
                ('lastname', models.CharField(max_length=250, null=True)),
                ('bemovil_id', models.IntegerField(null=True)),
                ('expedition_date', models.DateField(null=True)),
                ('expedition_place', models.CharField(max_length=250, null=True)),
                ('mobile_phone', models.IntegerField(null=True)),
                ('number', models.IntegerField(null=True)),
                ('address', models.TextField(max_length=250, null=True)),
                ('city', models.CharField(max_length=250, null=True)),
                ('valley', models.CharField(max_length=250, null=True)),
                ('company_name', models.CharField(max_length=250, null=True)),
                ('actividad_economica', models.CharField(max_length=250, null=True)),
                ('direccion', models.TextField(max_length=250, null=True)),
                ('barrio', models.CharField(max_length=250, null=True)),
                ('ciudad', models.CharField(max_length=250, null=True)),
                ('departamento', models.CharField(max_length=250, null=True)),
                ('mobile_phone_fin', models.IntegerField(null=True)),
                ('email_fin', models.EmailField(default='', max_length=254, null=True, unique=True)),
                ('telefono_fijo', models.IntegerField(blank=True, null=True)),
                ('ingresos', models.IntegerField(blank=True, null=True)),
                ('total_activos', models.IntegerField(blank=True, null=True)),
                ('egresos', models.IntegerField(blank=True, null=True)),
                ('total_pasivos', models.IntegerField(blank=True, null=True)),
                ('uploader', models.CharField(max_length=250, null=True)),
                ('firstFile', models.FileField(upload_to='documents')),
                ('secondFile', models.FileField(upload_to='documents')),
                ('file', models.BinaryField(null=True)),
                ('name_info', models.CharField(max_length=250, null=True)),
                ('email_info', models.EmailField(default='', max_length=254, null=True, unique=True)),
                ('lastname_info', models.CharField(max_length=250, null=True)),
                ('number_info', models.IntegerField(null=True)),
                ('id_image1', models.ImageField(null=True, upload_to='user_images/id_images')),
                ('id_image2', models.ImageField(null=True, upload_to='user_images/id_images')),
                ('client_image1', models.ImageField(null=True, upload_to='user_images/')),
                ('client_image2', models.ImageField(null=True, upload_to='user_images/')),
                ('client_image3', models.ImageField(null=True, upload_to='user_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_razonsocial', models.TextField(max_length=250, null=True)),
                ('participacion', models.IntegerField(null=True)),
                ('identification', models.CharField(max_length=250, null=True)),
                ('number', models.IntegerField(null=True)),
                ('ciudad', models.CharField(max_length=250, null=True)),
                ('direccion', models.CharField(max_length=250, null=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WizardForm')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
