# Generated by Django 4.0.1 on 2022-01-19 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan_card', models.FileField(default='', upload_to='files')),
                ('aadhar_card', models.FileField(default='', upload_to='files')),
                ('bank_statment', models.FileField(default='', upload_to='files')),
                ('photo', models.ImageField(default='', upload_to='image')),
                ('signature', models.ImageField(default='', upload_to='image')),
                ('salary_slip', models.FileField(default='', upload_to='files')),
                ('from16', models.FileField(default='', upload_to='files')),
                ('blance_sheet', models.FileField(default='', upload_to='files')),
                ('itr', models.FileField(default='', upload_to='files')),
                ('business_proof', models.FileField(default='', upload_to='files')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer')),
            ],
        ),
    ]