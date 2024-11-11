import re
from datetime import datetime, timedelta


def analyze_heartbeat(log_file_path, output_file_path):
    key_to_filter = "Key TSTFEED0300|7E3E|0400"
    pattern = re.compile(r"Timestamp (\d{2}:\d{2}:\d{2}) " + re.escape(key_to_filter))
    previous_timestamp = None

    with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
        for line in log_file:
            match = pattern.search(line)
            if match:
                timestamp_str = match.group(1)
                current_timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

                if previous_timestamp:
                    # Calculate heartbeat interval
                    interval = (current_timestamp - previous_timestamp).total_seconds()

                    # Log warnings and errors based on interval range
                    if 31 < interval < 33:
                        output_file.write(f"WARNING: Heartbeat {interval} sec at {current_timestamp}\n")
                    elif interval >= 33:
                        output_file.write(f"ERROR: Heartbeat {interval} sec at {current_timestamp}\n")

                previous_timestamp = current_timestamp


# Example usage:
analyze_heartbeat('hblog.txt', 'hb_test.log')
