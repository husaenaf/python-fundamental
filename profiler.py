import json

from typing import Any

with open("leader-profile.json", 'r+') as files:
    profiles: list[dict[str,Any]] = json.loads(files.read())
    print(profiles)

    # proses parsing data
    for i in profiles:
        print("Name: {}, gender: {}, email: {}".format(i['first_name'], i['gender'], i['email']))