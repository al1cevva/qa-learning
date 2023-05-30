from dataclasses import dataclass

@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email: str = None
    subject: str = None
    number: str = None
    address: str = None
    permanentAddress: str = None