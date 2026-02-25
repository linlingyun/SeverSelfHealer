#!/bin/bash
echo "Installing OpenClaw Sentinel..."
mkdir -p /root/.openclaw/workspace/scripts
cp sentinel.py /root/.openclaw/workspace/scripts/
(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/bin/python3 /root/.openclaw/workspace/scripts/sentinel.py >> /root/.openclaw/workspace/scripts/sentinel.log 2>&1") | crontab -
echo "Sentinel deployed successfully!"
