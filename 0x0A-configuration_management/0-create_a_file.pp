# create a file 
file { '/tmp/holberton':
  ensure  => file,
  path    => '/tmp/holberton',
  content => ' I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
