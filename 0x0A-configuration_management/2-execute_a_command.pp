# Using Puppet, create a manifest that kills a process named killmenow.

# Requirements:
# Must use the exec Puppet resource
# Must use pkill

exec { 'killmenow':
  command     => '/usr/bin/pkill -9 killmenow',
  refreshonly => true,
}
