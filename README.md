# CS50 Project: Character Skill Word Counter

## About the Project:
This program efficiently counts the no. of words based on each character's skill, before ranking them in descending order.

Data for the above is stored in a .csv to effectively store large amounts of info.
Each character has their own set of categories with one value of each, (Class, Rarity and Position and Year), allowing the user to filter said characters through their sub-categories, and/or also learn the individual word counts for the latter.
At the beginning, you may filter characters through said categories, or simply display all data.

## Requirements
**Pandas library**: Handling of .csv

## Usage

### Getting Started
*Note: When prompted to, you will constantly be asked to provide correct input, so if it's invalid, you will be able to re-input such without needing to re-run the program.*

In the beginning, select between three options by their respective number:
* `1`: Count words from all characters, filtered by categories (Class/Rarity/Position/Year) via input later
* `2`: Count words from all characters, ignoring categorical filters
* `3`: End program

Should `2` be sent, word counts from all characters and categories will immediately be provided and the program will end.

### Category Filtering
Should `1` be sent, you will have the option to select between the four categories to filter with.

* Only characters that are part of the given categories, followed by their subsequent sub-categories will appear. For example, with input as `Rarity` followed by `Epic`, only characters that fall under the `Epic` sub-category will appear in our final result.

* However, should two categories be present, for example, with `Rarity` as `Epic` and `Year` by `2021`, only characters that are `Epic` **and** `2021` will appear. Think of it as `if rarity == "Epic" and year == 2021`.

It'll take too long to specify every possible interaction, so **think of it as playing around with column filters in Excel.**. Alternatively, jump to the "How category filtering works" section for a more in-depth explanation.

For quick reference, you can choose between:

* `Class`
* `Rarity`
* `Position`
* `Year`

Input Notes:
* A space between each must be sent to specify multiple.
* Inputs are not case-sensitive, so `Rarity` or `rarity` will work fine.
* Unintentional duplicates (`Rarity Rarity`) will be auto-removed for you.

So, if you just want to filter characters by *Rarity*, specify:
```
Rarity
```

If you want to filter characters by *Rarity* and *Year*, specify:
```
Rarity Year
```

Only in here, to return to the beginning, specify *any* incorrect value.

### Sub-category filtering
After specifying the categories, specify their respective sub-categories to be filtered through. You will also be provided a list of the relevant sub-categories per category for easy reference.

For quick reference, a list of sub-categories to pick from (ignore commas):

* Class - `Ambush, Bomber, Charge, Defense, Healing, Magic, Ranged, Support`
* Rarity - `Epic, Ancient, Legendary, Super_Epic, Special, Beast, Awakened`
* Position - `Front, Middle, Rear`
* Year - `2024, 2023, 2022, 2021`

So, if you sent Rarity from above, you will be provided `Epic, Ancient, Legendary, Super_Epic, Special, Beast, Awakened` to choose from.

One category will be inputted at a time, so if you wrote *Rarity Year* above, you will first send the sub-categories for the Rarity, then for Year. **Attempting to send both of them at the same time will cause an error.**

Input Notes written in the *Category Filtering* section will also continue here.

With *Rarity* currently targetted from *Rarity Year* or just *Rarity*, to filter through the Epic Rarity, specify:

```
Epic
```

Then, with *Year* currently targetted from *Rarity Year*, to filter through the year 2021, specify:

```
2021
```

### How category filtering works

Category filtering breaks down the data table through the specified categories, **one at a time**, to filter with.

Here, we have a hypothetical data table (rankings are not taken into account, and the full dataset is not used to keep our example simple):

| Name  |Class|Position|Rarity|Year|
| ------------- | ------------- | ------------- | ------------- | ------------- |
|Snow Sugar	|Magic	|Middle	|Epic	|2021|
|Vampire	|Ambush	|Rear	|Epic	|2021|
|Tiger Lily	|Ranged	|Rear	|Epic	|2021|
|Werewolf	|Charge	|Front	|Epic	|2021|
|Mint Choco	|Support	|Rear	|Epic	|2021|
|Herb	|Healing	|Rear	|Epic	|2021|
|Dark Choco	|Charge	|Front	|Epic	|2021|
|Sparkling	|Healing	|Rear	|Epic	|2021|
|Chili Pepper	|Ambush	|Middle	|Epic	|2021|
|Pomegranate	|Support	|Middle	|Epic	|2021|
|Purple Yam	|Charge	|Front	|Epic	|2021
|Milk	|Defense	|Front	|Epic	|2021
|Poison Mushroom	|Bomber	|Middle	|Epic	|2021|
|Licorice	|Magic	|Middle	|Epic	|2021
|Madeline	|Defense	|Front	|Epic	|2021|
|Espresso	|Magic	|Middle	|Epic	|2021|
|Rye	|Ranged	|Rear	|Epic	|2021|
|Latte	|Magic	|Middle	|Epic	|2021|
|Black Pearl|Ambush|Middle|Legendary|2022|
|Moonlight|Magic|Middle|Legendary|2023|

Let's say we've inputted *Class* and *Position* **in that exact order**, to filter with as categories.

In *Class*, we input *Magic*, *Healing*, *Ranged* and *Ambush* as its subcategories. There order here will not matter.

As a result, we will get:

As shown below, we only get characters under the 4 mentioned subclasses.

| Name  |Class|Position|Rarity|Year|
| ------------- | ------------- | ------------- | ------------- | ------------- |
|Snow Sugar	|Magic	|Middle	|Epic	|2021|
|Vampire	|Ambush	|Rear	|Epic	|2021|
|Tiger Lily	|Ranged	|Rear	|Epic	|2021|
|Herb	|Healing	|Rear	|Epic	|2021|
|Sparkling	|Healing	|Rear	|Epic	|2021|
|Chili Pepper	|Ambush	|Middle	|Epic	|2021|
|Licorice	|Magic	|Middle	|Epic	|2021
|Espresso	|Magic	|Middle	|Epic	|2021|
|Rye	|Ranged	|Rear	|Epic	|2021|
|Latte	|Magic	|Middle	|Epic	|2021|
|Black Pearl|Ambush|Middle|Legendary|2022|
|Moonlight|Magic|Middle|Legendary|2023|

We move onto *Position*, being *Rear*.

As shown below, nothing but *Rear* is kept.

| Name  |Class|Position|Rarity|Year|
| ------------- | ------------- | ------------- | ------------- | ------------- |
|Vampire	|Ambush	|Rear	|Epic	|2021|
|Tiger Lily	|Ranged	|Rear	|Epic	|2021|
|Herb	|Healing	|Rear	|Epic	|2021|
|Sparkling	|Healing	|Rear	|Epic	|2021|
|Rye	|Ranged	|Rear	|Epic	|2021|

As shown in the above example, this program uses **the specified categories' order** to filter data with, one at a time.

### Results

There will be three parts of the results: *General Stats*, *Bonus Stats* and *Summary*.

**General Stats**: Display all (filtered, if applicable) characters by name, amount of words, and descending ranking by said amount.

Example:

| Character Stats  |
| ------------- |
| Burning Spice: 265 words, #1 |
| Mystic Flour: 246 words: #2 |
| Golden Cheese: 199 words: #3 |

etc.

**Bonus Stats**: Display all categories followed by their respective (filtered, if applicable) subclasses with the above format.

Note: All categories will appear, regardless if a subclass filter was applied or not.

Example:

| Class Stats  |
| ------------- |
| Charge: 1844 words, #1  |
| Support: 1723 words, #2  |
| Defense: 1425 words, #3  |

| Position Stats  |
| ------------- |
| Front: 3628 words, #1 |
| Middle: 3573 words, #2 |
| Rear: 2870 words, #3 |

| Rarity Stats |
| ------------- |
| Epic: 6621 words, #1 |
| Super_Epic: 1028 words, #2 |
| Legendary: 775 words, #3 |

| Year Stats |
| ------------- |
| 2024: 3185 words, #1 |
| 2023: 2927 words, #2 |

etc.

**Summary**: Just displays the total amount of words counted from all characters.





