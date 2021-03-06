# Generated by Django 3.0.6 on 2020-05-25 17:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20200525_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Course')),
            ],
        ),
    ]
