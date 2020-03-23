# command
exec { 'pkill killmenow':
    path => '/usr/bin/pkill -f killmenow'
}
