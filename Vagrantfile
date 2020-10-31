# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/xenial64"

  # Application Server
  config.vm.define "app" do |app|
    app.vm.hostname = "senaite-xenial"
    app.vm.box = "ubuntu/xenial64"
    app.vm.provision "shell", inline: "apt-get install -y python aptitude"
    app.vm.network :private_network, ip: "192.168.33.10"
  end

   config.vm.provider "virtualbox" do |vb|
     # Don't boot with headless mode
  #   vb.gui = true
     # Use VBoxManage to customize the VM. For example to change memory:
     vb.customize ["modifyvm", :id, "--memory", "4096"]
     vb.customize ["modifyvm", :id, "--cpus", "2"]
   end
end
