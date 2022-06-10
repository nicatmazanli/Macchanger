#!/usr/bin/env python3
import subprocess
import optparse
import re
import os
os.system("clear")
os.system("figlet KARABAGH  IS AZERBAIJAN")
try:
    def paraser():
        parse_obj = optparse.OptionParser()
        parse_obj.add_option("-i", "--interface", dest="interface", help="-i --interface Interface \n")
        parse_obj.add_option("-m", "--mac", dest="mac_address", help="-m --mac New Mac Address\n")
        return parse_obj.parse_args()


    def change(user_interface, user_mac_address):
        subprocess.call(["ifconfig", user_interface, "down"])
        subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
        subprocess.call(["ifconfig", user_interface, "up"])


    def control_mac(new_interface):
        ifconfig = subprocess.check_output(["ifconfig", new_interface])
        new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
        print(new_mac.group(0))

        if new_mac:
            return new_mac
        else:
            return None


    print("Starting Mac Changer....")
    (user_inputs, arguments) = paraser()
    change(user_inputs.interface, user_inputs.mac_address)
    new_mac_control = control_mac(str(user_inputs.interface))

    if new_mac_control.group(0) == user_inputs.interface:
        os.system("
                  ifconfig")
        print("\nPoseydons says: 'Karabagh is AZERBAIJAN'")


    else:
        print("\n[+]Succeed")
        print("\nPoseydons says: 'Karabagh is AZERBAIJAN'")


except TypeError:
    print("Please input mac address and interface :\n\n ./macchanger.py -i <interface> -m <mac_address>\n\n "
          "./macchanger.py --interface <interface> --mac <mac_address>")
