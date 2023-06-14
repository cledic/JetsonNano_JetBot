from jetbot.utils.utils import get_ip_address
import subprocess
from Battery_Vol_Lib import BatteryLevel

BatteryLevel = BatteryLevel()

cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
CPU = subprocess.check_output(cmd, shell = True )
cmd = "free -m | awk 'NR==2{printf \"Mem:%s/%sM %.2f%%\", $3,$2,$3*100/$2 }'"
MemUsage = subprocess.check_output(cmd, shell = True )
cmd = "df -h | awk '$NF==\"/\"{printf \"Disk:%d/%dGB %s\", $3,$2,$5}'"
Disk = subprocess.check_output(cmd, shell = True )

temp = BatteryLevel.Update()
print(CPU)
print(Disk)
print(temp)
