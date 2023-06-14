#!/usr/bin/env python3

# https://github.com/chrisb2/pi_ina219
#
from ina219 import INA219
from ina219 import DeviceRangeError
import time

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0

def battery_state(batt):
    if batt >= 12:
        return 'Battery_High'
    elif batt >= 11.1:
        return 'Battery_Medium'
    elif batt >= 10.05:
        return 'Battery_Low'
    #
    if batt <= 9.9:
        return 'Battery_Empty'
    elif batt <= 10.95:
        return 'Battery_Low'
    elif batt <= 11.85:
        return 'Battery_Medium'


ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS, address=0x41, busnum=1)
ina.configure(ina.RANGE_16V)

while True:
    Battery_vol = ina.voltage()

    print("Battery State: %s" % battery_state(Battery_vol))
    print("Bus Voltage: %.3f V " % ina.voltage())

    try:
        print("Bus Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)


    time.sleep(3)
    print("")
        
