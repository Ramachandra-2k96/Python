response1 = {
    "id": "g6-nanode-1",
    "label": "Nanode 1GB",
    "price": {
        "hourly": 0.0075,
        "monthly": 5.0
    }
}
with open('qwa.txt','w')as f:
    ram_capacity = response1["label"].replace("Nanode","")
    f.write(f"What is the RAM capacity of {response1['id']}? \nAns: {ram_capacity}")
    price_hourly = response1["price"]["hourly"]
    price_monthly = response1["price"]["monthly"]
    f.write(f"\nWhat is the Price of {response1['id']}? \nAns: Hourly: ${price_hourly}, Monthly: ${price_monthly}")
