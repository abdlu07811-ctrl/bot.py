from instagrapi import Client

cl = Client()

username = "OS.wd"
password = "07823520Aa"

cl.login(username, password)

cl.dump_settings("instagram_session.json")

print("✅ تم تسجيل الدخول")
