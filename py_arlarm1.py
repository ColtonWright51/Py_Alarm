
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from playsound import playsound
import os
import pygame
import time

def main():

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevel(-30.0, None)
    playsound(r'C:\Users\colto\Documents\GitHub\Py_Alarm\songs\Coldplay - Viva La Vida.mp3')
    # playsound(r'C:\Users\colto\Documents\GitHub\Py_Alarm\songs\loud_alarm.mp3')
    playsound(r'C:\Users\colto\Documents\GitHub\Py_Alarm\songs\loud_alarm.mp3')
    volume.SetMasterVolumeLevel(-18.0, None)
    playsound(r'C:\Users\colto\Documents\GitHub\Py_Alarm\songs\The Last Bear Ender - The Only Thing They Fear Is You.mp3')
    playsound(r'C:\Users\colto\Documents\GitHub\Py_Alarm\songs\Eminem - The Way I Am.mp3')

if __name__ == "__main__":
    main()