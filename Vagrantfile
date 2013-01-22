Vagrant::Config.run do |config|
  config.vm.box = "precise64"
  config.vm.share_folder "dora", "/var/dora", "."
  config.vm.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/dora", "1"]
  config.vm.forward_port 5556, 5555
  config.vm.forward_port 8080, 8080
  config.vm.customize [ "modifyvm", :id, "--memory", "1024", "--cpus", "2" ]

  config.vm.provision :puppet, :options => "--verbose --debug" do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.module_path = "puppet/modules"
    puppet.manifest_file = "site.pp"
  end
end
