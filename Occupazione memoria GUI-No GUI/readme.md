# Gestione del GUI

- https://github.com/NVIDIA-AI-IOT/jetbot/issues/440
If you run 4.3 version of Jetpack, it is better to run code at no-GUI mode(so call multi-user.target). 
If you want to make 4.5.1 version as GUI (graphical.target) mode, you can change it to GUI mode, but it takes most of 
RAM memory which result in very slow run of Jetbot. Same is true in 4.3 version if it is operating at GUI mode. 
Therefore it is better to run code at no-gui mode when use 4.3 version also. I think the reason of slow performance of 4.3 version 
could be related to small available RAM memory due to the gui mode. You can disable the gui mode. 
To disable GUI on boot, run: sudo systemctl set-default multi-user.target


- Toglie il GUI: ATTENZIONE: il WiFi non voleva andare: perdeva l'IP dopo il boot.
```
sudo systemctl set-default multi-user.target
```

- Programma nuovamente il GUI
```
sudo systemctl set-default graphical.target
```

- Nella modalità senza GUI, per farlo connettere al WiFi, ho dovuto eseguire questo comando:
```
sudo nmcli device wifi connect <SSID> password <password>
```

- Questi comandi li ho presi da questa pagina: https://jetbot.org/master/software_setup/sd_card.html
e sono indicati per la nuova versione di JetBot che parte senza GUI.
