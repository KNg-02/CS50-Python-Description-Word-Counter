def main():
    #Import pandas module
    import pandas as pd # type: ignore

    #Import dataframe
    DF = pd.read_csv('cookie1.csv', encoding='latin-1')

    #Convert year to string
    DF['year'] = DF['year'].map(str)

    #At the very start of the main(), ask the user for input, being 1 or 2 (just be a string)
    #1) Count all words, filtering by Rarity/Type/Position/Year.
    #calls counter_1().

    #2) Count all words without limitations.
    #calls counter_2().

    #This must be in a while True loop, to force the user to send some correct input.
    while True:
        user_choice = input(
        "Welcome! Select an option!\n" \
        "1) Count all words, filtering by Rarity/Class/Position/Year\n" \
        "2) Count all words without limitations\n" \
        "3) Quit\n").strip()
        if user_choice == "1":
            choice_maker = input(
                "Specify the categories you want. Rarity, Class, Position, Year.\n" \
                "Separate each option via a space. So, if you want Rarity and Position, do 'Rarity Position'.\n" \
                "Alternatively, type any other value to go back. \n")
            #Call the next function if choice_maker's value is valid.
            #Split by space first, then and lowercase each value with the listvia map()
            choice_maker_space_split = choice_maker.split()
            lowercased = list(map(str.lower, choice_maker_space_split))
            #print(lowercased)

            #Remove all duplicate items
            #print("dupe removal here")
            selected_data = list(dict.fromkeys(lowercased))
            #print(selected_data)

            #Check if each item within the lowercased list exists in the original csv's headers
            #Grab all headers from column index 2 and beyond
            column_names = DF.columns[2:].to_list()
            lowercase_check = [True if word in column_names else False for word in selected_data]
            #print(lowercase_check)

            #Make sure if there's no False in the lowercase check. Trigger function if so
            #If there is, go back to start
            if False not in lowercase_check:
                #print("Function should trigger here")
                data_list = []
                #Write a for loop here to trigger the function multiple times.
                for item_category in selected_data:
                    #item_category can be Rarity/Type/Position/Year individually.
                    #This function call could return ["Ancient", "Legendary"] and ["2021", "2022"]
                    data_list.append(counter_1_grab_values(item_category, DF))
                #data_list stores [["Ancient", "Legendary"],["2021", "2022"]]
                #print(data_list)

                #Now that we have data_list,
                #create a new dataframe that FITLERS BY specified values.
                #You will use
                #selected_data = ["Rarity", "Year"]
                #data_list = [["Ancient", "Legendary"], ["2021", "2022"]]
                print(" ")
                #print(selected_data)
                #print(data_list)
                #call the dataframe filter
                filtered_dataframe = counter_DF_filter(selected_data, data_list, DF)
                #print("Function: filtered_dataframe Hello")
                #print(filtered_dataframe)
                main_2(filtered_dataframe)
                break
            else:
                print("Try again")
        elif user_choice == "2":
            main_2(DF)
            break
        elif user_choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Input!")

def main_2(dataframe_):
        #Now that we've got the data, count the skill length.
        #Use filtered_dataframe, and pass the word_counter(filtered_dataframe)
        #print("Function: length_dataframe Hello")
        length_dataframe = word_counter(dataframe_)
        #print(length_dataframe)

        #With our new data, reorder the length in descending order.
        #Use length_descending().
        #print("New dataset!")
        reordered_dataframe = length_descending(length_dataframe)
        #print("Function: reordered_dataframe Hello")
        #print(reordered_dataframe)

        #From there, prepare to count words!
        word_counter_result = word_counting_normal(reordered_dataframe)

        #Write for loop here....
        #print(word_counter_result[0])
        print("----- Character Stats -----")
        for item in word_counter_result:
            print(item)

        #What if we went even more specific?
        #Using our reordered_dataframe, what if we wanted to find out the raw stats of:
        #1) The word count per class
        #2) The word count per position
        #3) The word count per rarity
        #4) The word count per year
        class_count = word_counting_specific(reordered_dataframe)
        #print(class_count)
        #print(class_count["2023"])
        print("\n--- [Bonus Stats] ---")
        print("--- Class Stats ---")
        class_list = ["Ambush", "Bomber", "Charge", "Defense", "Healing", "Magic", "Ranged", "Support"]
        list_a = {}
        list_b = {}
        list_c = {}
        list_d = {}
        #for key, value in class_count.items():
            #print(f"{key}: {value} words")
        #Call in a function here
        first_list = list_stat_counter(class_list, class_count, list_a)
        #print(first_list)
        key_value_count(first_list)

        print("\n--- Position Stats ---")
        position_list = ["Front", "Middle", "Rear"]
        second_list = list_stat_counter(position_list, class_count, list_b)
        #print(second_list)
        key_value_count(second_list)

        print("\n--- Rarity Stats ---")
        rarity_list = ["Ancient", "Awakened", "Beast", "Epic", "Legendary", "Special", "Super_Epic"]
        third_list = list_stat_counter(rarity_list, class_count, list_c)
        #print(third_list)
        key_value_count(third_list)

        print("\n--- Year Stats ---")
        year_list = ["2021", "2022", "2023", "2024"]
        fourth_list = list_stat_counter(year_list, class_count, list_d)
        #print(fourth_list)
        key_value_count(fourth_list)

        #Print the total no. of words from the reordered dataframe.
        print(f"\n--- Summary ---\nTotal no. of words: {reordered_dataframe['length'].sum()}")

def counter_1_grab_values(selected_data, DF):
    #Make sure to return a list
    check_for_confirm = []
    while True:
        #Ask for input
        unique_ref = DF[selected_data].unique()
        print(f"Possible sub-categories:")
        print(*unique_ref, sep=", ")
        desired_input = input(f"Input desired {selected_data.title()} sub-category, separated by a space for more\n").strip()
        #Split by space first, then and lowercase each value with the list via map()
        desired_input_split = desired_input.split()
        uppercased = list(map(str.title, desired_input_split))
        #print(uppercased)

        #Check if said item really exists in the given dictionary.
        #If yes, append true. If no, append False, both of which to a given list.
        #If there's a False,
        for item in uppercased:
            #print(item)
            if item in DF[selected_data].values:
                check_for_confirm.append("True")
            else:
                print(f"{item} doesn't exist")
                check_for_confirm.append("False")

            #print(check_for_confirm)
        if "False" in check_for_confirm:
            print("Task failed")
        else:
            return uppercased
        #Clear the list to prevent False values from being stuck
        check_for_confirm = []

def counter_DF_filter(selected_data, data_list, DF):
    #Don't overwrite the original dataframe, with DF_modified
    #create a new dataframe that FITLERS BY specified values.
    df_modified = DF
    #print("IN COUNTER!!!!")
    #print(selected_data) #This can be the rarity
    #print(data_list)

    if len(selected_data) == 1:
    #Flatten the single list, [["Ancient", "Legendary"]]
    #since .isin() doesn't work with lists in lists, []
        #print("YOU ARE #1")
        flat_list = []
        for xs in data_list:
            for x in xs:
                flat_list.append(x)
        #Based on the first value, grab the values from the flat list
        xl = df_modified.loc[df_modified[selected_data[0]].isin(flat_list)].copy()
        xl = xl.reset_index(drop=True)
        return xl
    #However, if the length of the list is at least 2, do this.
    elif len(selected_data) > 1:
        #print("YOU ARE AT #2")
        number = 0
        #Grab data_list by index via the number variable.
        for item in selected_data:
            #FIRST ITERATION.
            if number == 0:
                xl = df_modified.loc[df_modified[item].isin(data_list[number])].copy()
                number += 1
            #SECOND ITERATION AND BEYOND, WE WANT TO WORK WITH THE NEW FILE, XL
            elif number > 0:
                xl = xl.loc[xl[item].isin(data_list[number])].copy()
                number += 1
        xl = xl.reset_index(drop=True)
        return xl

def word_counter(filtered_dataframe):
    #Make a copy of the above dataframe
    word_dataframe = filtered_dataframe.copy()

    #Split words by spacing
    #1) Create a new column called "lengths"
    #2) Delete the column called "find_words", and "skill" since it's redundant
    word_dataframe['find_words'] = word_dataframe['skill'].str.split(' ')
    word_dataframe['length']  = word_dataframe['find_words'].apply(len)
    #word_dataframe = word_dataframe.drop(['find_words'], axis=1)

    #Reset the index for easier reading, and delete its column
    #word_dataframe = word_dataframe.reset_index()
    #word_dataframe = word_dataframe.drop(columns=['skill', 'find_words', 'index'])
    word_dataframe = word_dataframe.drop(columns=['skill', 'find_words'])
    return word_dataframe

def length_descending(length_dataframe):
    #Make a copy of the above dataframe
    descending_dataframe = length_dataframe.copy()
    descending_dataframe = descending_dataframe.sort_values(['length'], ascending=[False])
    descending_dataframe = descending_dataframe.reset_index(drop=True)
    return descending_dataframe

def word_counting_normal(reordered_dataframe):
    #Use for loop.
    #Create a list, then loop through it later. Get something to return
    word_counting_normal_list = []
    rank_no = 1
    for i in range(0, len(reordered_dataframe)):
        #print(reordered_dataframe.iloc[i]['name'], reordered_dataframe.iloc[i]['c2'])
        if i == 0:
            word_counting_normal_list.append(
                f"{reordered_dataframe.iloc[i]['name']}: {reordered_dataframe.iloc[i]['length']} words, #{rank_no}")
        elif i > 0:
            #If the previous dataframe's word count is the same as the previous, don't add rank no by 1!
            if reordered_dataframe.iloc[i]['length'] == reordered_dataframe.iloc[i - 1]['length']:
                pass
                #word_counting_normal_list.append(
                #f"{reordered_dataframe.iloc[i]['name']} has a total of {reordered_dataframe.iloc[i]['length']} words, and is at #{rank_no}")
            else:
                rank_no += 1
            word_counting_normal_list.append(f"{reordered_dataframe.iloc[i]['name']}: {reordered_dataframe.iloc[i]['length']} words, #{rank_no}")
        #print(rank_no)

    return word_counting_normal_list

def word_counting_specific(reordered_dataframe):
    categories = ["class", "position", "rarity", "year"]
    class_dict = {}
    for item in categories:
        loop_list = reordered_dataframe[item].unique()
        for item_2 in loop_list:
            class_dict[item_2] = reordered_dataframe.loc[reordered_dataframe[item] == item_2, 'length'].sum()

    #Convert every value to string to prevent int64 display bugs
    for keys in class_dict:
        class_dict[keys] = str(class_dict[keys])
    return class_dict

def list_stat_counter(class_list, class_count, list_stat_dictionary):
        for key, value in class_count.items():
            if key in class_list:
                list_stat_dictionary[key] = int(value)
        asc = {k: v for k, v in sorted(list_stat_dictionary.items(), key=lambda item: item[1], reverse=True)}
        return asc

def key_value_count(last_list):
    counter = 1
    for key, value in last_list.items():
        print(f"{key}: {value} words, #{counter}")
        counter += 1

if __name__ == "__main__":
    main()
