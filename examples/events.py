import brawlstars as bs

client = bs.Client("token")

@client.on_battlelog_update("#88RLQL8PQ")
def on_battlelog_update(battles):
    print("New battles!")
    for item in battles:
        print(f"{item.event.map} | {item.battle.trophy_change} 🏆")

@client.on_member_join("#2GUU9908V")
def on_member_join(members):
    for member in members:
        print(f"{member.name} ({member.trophies} 🏆) has joined!")

@client.on_member_leave("#2GUU9908V")
def on_member_leave(members):
    for member in members:
        print(f"{member.name} ({member.trophies} 🏆) has left!")
