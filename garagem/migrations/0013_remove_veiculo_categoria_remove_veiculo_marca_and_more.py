# Generated by Django 4.2.4 on 2023-08-29 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0012_alter_veiculo_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="veiculo",
            name="categoria",
        ),
        migrations.RemoveField(
            model_name="veiculo",
            name="marca",
        ),
        migrations.AddField(
            model_name="modelo",
            name="categoria",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modelo",
                to="garagem.categoria",
            ),
            preserve_default=False,
        ),
    ]