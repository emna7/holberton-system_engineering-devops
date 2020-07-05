# Change the OS configuration
exec {'holberton hard':
command => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 65534/g' /etc/security/limits.conf; /sbin/sysctl -p",
path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
exec {'holberton soft':
command => "sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 65534/g' /etc/security/limits.conf; /sbin/sysctl -p",
path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
