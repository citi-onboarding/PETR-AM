# Generated by Django 2.1.3 on 2018-11-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181129_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='foto',
            field=models.ImageField(default='core/static/imagens/servicos/servicosImgTeste.jpg', upload_to='servicos/'),
        ),
    ]
