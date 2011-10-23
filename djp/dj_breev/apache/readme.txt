o run under apache perform the following steps
0. install apache2 
   sudo apt-get install apache2
   
   install libapache2-mod-wsgi
   (this cann also be done via the Synaptic Package Manager) 


check the files in this directory
1. /wsgi/dj_breev.wsgi
   this file is referenced by file /conf/dj_breef

2. The following directive should be added to /etc/apache2/ports.conf
Listen 8080

3. /conf/dj_breef
   in this file the VirtualHost on port 8080 directive is defined

   make this file available to apache by an symbolic link
   /etc/apache2/sites-available$ sudo ln -sf /home/nos/workspaces/auk/djp/dj_breev/apache/conf/dj_breev


4. enable the new dj_breev site with the a2ensite command
   (this script also creates a symbolic link
   , using the script seems the default way 
     to enable or disable an available sitein Apache) 
   /etc/apache2/sites-available$ sudo a2ensite dj_breev

5. in settings.py change the following entries
   - database hostname

6. in urls.py
   - comment static urls out, let the static urls be serviced by apache instead of django

7. start apache2
   sudo /etc/init.d/apache2 restart

