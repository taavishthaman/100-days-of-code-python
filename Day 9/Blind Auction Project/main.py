from art import logo
print(logo)
bid_dict = {}
bidders_left = True

while bidders_left:
    # TODO-1: Ask the user for input
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    # TODO-2: Save data into dictionary {name: price}
    bid_dict[name] = bid
    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there any other bidders? yes/no\n")
    if more_bidders == "yes":
        print("\n" * 100)
    else:
        bidders_left = False

# TODO-4: Compare bids in dictionary
res = ["",0]
for key in bid_dict:
    if bid_dict[key] > res[1]:
        res[0] = key
        res[1] = bid_dict[key]

print(f"{res[0]} made the highest bid of ${res[1]}.")

