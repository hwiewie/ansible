指令：

git add .

git commit -m "first commit"

git pull origin master

git push -u origin master

production        # inventory file for production.
staging           # inventory file for staging.

group_vars/
├ group1         # here we assign variables to particular groups
├ group2
host_vars/
├ hostname1      # if systems need specific variables, put them here
├ hostname2
library/          # 任何自己寫或自己維護 (也就是非 Built-in) 的 module 都建議放這邊
module_utils/     # 個人很少在用
filter_plugins/   # 任何自己寫或自己維護 (也就是非 Built-in) 的filter 都建議放這邊
roles/
├ common/        # role name
   ├tasks/       #   
     ├main.yml   # main tasks file.
   ├handlers/    #
     ├main.yml   # handlers file.
   ├templates/   #
     ├ntp.conf.j2# templates end in .j2.
   ├files/       #   
     ├bar.txt    # files
     ├foo.sh     # script files
   ├vars/        #
     ├main.yml   # variables with this role.
   ├defaults/    #
     ├main.yml   # default variables.
   ├meta/        #
     ├main.yml   # role dependencies
site.yml          # master playbook
webservers.yml    # playbook for webserver tier
dbservers.yml     # playbook for dbserver tier

git@github.com:hwiewie/ansible.git

git@github.com:Azure/sonic-mgmt.git

git@github.com:linagora/hublin-ansible.git

git@github.com:HewlettPackard/hpe3par_ansible_module.git

git@github.com:fdavis/ansible-best-practices.git

git@github.com:mikechau/ansible-boilerplate.git

git@github.com:edx/configuration.git

git@github.com:openshift/openshift-ansible.git

git@github.com:senaite/senaite.ansible-playbook.git

git@github.com:openzfs/openzfs-ci.git

git@github.com:dev-sec/ansible-os-hardening.git

git@github.com:splunk/splunk-ansible.git

git@github.com:gchq/stroom-ansible.git

git@github.com:flathub/ansible-playbook.git

git@github.com:splunk/splunk-ansible.git

git@github.com:easzlab/kubeasz.git

git@github.com:kairen/kube-ansible.git

git@github.com:Tobewont/ansible-playbook.git
