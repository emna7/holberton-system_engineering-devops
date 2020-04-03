# automate the task of creating a custom HTTP header response with Puppet

exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

-> package {'nginx':
  ensure => present,

}

-> file_line { 'header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

-> exec { 'ngnix':
  command  => 'sudo service nginx restart',
  provider => shell,
}
