n = int(input("Enter number of transactions:"))
transactions = []
i = 0
while i < n:
    t = int(input("Enter amount:"))
    transactions = transactions + [t]
    i = i + 1
data = {
    "normal": [] ,
    "large": [] ,
    "high": [] ,
    "invalid": [] ,
}
for t in transactions:
    if t <= 0:
        data["invalid"] = data["invalid"] + [t]
    elif t <= 500:
        data["normal"] = data["normal"] + [t]
    elif t <= 2000:
        data["large"] = data["large"] + [t]
    else:
        data["high"] = data["high"] + [t]
values = [x for x in transactions if x > 0]
total = 0
count = 0
for v in values:
    total = total + v
    count = count + 1
many = 0
if count > 5:
    many = 1
big = 0
if total > 5000:
    big = 1
high_num = 0
for x in data["high"]:
    high_num = high_num + 1
warn = 0
if high_num >= 3:
    warn = 1
risk = "Low Risk"
if many == 1 or big == 1:
    risk = "Moderate Risk"
if warn == 1:
    risk = "High Risk"
Summary = (total, count, risk)
print("Data:", data)
print("Total:", total)
print("Count:", count)
print("Risk:", risk)
print("Summary:", Summary)