```python
diary = [
    {
        "date": "2026-10-04",
        "place": "Варшава",
        "description": "Я почав вести щоденник мандрівника."
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


add_entry(
    diary,
    "2026-10-05",
    "Краків",
    "Я відвідав центр міста."
)

show_entries(diary)
```
