from dataclasses import dataclass
from enum import Enum


class Processor(Enum):
    Slow = '52'
    Medium = '53'
    Fast = '65'

    def to_human_readable(self):
        return self.name


class RAM(Enum):
    GB_8 = '91'
    GB_2 = '54'
    GB_4 = '55'

    def to_human_readable(self):
        return f'{self.name.split('_')[1]} GB'


class HDD(Enum):
    GB_320 = '57'
    GB_400 = '58'

    def to_human_readable(self):
        return f'{self.name.split('_')[1]} GB'


@dataclass
class Computer:
    processor: Processor
    ram: RAM
    hdd: HDD


computer = Computer(Processor.Fast, RAM.GB_2, HDD.GB_320)
