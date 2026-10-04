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


add_entry(
    diary,
    "2026-10-06",
    "Львів",
    "Я прогулявся старою частиною міста."
)

show_entries(diary)

print("\nЗаписи зі словом 'місто':")
entries_with_word(diary, "місто")
```
