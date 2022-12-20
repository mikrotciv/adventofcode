"""Day 6: Tuning Trouble"""
from collections import defaultdict
from pathlib import Path

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

def get_start_of_packet(stream: str, packet_size: int) -> int:
    """Reads packet stream and returns the position of start-of-packet"""
    # Sliding window
    start = 0
    end = start
    start_of_packet = defaultdict(int)
    while end != len(stream):
        start_of_packet[stream[end]] += 1

        # Sliding window not reach max size
        if end-start+1 < packet_size:
            end += 1
            continue

        # Found 'packet_size' unique characters
        if len(start_of_packet.keys()) == packet_size and \
            sum(start_of_packet.values()) == packet_size:
            return end+1 # As we want one char after end of start of packet

        # Shift the window
        start_of_packet[stream[start]] -= 1
        if start_of_packet[stream[start]] == 0:
            del start_of_packet[stream[start]]
        start += 1
        end += 1
    return -1

def main():
    """Print solutions"""
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        stream = input_file.readline()

    print(f"Part 1: {get_start_of_packet(stream, 4)}")
    print(f"Part 2: {get_start_of_packet(stream, 14)}")

if __name__ == "__main__":
    main()
