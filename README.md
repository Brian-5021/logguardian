# LogGuardian

**LogGuardian** is a Python-based security log analyzer designed to identify suspicious authentication activity in application log files.

The project demonstrates log parsing, event filtering, time-based pattern detection, automated testing, and modular Python development.

## Features

- Discovers and reads `.log` files.
- Parses log entries into structured events.
- Filters relevant `WARNING` and `ERROR` events.
- Identifies failed authentication attempts using configurable message patterns.
- Groups failed authentication events by source IP address.
- Detects a potential brute-force pattern when at least three matching events from the same IP occur within 30 seconds.
- Generates a console report with the detected IP, event counts, and sequence duration.
- Includes automated tests for detection thresholds, IP separation, and unordered events.

## Project Structure

```text
logguardian/
├── main.py
├── lector.py
├── analizador.py
├── detector.py
├── patrones.py
├── reportes.py
├── logs/
│   ├── access.log
│   └── error.log
└── tests/
    └── test_patrones.py
```

## Requirements

- Python 3.14 or a compatible Python version.
- `pytest` to run the automated tests.

## Run the Analyzer

From the project root, run:

```bash
python main.py
```

The application processes the configured log directory and prints a report to the console.

## Run the Tests

Run:

```bash
python -m pytest
```

The tests validate the current detection rules and expected behavior.

## Detection Logic

LogGuardian looks for configured failed-authentication message patterns. It groups matching events by source IP and orders them chronologically.

A potential brute-force pattern is reported when three matching events from the same IP occur within a maximum interval of 30 seconds.

## Limitations

- Detection depends on the log format and configured message patterns.
- The current detection rule is heuristic and may produce false positives or miss attacks that use different log messages.
- The tool analyzes log files; it does not block IP addresses or prevent authentication attempts.
- A detection result is an indicator for investigation, not proof of a successful attack.

## Purpose

This project is part of a practical learning portfolio focused on Python automation and application security.

It is intended for educational use with authorized log data.