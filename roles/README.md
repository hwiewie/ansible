# Ansible Galaxy Roles

This folder contains roles distributed on https://galaxy.ansible.com,

To improve stability and remove the need for extra build steps, the roles are committed directly to this repo.

This is modeled on the DrupalVM repository. See https://github.com/geerlingguy/drupal-vm/tree/master/provisioning

## Adding and Updating Galaxy roles

To simplify role management, we've come up with a model for committing roles to code.

To update roles to the latest versions, just run `composer update` and commit
the result.

To install a new role, add it to `roles/roles.yml`, then run `composer update` 
to install the roles.

DevShop's `composer.json` file has a `post-update-cmd` hook that calls
`ansible-galaxy install` with the `--force` option.  

## Forking Roles

You can easily fork a role and include your version in this repository. 

Change the entry in `roles.yml` to point to your repository instead:

    # from GitHub, overriding the name and specifying a specific tag
    - src: https://github.com/bennojoy/nginx
      version: master
      name: nginx_role

## file structure

    .
    └── example_role
        ├── README.md     # 說明文件
        ├── defaults
        │   └── main.yml  # 可被覆寫的變數。
        ├── files         # 需複製到 Managed node 的檔案。
        ├── handlers
        │   └── main.yml  # 主要的 handler。
        ├── meta
        │   └── main.yml
        ├── tasks
        │   └── main.yml  # 主要的 task。
        ├── templates     # 集中存放 Jinja2 模板的目錄。
        ├── tests
        │   ├── inventory
        │   └── test.yml
        └── vars
            └── main.yml  # 不該被覆寫的變數。

根目錄

舉凡 LICENSE, README.md, Vagrantfile 以及 ansible.cfg 這類的說明、設定檔案，我都習慣將它們直接放在根目錄下。另外，由於在這個專案內我只有一個 inventory file，所以我也直接將其擺放在根目錄下，如果有多個 inventory files，還可以加入 group_vars/ 以及 host_vars/ 來定義不同環境下會用到的變數。除此之外，這個 Ansbile 專案內，我還放了三份不同的 playbook。

roles/

在這裡我存放了所有跟這個專案有關的 roles。由於每個 role 的結構類似，所以我以其中的 docker-jenkins 這個 role 來做簡單介紹：

defaults/

在這個資料夾下，通常被用來定義優先度較低的變數。除了 defaults/，習慣上我還會另外將只跟這個 role 有關的變數放在 vars/ 的資料夾下來做使用目的上的區分。關於 Ansbile 變數的優先權，可以參考官方在這裡的說明文件。

files/

這個資料夾內通常存放著這個 role 在部署過程中會需要使用或執行的檔案。

templates/

由於 Ansible 是用 Python 開發的一個自動化工具，所以也原生支援 Jinja2 這套模版引擎 (templating engine)。與 files/ 下的檔案不同，這個資料夾下的檔案通常都以 .j2 作為副檔名。Ansible 會根據執行環境、傳遞參數等等的不同在部署過程中來對 template file 做某種程度上調整。

tasks/

整個 role 中最核心的部分。這裡面定義了這個 role 的部署邏輯以及運行任務。在這個資料夾下可以不只有一個檔案，然後在 main.yml 裡定義何時呼叫其他檔案。

meta/

meta/ 資料夾內定義了這個 role 的依賴 (dependencies) 關係。以這個 docker-jenkins 為例，docker 這個 role 就是其依賴。在運行時，會在運行完 meta/ 內定義的所有 dependencies 後才接著執行 role 本身的任務。我們可以充分利用這個特色來重複組合及利用已經定義好的 role 以減少重造輪子的情況發生。

handlers/

我們會將所有 handlers 事件存放在這個目錄下。雖然這個專案並沒有使用到任何 handler，但 handler 是 Ansible 中非常好用的一個功能。我們可以根據 Ansible 運行時 tasks 狀態的改變來通知 (notify) handlers。最重要的特色是，無論有多少個 task notify 同一個 handler，該 handler 都只會運行一次。非常常見 handler 的實踐之一就是在檔案被修改後重啟 services。
