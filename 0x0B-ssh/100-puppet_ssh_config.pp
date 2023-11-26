# using Puppet, make changes to the config file.
# set up your client SSH configuration file so that you can connect to a server without typing a password.
# Requirements:
# Your SSH client configuration must be configured to use the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to authenticate using a password

include stdlib

file_line { 'Turn off passwd auth':
    path => '/etc/ssh/sshd_config',
    line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
}
