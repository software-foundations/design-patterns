"""
Bridge seams to adapter
- Bridge make things works after they exist
- Adapter make thing works after the have been implemented
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    """Interface RemoteControl"""

    @abstractmethod
    def increase_volume(self) -> None:
        """increase volume (abstract method)"""

    @abstractmethod
    def decrease_volume(self) -> None:
        """decrease volumne (abstract method)"""

    @abstractmethod
    def power(self) -> None:
        """ turn on/off (abstract method)"""


class RemoteControl(IRemoteControl):
    """Concrete Remote Control"""

    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        """ get power state (concrete)"""
        self._device.power = not self._device.power


class IDevice(ABC):
    """ Abstract Device"""
    @property
    @abstractmethod
    def volume(self) -> int:
        """returns the volume (abstract method)"""

    @volume.setter
    def volume(self, volume: int) -> None:
        """return the volume (abstract)"""

    @property
    @abstractmethod
    def power(self) -> bool:
        """get power state (abstract method)"""

    @power.setter
    def power(self, value: bool) -> None:
        """set power state (abstract method)"""


class TV(IDevice):
    """Concrete Device"""

    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        """get the volume (abstract method)"""
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        """get the volume (concrete IDevice)"""
        if not self._power:
            print(f'Please, turn {self._name} ON')

        if volume > 100:
            return

        if volume < 0:
            return

        self._volume = volume

        print(f'{self.__class__.__name__} volume is now {self._volume}')

    @property
    def power(self) -> bool:
        """get power state (concrete method)"""
        return self._power

    @power.setter
    def power(self, value: bool) -> None:
        """set power state (concrete method)"""
        self._power = value
        power_status = 'ON' if self._power else 'OFF'
        print(f'{self._name} is now {power_status}')


class Radio(TV):
    """It is not recommended to inherit from concrete class
    Don't do this in real case"""


class RemoteControlWithMute(RemoteControl):
    """Subclass of RemoteControl"""

    def mute(self) -> None:
        """Mute the volume"""
        self._device.volume = 0


if __name__ == "__main__":

    tv = TV()
    control_tv = RemoteControl(tv)

    # only to test
    # control_tv.increase_volume()

    control_tv.power()
    control_tv.increase_volume()
    control_tv.decrease_volume()
    control_tv.power()

    radio = Radio()
    control_radio = RemoteControlWithMute(radio)

    control_radio.power()
    control_radio.increase_volume()
    control_radio.decrease_volume()
    print('MUTE')
    control_radio.mute()
    control_radio.power()
