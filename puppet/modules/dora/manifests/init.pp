class dora {
  package { 'git': ensure => present, }
  package { 'htop': ensure => present, }
  package { 'vim': ensure => present, }

  package { 'libfreetype6-dev': ensure => present, }
  package { 'libpng12-dev': ensure => present, }
  package { 'libzmq-dev': ensure => present, }
  package { 'python-dev': ensure => present, }
  package { 'curl': ensure => present, }
  
  # installing these with virtualenv causes issues
  # pip continues installing other packages while numpy is still installing.
  package { 'python-pip': ensure => present, }
  package { 'python-scitools': ensure => latest, }
  package { 'matplotlib':
    ensure => latest,
    provider => pip,
    require => Package['libfreetype6-dev', 'libpng12-dev', 'python-scitools'],
  }
  package { 'tornado': ensure => present, provider => pip, }
  package { 'pyzmq':
    ensure => present,
    provider => pip,
    require => Package['libzmq-dev', 'python-dev'],
  }
  package { 'ipython':
    ensure => latest,
    provider => pip,
    require => Package['tornado', 'pyzmq'],
  }
  package { 'pandas':
    ensure => latest,
    provider => pip,
    require => Package['python-scitools'],
  }
  package { 'httplib2': ensure => present, provider => pip, }
  package { 'google-api-python-client': ensure => present, provider => pip, }

  file { '/etc/init/dora.conf':
    ensure  => present,
    source => 'puppet:///modules/dora/dora.conf',
  }

  file { '/etc/init.d/dora':
    ensure => link,
    target => '/etc/init/dora.conf'
  }

  file { '/var/log/dora':
    ensure => directory,
  }

  service {'dora':
    ensure => running,
    provider => 'upstart',
    require => [File['/etc/init.d/dora'], Package['ipython', 'pandas']] ,
  }
}
