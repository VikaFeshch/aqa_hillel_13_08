from datetime import datetime, timedelta


def analyze_heartbeat(log_file_path, output_file_path):
    filtered_log = []
    key_to_filter = "Key TSTFEED0300|7E3E|0400"

    # Читання файлу та фільтрація рядків з потрібним ключем
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if key_to_filter in line:
                filtered_log.append(line.strip())
                print(line.strip())

    with open(output_file_path, 'w') as output_file:
        previous_timestamp = None

        # Аналіз кожного відфільтрованого рядка
        for line in filtered_log:
            timestamp_index = line.find("Timestamp ") + len("Timestamp ")
            timestamp_str = line[timestamp_index:timestamp_index + 8]
            current_timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

            if previous_timestamp:
                # Обчислення інтервалу
                interval = (current_timestamp - previous_timestamp).total_seconds()

                # Логування відповідно до інтервалу
                if 31 < interval < 33:
                    output_file.write(f"WARNING: Heartbeat {interval} sec at {current_timestamp}\n")
                elif interval >= 33:
                    output_file.write(f"ERROR: Heartbeat {interval} sec at {current_timestamp}\n")

            previous_timestamp = current_timestamp


# Використання:
analyze_heartbeat('hblog.txt', 'hb_test.log')
