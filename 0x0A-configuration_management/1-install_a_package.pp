# Using Puppet, install flask from pip3.

# Requirements:
# Install flask
# Version must be 2.1.0

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}

package { 'Werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
}
