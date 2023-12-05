# Automate the task of creating a custom HTTP header response, but with Puppet.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to get the hostname of the server
facter::add('server_hostname') {
  setcode 'hostname'
}

# Use exec to append custom header to Nginx configuration
exec { 'configure_nginx_custom_header':
  command     => 'echo "add_header X-Served-By $hostname;" >> /etc/nginx/sites-available/default',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  subscribe   => Package['nginx'],
  notify      => Service['nginx'],
}

# Enable the custom Nginx site
nginx_site { 'default':
  ensure => present,
}

# Restart Nginx when the configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['configure_nginx_custom_header'],
}
