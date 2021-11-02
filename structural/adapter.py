"""
One Adpater allow two inconpatible classes work together
Use Composition always you can
Else, use Inheritance
"""
from abc import ABC, abstractmethod


class IControl(ABC):

    @abstractmethod
    def top(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass

    @abstractmethod
    def down(self) -> None:
        pass

    @abstractmethod
    def left(self) -> None:
        pass


class Control(IControl):

    def top(self) -> None:
        print('Moving to top')

    def right(self) -> None:
        print('Moving to right')

    def down(self) -> None:
        print('Moving to down')

    def left(self) -> None:
        print('Moving to left')


class NewControl:
    def move_top(self) -> None:
        print('NewControl: Moving to top')

    def move_right(self) -> None:
        print('NewControl: Moving to right')

    def move_down(self) -> None:
        print('NewControl: Moving to down')

    def move_left(self) -> None:
        print('NewControl: Moving to left')


class ControlAdapter:
    """Adapter Object - Composition"""

    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    """Adapter Class - Inheritance"""

    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == "__main__":

    new_control = NewControl()

    control_object = ControlAdapter(new_control)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    print()

    # Control Class - Adapter Class

    control_class = ControlAdapter2()

    control_class.top()
    control_class.down()
    control_class.left()
    control_class.right()
