# This manifest fixes the limit for number of open files

file {'/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 4096"',
  notify  => Exec['restart-nginx']
}

exec {'restart-nginx':
  command     => 'service nginx restart',
  path        => '/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}
