"""
Broker Settings
"""
from threading import Lock
import MetaTrader5


class BrokerSettingsMeta(type):
    """
    Broker Settings metaclass.
    """

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class BrokerSettings(metaclass=BrokerSettingsMeta):
    """
    Broker Settings class.
    """

    account: int = 0
    password: str = ""
    server: str = ""
    type_time: int = MetaTrader5.ORDER_TIME_GTC
    type_filling: int = MetaTrader5.ORDER_FILLING_RETURN
