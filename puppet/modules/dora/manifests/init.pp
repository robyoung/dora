class dora {
  package {[
    'git',
    'htop',
    'vim',
    'libfreetype6-dev',
    'libpng12-dev',
    'libzmq-dev',
    'python-dev',
    'curl',
    'python-pip',
    'python-scitools',
  ]:
    ensure => present
  }

  package {[
    'tornado',
    'httplib2',
    'google-api-python-client',
    'jinja2',
  ]:
    ensure   => present,
    provider => pip,
  }

  # installing these with virtualenv causes issues
  # pip continues installing other packages while numpy is still installing.
  package { 'matplotlib':
    ensure   => latest,
    provider => pip,
    require  => Package['libfreetype6-dev', 'libpng12-dev', 'python-scitools'],
  }
  package { 'pyzmq':
    ensure   => present,
    provider => pip,
    require  => Package['libzmq-dev', 'python-dev'],
  }
  package { 'ipython':
    ensure   => latest,
    provider => pip,
    source   => 'git+git://github.com/robyoung/ipython.git',
    require  => Package['tornado', 'pyzmq'],
  }
  package { 'pandas':
    ensure   => latest,
    provider => pip,
    require  => Package['python-scitools'],
  }

  file { '/etc/init/dora.conf':
    ensure => present,
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
    ensure   => running,
    provider => 'upstart',
    require  => [File['/etc/init.d/dora'], Package['ipython', 'pandas']] ,
  }
}
