# Generated by Django 4.0.5 on 2022-06-06 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='doubts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.trainer')),
                ('_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.trainee')),
            ],
        ),
    ]
