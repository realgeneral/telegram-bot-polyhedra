#!/bin/bash

pip install --no-cache-dir --upgrade -r requirements.txt

while true; do
    python3 -m app.main
    exit_code=$?
    if [ $exit_code -eq 0 ]; then
        # Команда успешно завершилась, выходим из скрипта
        exit
    else
        # Команда выбросила ошибку, ждем некоторое время перед перезапуском
        sleep 5
    fi
done
