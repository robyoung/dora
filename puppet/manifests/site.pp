node default {
  exec { 'apt-update':
    command => '/usr/bin/apt-get update',
  }
  Exec['apt-update'] -> Package <| |>

  include dora
}
