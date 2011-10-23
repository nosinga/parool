echo   "-- python manage.py sql breev         >> database/breev.sql " >  database/breev.sql
           python manage.py sql breev         >> database/breev.sql

echo   "-- BEGIN SCRIPT"                                              >  database/django.sql
echo   "-- python manage.py sql contenttypes  >> database/django.sql" >> database/django.sql
           python manage.py sql contenttypes  >> database/django.sql
echo   "-- python manage.py sql auth          >> database/django.sql" >> database/django.sql
           python manage.py sql auth          >> database/django.sql
echo   "-- python manage.py sql admin         >> database/django.sql" >> database/django.sql
           python manage.py sql admin         >> database/django.sql
echo   "-- python manage.py sql sessions      >> database/django.sql" >> database/django.sql
           python manage.py sql sessions      >> database/django.sql
echo   "-- python manage.py sql sites         >> database/django.sql" >> database/django.sql
           python manage.py sql sites         >> database/django.sql
echo   "-- python manage.py sql messages      >> database/django.sql" >> database/django.sql
           python manage.py sql messages      >> database/django.sql
echo   "-- python manage.py sql reporting     >> database/django.sql" >> database/django.sql
           python manage.py sql reporting     >> database/django.sql
echo   "-- END SCRIPT"                                                >> database/django.sql
