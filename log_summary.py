# v1
import os
import random

# function to create log file


def create_log_file(filename, num_lines):
    # 20 lines are created in the file, with each line being a random choice between (pass, fail, untested)
    os.makedirs("log_files", exist_ok=True)
    filepath = os.path.join("log_files", filename)
    results = ['pass', 'fail', 'untested']
    with open(filepath, 'w') as file:
        for _ in range(num_lines):
            file.write(f"{random.choice(results)}\n")

# function to read log file


def read_log_file(filename):
    # return all the lines from the file to be counted
    filepath = os.path.join("log_files", filename)
    log_data = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # remove any extra leading or traling whitespace for each line
            log_data.append(line.strip())
        return log_data

# function to generate and print the summary for each log file


def generate_summary(log_files):
    summary = {}
    for log_file in log_files:
        log_data = read_log_file(log_file)
        summary[log_file] = {
            "pass": log_data.count("pass"),
            "fail": log_data.count("fail"),
            "untested": log_data.count("untested")
        }
        # for testing purposes
        print(f"{log_file} (pass: {log_data.count('pass')}, fail: {log_data.count('fail')}, untested: {log_data.count('untested')})\n")
    return summary


log_files = [f"hardware{i}.log" for i in range(1, 11)]
