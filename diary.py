```python
diary = [
    {
        "date": "2026-10-04",
        "place": "Варшава",
        "description": "Я почав вести щоденник мандрівника."
    },
    {
        "date": "2026-10-05",
        "place": "Краків",
        "description": "Я відвідав центр міста."
    },
    {
        "date": "2026-10-07",
        "place": "Одеса",
        "description": "Я прогулявся біля моря."
    }
]


def add_entry(diary, date, place, description):
    diary.append({
        "date": date,
        "place": place,
        "description": description
    })


def show_entries(diary):
    for entry in diary:
        print(f"{entry['date']} - {entry['place']}: {entry['description']}")


def entries_with_word(diary, word):
    for entry in diary:
        if word.lower() in entry["description"].lower():
            print(f"{entry['date']} - {entry['place']}: {entry['description']}")


def count_entries(diary):
    return len(diary)


add_entry(
    diary,
    "2026-10-08",
    "Львів",
    "Я відвідав історичний центр міста."
)

show_entries(diary)

print("\nЗаписи зі словом 'місто':")
entries_with_word(diary, "місто")

print(f"\nКількість записів: {count_entries(diary)}")
```
