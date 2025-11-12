import pandas as pd

class Timetable:
    def __init__(self, file_path: str):
        # Load timetable into a DataFrame
        self.df = pd.read_csv(file_path)
        self.df.columns = self.df.columns.str.strip().str.lower()  # normalize column names

    def get_faculty_schedule(self, faculty_name: str):
        """Return the schedule for a given faculty."""
        result = self.df[self.df['username'].str.contains(faculty_name, case=False, na=False)]
        return result.sort_values(by=['day', 'time'])

    def get_subject_teachers(self, subject_name: str):
        """Return all teachers for a given subject/course."""
        result = self.df[self.df['course'].str.contains(subject_name, case=False, na=False)]
        return result[['course', 'username', 'day', 'time', 'venue', 'division']]

    def find_free_slots(self, faculty_name: str = None, division: str = None):
        """Find available free slots for a faculty or division."""
        all_slots = [
            "09:30 - 10:30", "10:45 - 11:45", "12:00 - 13:00",
            "13:30 - 14:30", "14:30 - 15:30", "15:30 - 17:30"
        ]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        free_slots = []
        for day in days:
            for slot in all_slots:
                query = (self.df['day'].str.lower() == day.lower()) & (self.df['time'] == slot)
                if faculty_name:
                    query &= self.df['username'].str.contains(faculty_name, case=False, na=False)
                if division:
                    query &= self.df['division'].str.contains(division, case=False, na=False)
                if self.df[query].empty:
                    free_slots.append({"day": day, "time": slot})
        return pd.DataFrame(free_slots)


# Optional: Test usage when running directly
if __name__ == "__main__":
    timetable = Timetable("timetable.csv")

    print("--- Faculty schedule (sunitakulkarni) ---")
    print(timetable.get_faculty_schedule("sunitakulkarni"))

    print("\n--- Teachers for 'Data Analytics' ---")
    print(timetable.get_subject_teachers("Data Analytics"))

    print("\n--- Free slots for faculty sunitakulkarni ---")
    print(timetable.find_free_slots(faculty_name="sunitakulkarni"))
