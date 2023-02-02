# Copyright (c) 2023 PANTHEON.tech s.r.o. All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v1.0 which accompanies this distribution,
# and is available at http://www.eclipse.org/legal/epl-v10.html


## Google workspace import:
    This program import chat history from exported Mattermost CSV file.

## Installing
    PREREQUISITE:
        - New workspace created in Google chat
        - Webhook address from this new created channel (Channel options --> Manage webhooks --> Create and copy webhook_url)
        - Mattermost channel export CSV file
            (channel can be exported with //export command directly in MM channel)
        - Python 3.8+
        - Python libraries: pandas, httplib2
    GET THE CODE:
        git clone "https://github.com/MarioDoman/google-workspace-import-bot.git"
    NAVIGATE TO:
        cd google-workspace-import-bot
    INSTALL VIRTUAL ENVIRONMENT PACKAGE:
        sudo apt install python3-virtualenv
    CREATE NEW VIRTUAL ENVIRONMENT:
        virtualenv venv
    ACTIVATE VIRTUAL ENVIRONMENT:
        . venv/bin/activate
    INSTALL LIBRARIES:
        pip install pandas httplib2

## RUN
# COPY CSV
    - copy exported CSV file in to google-workspace-import-bot directory
    - change webhook_address address with your web_hook channel address in main.py line 11 (url = 'webhook_address')
    - change file name according to your csv file in main.py line 12 (df = pd.read_csv('file.csv'))

# UPLOADING FILES
    - if you want to import also images or other files, you need to do it manually
    - program will stop where file was uploaded due to empty "Post message" cell on that row
      (if not, please add blank line in to CSV file where you need program to make pause for uploading file)
    - while running, program will make a pause for uploading the file you want
    - after uploading, press enter in to console to continue

# RUNNING
    - run command: python3 main.py

# LOGS
    - if everything is going well, you will see a percentage progress in terminal
    - if a pause occur, you will see message like this:
      "Please upload files from 2020-04-22 08:05:35.348 +0000 UTC uploaded by name.surname and pres any key to continue"
