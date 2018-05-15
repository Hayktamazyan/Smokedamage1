import json

def readData():
    with open('data.json') as data_file:
        data = json.load(data_file);
    smoked_packs = data["smoked_packs"];
    return smoked_packs;

def main():
    with open('data.json') as data_file:
        data = json.load(data_file);
    smoked_packs = data["smoked_packs"];
    if len(smoked_packs) == 0:
        price = float (input ("Input you cigarette price in drams "));
        nicotine = float (input ("Input you cigarette nicotine in milligrams "));
        cigarette = {"smoked_packs": [{"price": price, "nicotine": nicotine, "count": 0}]};
        file = open("data.json", "w");
        file.write(json.dumps(cigarette));
        file.close();
    else:
        price = smoked_packs[len(smoked_packs) - 1]["price"];
        nicotine = smoked_packs[len(smoked_packs) - 1]["nicotine"];
    while True:
        print"please select one of the following"
        print("1 - Get statistics.\n2 - Add count of packs you bought.\n3 - Change the type of cigarettes you somke.\n4 - Delete current data.\n5 - Exit");
        text = raw_input("Type here option you want -> ");
        if text == "1":
            smoked_packs = readData();
            total_money = 0.0;
            total_nicotine = 0.0;
            total_packs_count = 0;
            for cigarette in smoked_packs:
                total_money += float(cigarette["price"]) * int(cigarette["count"]);
                total_nicotine += float(cigarette["nicotine"]) * int(cigarette["count"]);
                total_packs_count += int(cigarette["count"]);
            print ("You have smoked " + str(total_packs_count * 20) + " cigarettes, which contained total of " + str(total_nicotine) + " milligrams of nicotine and spent " + str(total_money) + " AMD on that.");
        elif text == "2":
            smoked_packs = readData();
            count_of_added_packs = int(input ("    How many packs you have bought? "));
            smoked_packs[len(smoked_packs) - 1]["count"]+=count_of_added_packs;
            cigarette = {
                "smoked_packs" : smoked_packs
            };
            file = open("data.json", "w");
            file.write(json.dumps(cigarette));
            file.close();
            total_money = 0.0;
            total_nicotine = 0.0;
            total_packs_count = 0;
            for cigarette in smoked_packs:
                total_money += float(cigarette["price"]) * int(cigarette["count"]);
                total_nicotine += float(cigarette["nicotine"]) * int(cigarette["count"]);
                total_packs_count += int(cigarette["count"]);
            print ("You have smoked " + str(total_packs_count * 20) + " cigarettes, which contained total of " + str(total_nicotine) + " milligrams of nicotine and spent " + str(total_money) + " AMD on that.");
        elif text == "3":
            smoked_packs = readData();
            price = float (input ("    Input you cigarette price in drams "));
            nicotine = float (input ("    Input you cigarette nicotine in milligrams "));
            smoked_packs.append({
                    "price": price,
                    "nicotine": nicotine,
                    "count": 0
                });
            cigarette = {
                "smoked_packs" : smoked_packs
            };
            file = open("data.json", "w");
            file.write(json.dumps(cigarette));
            file.close();
        elif text == "4":
            answer = input("If you want to input paremeters of the cigarette you are smoking type 'add', otherwhise the program will close itself.");
            cigarette = {
                "smoked_packs" : []
            };
            file = open("data.json", "w");
            file.write(json.dumps(cigarette));
            file.close();
            if answer != "add":
                break;
            price = float (input ("    Input you cigarette price in drams "));
            nicotine = float (input ("    Input you cigarette nicotine in milligrams "));
            cigarette = {
                            "smoked_packs" : [ {
                                                    "price": price,
                                                    "nicotine": nicotine,
                                                    "count": 0
                                                } 
                                             ]
                        };
        elif text == "5":
            exit()
        else:
            print "Wrong input please enter 1, 2, 3 or 4"
            file = open("data.json", "w");
            file.write(json.dumps(cigarette));
            file.close();
main()