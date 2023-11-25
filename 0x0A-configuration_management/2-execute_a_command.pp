# Using Puppet, create a manifest that kills a process named killmenow.

# Requirements:
# Must use the exec Puppet resource
# Must use pkill

exec { 'killmenow':
    command  => 'pkill -f killmenow',
    path     => ['/bin', '/usr/bin'],
    onlyif   => 'pgrep -f killmenow',
}
