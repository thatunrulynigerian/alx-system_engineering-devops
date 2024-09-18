# a puppet code to fix a wordpress site 5xx error to 200 ok
# edit the mistyped .phpp to php in the /var/www/html/wp-settings.php file

exec { 'fix-wordpess-server-error':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
