# Generated by Django 2.0.7 on 2018-07-09 16:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('email_id', models.EmailField(max_length=254)),
                ('ph_no', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be a valid number. ', regex='^\\+?1?\\d{9,15}$')])),
                ('reg_date', models.DateField()),
                ('last_login', models.DateTimeField()),
                ('last_activity_ip', models.GenericIPAddressField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]