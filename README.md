# pi-plant

### A timelapse script that uploads the resultant GIF to Github

---

## Set up the Raspberry Pi
1) Download the Raspberry Pi Linux image, Raspbian from [the raspberry pi website](https://www.raspberrypi.com/software/).
2) Use the tool to flash your sd card.
3) Insert the flash drive into your Raspberry Pi.
4) Plug the Raspberry Pi into a monitor and keyboard. 
5) Plug the Raspberry Pi into a power supply.
6) Follow the setup process.
7) Plug the Raspberry Pi into the internet.

## Download the Github CLI
In the Raspberry Pi terminal follow [this tutorial](https://lindevs.com/install-github-cli-on-raspberry-pi/)

To save some time the next time you log into the Raspberry Pi, add the command to log in to your `.bashrc` file:
```
cd
echo "gh auth login --with-token < ~/token.txt" >> .bashrc
```
Now, You will be logged in automatically the next time you start the Pi.

## Add an ssh key to your Github Account
On the Raspberry Pi, open a terminal and run the following commands:
```
ssh-keygen
```
Hit `enter` three times to:
1) Install the key in the default location (/home/pi/.ssh/id_rsa).
2) Decline a passphrase.
3) Confirm that you do not want to add a passphrase to the ssh key.

Add the key to GitHub:
```
gh ssh-key add .ssh/id_rsa.pub
```

Configure your Git username and email:
```
git config --global user.email "<YOUR EMAIL>"
git config --global user.name "<YOUR USERNAME>"
```

Now clone this repository:
```
git clone git@github.com:chaukap/pi-plant.git 
```

Navigate to it:
```
cd pi-plant
```

## Install python dependencies
```
pip3 install opencv-python
```
