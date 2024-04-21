# Generated by Django 4.2.11 on 2024-04-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_produto_alter_cadastro_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='estoque',
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='produtos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]