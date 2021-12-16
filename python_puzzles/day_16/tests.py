from .clean_2 import Parser, hex_to_bin

imap = {
    "C200B40A82": 3,
    "04005AC33890": 54,
    "880086C3E88112": 7,
    "CE00C43D881120": 9,
    "D8005AC2A8F0": 1,
    "F600BC2D8F": 0,
    "9C005AC2F8F0": 0,
    "9C0141080250320F1802104A08": 1,
}

for i, val in imap.items():
    if Parser(hex_to_bin(i)).next() != val:
        print(f"Failed Test {i}")
    else:
        print(f"Suceeded Test {i}")
