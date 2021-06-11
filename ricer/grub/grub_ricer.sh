# Copy theme
sudo cp -r StarWars /usr/share/grub/themes/
sudo mv /etc/default/grub /etc/default/grub.bak
sudo cp grub /etc/default/grub 

# Make config
sudo grub-mkconfig -o /boot/grub/grub.cfg
