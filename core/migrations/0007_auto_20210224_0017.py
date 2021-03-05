# Generated by Django 3.1.2 on 2021-02-24 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201224_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(default=0)),
                ('st_count', models.IntegerField(default=0)),
                ('mn_count', models.IntegerField(default=0)),
                ('rn_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='story',
            name='page',
            field=models.CharField(choices=[('st', 'Slo-tech'), ('mn', 'Monitor'), ('rn', 'Racunalniske novice')], max_length=3),
        ),
    ]