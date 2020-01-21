+++
title = "Multiple Ssh Keys"
date = 2020-01-21T12:32:54-07:00
draft = true
markup = "mmark"
+++

1. Created new public/private key pair (run `ssh-keygen -t rsa` and choose a new file name e.g. 'id_rsa_jenkins'. This way your existing key won't get overwritten.)
1. Put public key in access keys on Bitbucket
1. Put private key in Jenkins
1. Make sure you are using the SSH URL

## Create new keys

You probably already have keys that you are using so create some different keys.

```sh
ssh-keygen -t rsa
# add a new file path for the new keys
# don't overwrite you old keys
```

![Bitbucket Repo Settings](/img/jenkins-ssh-keys/bitbucket-repo-settings.png)

![Add SSH key on Jenkins](/img/jenkins-ssh-keys/jenkins-add-ssh-key.png)

![Add SSH Key on Jenkins](/img/jenkins-ssh-keys/jenkins-add-ssh-key-button.png)

