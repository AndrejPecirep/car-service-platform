from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.service')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_appointments', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='vehicles.vehicle')),
            ],
        ),
    ]
