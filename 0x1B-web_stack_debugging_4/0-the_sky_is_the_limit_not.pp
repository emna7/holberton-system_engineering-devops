# fixing the failing requests
exec {'/etc/default/ngix':
path    => ['/usr/bin', '/bin'],
command => "sudo sed -i 's/-n 15/-n 2000/g' /etc/default/nginx; sudo service nginx restart",
}
