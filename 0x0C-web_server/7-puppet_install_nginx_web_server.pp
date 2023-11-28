# configuring your server with Puppet to install Nginx

#Install Nginx
package { 'nginx':
    ensure => installed,
}

# Define Nginx configuration
file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => "# Nginx configuration file
server {
    listen 80;
}

    # Redirect /redirect_me to the desired location with a 301 Moved Permanently
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    # Set the default root to serve Hello World! at /
    location / {
        root /var/www/html;
        index index.nginx-debian.html;
    }
}",
  notify  => Service['nginx'],
}

# Create a basic HTML file with Hello World!
file { '/var/www/html/index.nginx-debian.html':
    ensure  => 'file',
    content => 'Hello World!',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default', '/var/www/html/index.nginx-debian.html'],
}
