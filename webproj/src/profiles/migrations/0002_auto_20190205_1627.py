# Generated by Django 2.1.5 on 2019-02-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('suburb', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
                ('street_number', models.IntegerField(blank=True, null=True)),
                ('unit_number', models.IntegerField(blank=True, null=True)),
                ('postcode', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('name', models.CharField(max_length=80, primary_key=True, serialize=False, verbose_name='Business Name')),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='Business Phone')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True, verbose_name='Optional Contact Mobile')),
                ('cont_name', models.CharField(blank=True, max_length=50, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture')),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateField(editable=False)),
                ('edited_at', models.DateField()),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'bussinesses',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Addresses', to='profiles.Business'),
        ),
    ]
