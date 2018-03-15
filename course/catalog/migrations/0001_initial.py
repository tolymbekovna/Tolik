# Generated by Django 2.0.2 on 2018-03-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Есімін енгізініз', max_length=200)),
                ('last_name', models.CharField(help_text='Тегін енгізініз', max_length=200)),
                ('email', models.CharField(help_text='Почта енгізініз', max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Есімін енгізініз', max_length=200)),
                ('last_name', models.CharField(help_text='Тегін енгізініз', max_length=200)),
                ('email', models.CharField(help_text='Почта енгізініз', max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
