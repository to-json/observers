from abc import ABC, abstractmethod
from dataclasses import dataclass

from observers.observers.base import Record


@dataclass
class Store(ABC):
    """
    Base class for storing records
    """

    @abstractmethod
    def add(self, record: Record):
        """Add a new record to the store"""
        pass

    @abstractmethod
    def connect(self):
        """Connect to the store"""
        pass

    @abstractmethod
    def _init_table(self, record: "Record"):
        """Initialize the table"""
        pass
