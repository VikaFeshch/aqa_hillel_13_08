from datetime import datetime


def analyze_heartbeat(log_file_path, output_file_path):
    filtered_log = []
    key = "Key TSTFEED0300|7E3E|0400"

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if key in line:
                filtered_log.append(line.strip())

    filtered_log.reverse()

    if not filtered_log:
        print("No row with the specified key was found")
        return

    with open(output_file_path, 'w') as output_file:
        previous_timestamp = None

        for line in filtered_log:
            timestamp_index = line.find("Timestamp ") + len("Timestamp ")
            timestamp_str = line[timestamp_index:timestamp_index + 8]

            print(f"Row: {line}")
            print(f"Period of time: {timestamp_str}")
            current_timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

            if previous_timestamp:
                interval = (current_timestamp - previous_timestamp).total_seconds()
                print(f'Interval between messages: {interval} сек, current time {current_timestamp.strftime("%H:%M:%S")}')

                # logs for interval
                if 31 < interval < 33:
                    output_file.write(f'WARNING: Heartbeat {interval} sec at {current_timestamp.strftime("%H:%M:%S")}\n')
                elif interval >= 33:
                    output_file.write(f'ERROR: Heartbeat {interval} sec at {current_timestamp.strftime("%H:%M:%S")}\n')

            previous_timestamp = current_timestamp


analyze_heartbeat('hblog.txt', 'hb_test.log')

