import json
class media:
    def __init__(self,title ,creator, year, days_burrowed):
        self.title=title
        self.creator=creator
        self.year=year
        self.days_burrowed=days_burrowed
    def __str__(self):
        return f"{self.title} by {self.creator} ({self.year}) - {self.days_burrowed} days burrowed"
    def estimate_completion(self):
        raise NotImplementedError 
class Book(media):
    def __init__(self,title, creator, year, days_burrowed, pages,pages_per_day):
        super().__init__(title, creator, year, days_burrowed)
        self.pages=pages
        self.pages_per_day=pages_per_day
    def estimate_completion(self):
        return self.pages/self.pages_per_day
class Course(media):
    def __init__(self, title,creator,year,duration,hours_per_day):
        super().__init__(title,creator,year,duration)
        self.duration=duration
        self.hours_per_day=hours_per_day
    def estimate_completion(self):
        return self.duration/self.hours_per_day
class Video(media):
    def __init__(self, title, creator, year, days_burrowed, total_minutes, minutes_per_day=60):
        super().__init__(title, creator, year, days_burrowed)
        self.total_minutes = total_minutes
        self.minutes_per_day = minutes_per_day                      

    def estimate_completion(self):
            return self.total_minutes / self.minutes_per_day
    
class LibrarySystem:
    def __init__(self):
        self.items = []  
    def status_report(self):
        for item in self.items:
            print(item.estimate_completion())
    def add_item(self,new):
        self.items.append(new)
    def show_items(self):
        sorted_items=sorted(self.items, key= lambda item:(type(item).__name__, item.estimate_completion()))
        return sorted_items
    def store_items(self):
        data = [vars(item) for item in self.items]
        with open("library.json", mode="w") as file:
            json.dump(data, file, indent=2)
    print("Items were successfully stored")
    def extract_info(self):
        with open("library.json", mode="r") as file:
            data=json.load(file)
        return data
    def load_items(self):
        with open("library.json", mode="r") as file:
            data_list=json.load(file)
            for data in data_list:
                if "pages" in data:
                    book=Book(data["title"],data["creator"],data["year"],data["days_burrowed"],data["pages"],data["pages_per_day"])
                    self.items.append(book)
                elif "duration" in data:
                    course=Course(data["title"],data["creator"],data["year"],data["duration"],data["hours_per_day"])
                    self.items.append(course)
                elif "total_minutes" in data:
                    video=Video(data["title"],data["creator"],data["year"],data["days_burrowed"],data["total_minutes"],data["minutes_per_day"])
                    self.items.append(video)

def test():
    library = LibrarySystem()

    b = Book("Deep Work", "Cal Newport", 2016, 0, 296, 20)
    c = Course("CS50", "Harvard", 2024, 100, 2)
    v = Video("Intro to ML", "3Blue1Brown", 2023, 0, 45, 20)

    library.add_item(b)
    library.add_item(c)
    library.add_item(v)

    print("--- status_report ---")
    library.status_report()

    print("--- show_items (sorted) ---")
    for item in library.show_items():
        print(item)

    print("--- saving ---")
    library.store_items()

    print("--- loading into a FRESH LibrarySystem ---")
    fresh_library = LibrarySystem()
    fresh_library.load_items()

    print("--- status_report after reload ---")
    fresh_library.status_report()

    print(f"\nItems before save: {len(library.items)}")
    print(f"Items after reload: {len(fresh_library.items)}")
    assert len(library.items) == len(fresh_library.items), "Item count mismatch after reload!"
    print("All good — counts match.")

test()



        