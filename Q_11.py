"""Following are the initials of players who play various games. Some of these players play more than one game.
Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football: [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]

Write a program to:
a.	List those players who play all three games.
b.	List those players who play exactly one game."""

cricket=["PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]
football=["PKM","ALN","RMZ","CS","MCS"]
badminton=["PKM","ALN","NV","KM","RMV"]
player=[]
player.extend(cricket)
player.extend(football)
player.extend(badminton)
lst=[]
lst1=[]
lst2=[]
c_names={ }

for name in player:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]=c_names[name]+1
lst=(c_names.values)
for k,value in c_names.items():
    if value==3:
        lst1.append(k)
    else:
        lst2.append(k)

print(f"Count of players playing all three games:{lst1}")
print(f"Count of players playing only one game:{lst2}")
