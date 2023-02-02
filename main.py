# Copyright (c) 2023 PANTHEON.tech s.r.o. All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v1.0 which accompanies this distribution,
# and is available at http://www.eclipse.org/legal/epl-v10.html

from json import dumps
import pandas as pd
from httplib2 import Http

url = 'webhook_url'
df = pd.read_csv('file.csv')
df_length = df.shape[0]
df = df.iloc[::-1]
line_counter = 0

for index, row in df.iterrows():
    line_counter += 1
    time = row['Post Creation Time']
    sender_name = row['User Name']
    message_body = row['Post Message']

    if isinstance(message_body, float):
        if isinstance(time, float):
            user_input = input(f"Please upload files from {df.loc[index+1,'Post Creation Time']} uploaded by {df.loc[index+1,'User Name']} and pres any key to continue")
        else:
            user_input = input(f"Please upload files from {time} uploaded by {sender_name} and pres any key to continue")
    else:
        bot_message = {
            "text": f"*{time.split(' ')[0]}*  *{sender_name}*\n{message_body}"}
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        http_obj = Http()
        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message)
        )

    print(f"Progress: {round((line_counter / df_length)*100, 2)}%")