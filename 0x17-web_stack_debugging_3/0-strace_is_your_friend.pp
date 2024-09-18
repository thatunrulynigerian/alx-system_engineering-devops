# This Puppet manifest fixes the Apache 500 Internal Server Error.

class apache_fix {
    # Ensure that the required files and directories exist
    file { '/var/www/html/index.html':
        ensure => file,
        source => 'puppet:///modules/apache/index.html', # Update with your file source
        mode   => '0644',
        owner  => 'www-data',
        group  => 'www-data',
    }

    # Ensure the correct permissions on the web directory
    file { '/var/www/html':
        ensure => directory,
        mode   => '0755',
        owner  => 'www-data',
        group  => 'www-data',
    }

    # Restart Apache to apply changes
    service { 'apache2':
        ensure => running,
        enable => true,
        subscribe => File['/var/www/html/index.html'],
    }
}

# Apply the class
include apache_fix
