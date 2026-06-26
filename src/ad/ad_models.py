from dataclasses import dataclass


@dataclass
class ADUser:
    name: str
    dn: str


@dataclass
class ADGroup:
    name: str
    dn: str


@dataclass
class ADComputer:
    name: str
    dn: str