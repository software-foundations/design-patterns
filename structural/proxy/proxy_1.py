"""
- Proxy is a Class with the same interface of another
- Proxy seams (but far) to decorator
- Use proxy object instead of real object
- Kinds of proxy
    1. virtual: controll resource access
    2. remote: control remote resource access
    3. protection: control resource protection
    4. inteligence: increase inteligence in resource access

- Proxy can do many things:
    1. Authenticate users
    2. Create logs
    3. Distribute services
    4. Create cache
    5. Create and destroy objects
    6. Postpone 
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict

class IUser(ABC):
    """Subject Interface"""
    first_name: str    
    last_name: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        """get user address (abstract method)"""

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        """get all user data (abstract method)"""


class RealUser():
    """Real Subject"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """initialization method for concrete user"""
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def get_addresses() -> List[Dict]:
        """get user address (concrete method)"""

        # simulating a request
        sleep(2)

        return [
            {'street': "Av. Brasil", 'number': 500}
        ]

    @staticmethod
    def get_all_user_data() -> Dict:
        """get all user data (concrete method)"""
        # simulating a request
        sleep(2)

        return {
            'cpf': '111.111.111-11',
            'rg': '1231234'
        }


class UserProxy(IUser):
    """User Proxy"""

    def __init__(self, first_name: str, last_name: str) -> None:
        """initialization method (proxy method)"""
        self.first_name = first_name
        self.last_name = last_name

        # lazy instantiation
        self._real_user: RealUser

        # caching to increase speed
        # objects still not exist at this point of code
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        """get real user"""
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.first_name, self.last_name)

    def get_addresses(self) -> List[Dict]:
        """get user address (proxy)"""
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_all_user_data()

        return self._cached_addresses


if __name__ == '__main__':

    bruno = UserProxy('Bruno', 'Conde')

    print(bruno.first_name)
    print(bruno.last_name)

    print(bruno.get_all_user_data())
    print(bruno.get_addresses())

    # Responds instantaneously
    print('CACHED DATA:')
    for i in range(50):
        print(i, bruno.get_addresses())
