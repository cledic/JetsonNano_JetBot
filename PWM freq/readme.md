# Modificare la velocità dei motori.

Un problema che subito è evidente nell'usare il Jetbot è che risponde ai comandi di movimento con dei veloci scatti.
L'unica soluzione che ho trovato è stata abbassare la freq. dei PWM utilizzando i costrutti che riporto di seguito.

>Looking into the Adafruit_MotorHAT library, which has the calls for the motor controller, I can set the PWM using the following call. 
>This call works because the Robot class instantiates an Adafruit_MotorHAT object. This object has a set PWMFreq method, which we can 
>call right after instantiating the robot object:
>A PWM frequency of 100 Hz seems to stop the whining!

Dalle prove che ho eseguito, il valore che ho trovato migliore è **50**

```
robot = Robot()
robot.motor_driver._pwm.setPWMFreq(50)
```


https://forums.developer.nvidia.com/t/where-to-change-motor-pwm-switching-frequency-on-jetbot-4-3-image/181788/16
