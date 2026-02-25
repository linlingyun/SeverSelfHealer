# OpenClaw Sentinel 🦞

A lightweight, proactive server self-healing agent designed for OpenClaw environments.

## Features
- **Docker Auto-Heal**: Monitors specific containers (like `antigravity-manager`) and restarts them instantly if they crash.
- **Cache Purge**: Automatically detects and cleans up massive pip/system caches to prevent OOM or Disk-Full errors.
- **Log Monitoring**: Keeps an eye on system health and reports via local logs (and optional Telegram notifications).
- **Resource Efficient**: Runs as a cron job with near-zero CPU/RAM overhead.

## Installation
1. Clone the repo.
2. Run `bash setup.sh`.

## Requirements
- Python 3.x
- Docker (optional)
