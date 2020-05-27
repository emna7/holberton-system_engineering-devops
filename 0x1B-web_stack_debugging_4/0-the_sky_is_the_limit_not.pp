exec { '/etc/default/ngix':
  command => 'sed -i s/15/4096/g /etc/default/ngix; \
  /etc/init.d/nginx restart',
  path    => ['/bin/'],
}
