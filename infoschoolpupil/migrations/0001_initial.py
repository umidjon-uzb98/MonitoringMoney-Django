# Generated by Django 4.1.5 on 2023-03-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PupilMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.PositiveBigIntegerField(blank=True, default=1, null=True)),
                ('classNum', models.CharField(max_length=255)),
                ('monday_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('tuesday_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('wednesday_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('thursday_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('friday_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('saturday_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('weekly_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('monthly_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('yearly_spendMoney', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'PupilMoney',
                'verbose_name_plural': 'PupilMoney',
            },
        ),
    ]