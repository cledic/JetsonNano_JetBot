# Configurare la Jetson Nano per assorbire 10W o 5W

https://forums.developer.nvidia.com/t/jetson-nano-shuts-down-during-the-inference-in-10w-mode/107347

## Modo 5W
```
sudo nvpmodel -m 1
```

## Modo 10W
```
sudo nvpmodel -m 0
```
