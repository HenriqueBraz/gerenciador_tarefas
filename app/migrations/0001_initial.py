# Generated by Django 2.2.4 on 2019-09-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=100)),
                ('data_expiracao', models.DateField()),
                ('prioridade', models.CharField(choices=[('A', 'Alta'), ('B', 'Normal'), ('C', 'Baixa')], max_length=1)),
            ],
        ),
    ]
