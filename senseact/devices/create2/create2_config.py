from collections import OrderedDict

# Create2 opcode info for each possible command keyed on the opcode ID, include
# param range for commands that make sense
OPCODE_INFO = {
    7: {'name': 'reset'},
    128: {'name': 'start'},
    129: {'name': 'baud'},
    131: {'name': 'safe'},
    132: {'name': 'full'},
    133: {'name': 'power'},
    134: {'name': 'spot'},
    135: {'name': 'clean'},
    136: {'name': 'max'},
    # TODO: support discontinuous action space for drive radius 32767, 32768
    137: {'name': 'drive', 'params': OrderedDict([('velocity', [-500, 500]), ('radius', [-2000, 2000])])},
    138: {'name': 'motors'},
    139: {'name': 'led'},
    140: {'name': 'song'},
    141: {'name': 'play'},
    142: {'name': 'sensors'},
    143: {'name': 'seek_dock'},
    144: {'name': 'motors_pwm'},
    145: {'name': 'drive_direct', 'params': OrderedDict([('left', [-150, 150]), ('right', [-150, 150])])},
    146: {'name': 'drive_pwm'},
    148: {'name': 'stream'},
    149: {'name': 'query_list'},
    150: {'name': 'pause_resume_stream'},
    162: {'name': 'scheduling_led'},
    163: {'name': 'digit_led_raw'},
    164: {'name': 'digit_led_ascii'},
    165: {'name': 'buttons'},
    167: {'name': 'schedule'},
    168: {'name': 'set_day_time'},
    173: {'name': 'stop'}}

OPCODE_NAME_TO_CODE = dict((v['name'], k) for k, v in OPCODE_INFO.items() if 'name' in v)

# Create2 sensor packet definition keyed on the packet ID
PACKET_INFO = {
    # ===== Group packets =====
    0:   {'subpackets': list(range(7, 27))},
    1:   {'subpackets': list(range(7, 17))},
    2:   {'subpackets': list(range(17, 21))},
    3:   {'subpackets': list(range(21, 27))},
    4:   {'subpackets': list(range(27, 35))},
    5:   {'subpackets': list(range(35, 43))},
    6:   {'subpackets': list(range(7, 43))},
    100: {'subpackets': list(range(7, 59))},
    101: {'subpackets': list(range(43, 59))},
    102: {'subpackets': list(range(46, 52))},
    103: {'subpackets': list(range(54, 59))},

    # ===== Sensor packets =====
    7:  {'fmt': '-', 'name': 'bumps and wheel drops',
         'range': [0, 15]},
    8:  {'fmt': 'B', 'name': 'wall',
         'range': [0, 1]},
    9:  {'fmt': 'B', 'name': 'cliff left',
         'range': [0, 1]},
    10: {'fmt': 'B', 'name': 'cliff front left',
         'range': [0, 1]},
    11: {'fmt': 'B', 'name': 'cliff front right',
         'range': [0, 1]},
    12: {'fmt': 'B', 'name': 'cliff right',
         'range': [0, 1]},
    13: {'fmt': 'B', 'name': 'virtual wall',
         'range': [0, 1]},
    14: {'fmt': '-', 'name': 'wheel overcurrents',
         'range': [0, 31]},
    15: {'fmt': 'B', 'name': 'dirt detect',
         'range': [0, 255]},
    16: {'fmt': 'B', 'name': 'unused byte',
         'range': [0, 0]},
    17: {'fmt': 'B', 'name': 'infrared character omni',
         'range': [0, 255]},
    18: {'fmt': '-', 'name': 'buttons',
         'range': [0, 255]},
    19: {'fmt': 'h', 'name': 'distance',
         'range': [-32768, 32767]},
    20: {'fmt': 'h', 'name': 'angle',
         'range': [-32768, 32767]},
    21: {'fmt': 'B', 'name': 'charging state',
         'range': [0, 5]},
    22: {'fmt': 'H', 'name': 'voltage',
         'range': [0, 65535]},
    23: {'fmt': 'h', 'name': 'current',
         'range': [-32768, 32767]},
    24: {'fmt': 'b', 'name': 'temperature',
         'range': [-128, 127]},
    25: {'fmt': 'H', 'name': 'battery charge',
         'range': [0, 65535]},
    26: {'fmt': 'H', 'name': 'battery capacity',
         'range': [0, 65535]},
    27: {'fmt': 'H', 'name': 'wall signal',
         'range': [0, 1023]},
    28: {'fmt': 'H', 'name': 'cliff left signal',
         'range': [0, 4095]},
    29: {'fmt': 'H', 'name': 'cliff front left signal',
         'range': [0, 4095]},
    30: {'fmt': 'H', 'name': 'cliff front right signal',
         'range': [0, 4095]},
    31: {'fmt': 'H', 'name': 'cliff right signal',
         'range': [0, 4095]},
    32: {'fmt': 'b', 'name': 'unused 1',
         'range': [0, 0]},
    33: {'fmt': 'h', 'name': 'unused 2',
         'range': [0, 0]},
    34: {'fmt': '-', 'name': 'charging sources available',
         'range': [0, 3]},
    35: {'fmt': 'B', 'name': 'oi mode',
         'range': [0, 3]},
    36: {'fmt': 'B', 'name': 'song number',
         'range': [0, 15]},
    37: {'fmt': 'B', 'name': 'song playing',
         'range': [0, 1]},
    38: {'fmt': 'B', 'name': 'number of stream packets',
         'range': [0, 108]},
    39: {'fmt': 'h', 'name': 'requested velocity',
         'range': [-500, 500]},
    40: {'fmt': 'h', 'name': 'requested radius',
         'range': [-32768, 32767]},
    41: {'fmt': 'h', 'name': 'requested right velocity',
         'range': [-500, 500]},
    42: {'fmt': 'h', 'name': 'requested left velocity',
         'range': [-500, 500]},
    43: {'fmt': 'h', 'name': 'left encoder counts',
         'range': [-32768, 32767]},
    44: {'fmt': 'h', 'name': 'right encoder counts',
         'range': [-32768, 32767]},
    45: {'fmt': '-', 'name': 'light bumper',
         'range': [0, 127]},
    46: {'fmt': 'H', 'name': 'light bump left signal',
         'range': [20, 4095]},
    47: {'fmt': 'H', 'name': 'light bump front left signal',
         'range': [20, 4095]},
    48: {'fmt': 'H', 'name': 'light bump center left signal',
         'range': [20, 4095]},
    49: {'fmt': 'H', 'name': 'light bump center right signal',
         'range': [20, 4095]},
    50: {'fmt': 'H', 'name': 'light bump front right signal',
         'range': [20, 4095]},
    51: {'fmt': 'H', 'name': 'light bump right signal',
         'range': [20, 4095]},
    52: {'fmt': 'B', 'name': 'infrared character left',
         'range': [0, 255]},
    53: {'fmt': 'B', 'name': 'infrared character right',
         'range': [0, 255]},
    54: {'fmt': 'h', 'name': 'left motor current',
         'range': [-32768, 32767]},
    55: {'fmt': 'h', 'name': 'right motor current',
         'range': [-32768, 32767]},
    56: {'fmt': 'h', 'name': 'main brush motor current',
         'range': [-32768, 32767]},
    57: {'fmt': 'h', 'name': 'side brush motor current',
         'range': [-32768, 32767]},
    58: {'fmt': 'B', 'name': 'stasis',
         'range': [0, 3]}
}

PACKET_NAME_TO_ID = dict((v['name'], k) for k, v in PACKET_INFO.items() if 'name' in v)
