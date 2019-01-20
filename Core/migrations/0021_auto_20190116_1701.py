# Generated by Django 2.1.5 on 2019-01-16 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0020_auto_20190116_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='contato',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='ramal',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='status_chamado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Status_Chamado', verbose_name='Status'),
        ),
    ]