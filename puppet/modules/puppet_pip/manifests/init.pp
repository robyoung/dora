class puppet_pip {
  package { "puppet-pip":
    ensure => latest,
    provider => "gem",
  }
}
