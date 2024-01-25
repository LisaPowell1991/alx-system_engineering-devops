# Testing how well our web server setup
# featuring Nginx is doing under pressure and
# it turns out it is not doing well:
# we are getting a huge amount of failed requests.

# Increase limit
exec { 'increase_limit':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/bin:/usr/bin',
}

# Restart Nginx
exec { 'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
