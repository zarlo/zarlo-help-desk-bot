import string
flags0To9 = [
    ':zero:',
    ':one:',
    ':two:',
    ':three:',
    ':four:',
    ':five:',
    ':six:',
    ':seven:',
    ':eight:',
    ':nine:',
] 

hex_flags = [
    flags0To9,
    [ regional(code) for code in string.ascii_lowercase[6:] ]
]

def regional(code):
    return ':regional_indicator_{0}:'.format(code)

def hexToInt(hex):
    return int(hex, 16)

def intToHex(number):
    return '{:x}'.format(hex(number))