# Create a in tmp with basic requirents
file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet',
}
