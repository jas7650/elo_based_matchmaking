import trueskill

r1 = trueskill.Rating()
r2 = trueskill.Rating()
r3 = trueskill.Rating()
r4 = trueskill.Rating()

rating_list = [r1, r2, r3, r4]
for rating in rating_list:
    print(rating)

t1 = [r1, r2]
t2 = [r3, r4]

print(f"Chance to draw: {100*trueskill.quality([t1, t2])}%")
(r1, r2), (r3, r4) = trueskill.rate([t1, t2], ranks=[0, 1])

for rating in rating_list:
    print(rating)
t1 = [r1, r2]
t2 = [r3, r4]
print(f"Chance to draw: {100*trueskill.quality([t1, t2])}%")
