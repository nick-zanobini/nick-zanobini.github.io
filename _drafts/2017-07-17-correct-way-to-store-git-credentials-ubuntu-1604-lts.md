This was answered here: What is the correct way to use git with gnome-keyring and http(s) repos?

Quoting the answer:

You need to setup the git credential helper with Gnome Keyring:

Install and compile the Gnome Keyring devel:

sudo apt-get install libgnome-keyring-dev
sudo make --directory=/usr/share/doc/git/contrib/credential/gnome-keyring
And setup the credential:

git config --global credential.helper /usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring

https://askubuntu.com/questions/740183/store-git-credentials-permanently-and-encrypted-using-a-keystore-in-ubuntu