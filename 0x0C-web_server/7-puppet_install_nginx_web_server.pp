# configuring your server with Puppet to install Nginx

#Install Nginx
package { 'nginx':
    ensure => installed,
}

#Ensure Nginx is running and enabled
service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
}

# Create a basic HTML file with Hello World!
file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => 'Ceci n\'est pas une page',
    require => Package['nginx'],
}

# Define a Nginx location for the 301 redirect
nginx::resource::location { '/redirect_me':
    ensure        => present,
    location      => '/redirect_me',
    server        => 'default',
    location_cfg  => {
         'return' => '301 http://www.example.com/destination',
    },
    notify        => Service['nginx'],
    require       => Package['nginx'],
}

