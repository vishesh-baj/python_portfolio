print("Welcome to blind auction")

auction_over = False

auctions_list = []


def calculate_top_bidder(auction_list):
    max_bid = 0
    max_bidder = ""
    for auction in auction_list:
        for key in auction:
            if auction["bid_amount"] > max_bid:
                max_bid = auction["bid_amount"]
                max_bidder = auction["name"]
    print(f"MAX BID IS: {max_bid} BY: {max_bidder}")


while not auction_over:
    new_dict = {}
    name = input("Enter your name: ")
    bid_amount = int(input("Enter your bid amount: "))
    new_dict["name"] = name
    new_dict["bid_amount"] = bid_amount
    auctions_list.append(new_dict)
    print(auctions_list)
    should_continue = input("Are there any other bidders?:  ")
    if should_continue == "yes" or "YES" or "y":
        continue
    else:
        # calculate top bidder
        calculate_top_bidder(auctions_list)
        auction_over = True
