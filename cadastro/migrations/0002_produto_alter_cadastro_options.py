# Generated by Django 4.2.11 on 2024-04-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.AlterModelOptions(
            name='cadastro',
            options={'ordering': ['-data'], 'verbose_name': 'Formulário de cadastro', 'verbose_name_plural': 'Formulário de cadastro'},
        ),
    ]
