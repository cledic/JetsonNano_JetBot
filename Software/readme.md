# Script e programmi Python

## Shell script
Questi shell script sono comandi diretti per attiva/disattivare funzionalità

### GUI ON/OFF
Permette di attivare / disattivare la GUI, può essere utile per *liberare memoria* (**GUI OFF**) o per eseguire impostazioni dall'interfaccia grafica (**GUI ON**): *WiFi o Audio*.

### CLI WiFi Start
Prima di utilizzarlo, bisogna editare i due valori: **SSID** e **password**, del proprio WiFi. Permette la **configurazione del WiFi da CLI**, senza attivare il GUI grafico.

### Speed Up On/Off
Modifica la Jetson Nano, in modo da assorbire meno corrente. Si passa da *10W* con **speedUp_On** a *5W* con **speedUp_Off**. 

### I2C detect
Questo script eseguo lo scanner dei **due bus I2C** della Jetson
