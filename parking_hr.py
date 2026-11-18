
import json


class ParkingHR:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.spaces = [None] * capacity

    def park_hr(self, plate):
        plate = plate.strip().upper()

        if not plate:
            return False, "Adj meg egy rendszámot!"

        if plate in self.spaces:
            return False, "Ez a jármű már a parkolóban van!"

        for i in range(self.capacity):
            if self.spaces[i] is None:
                self.spaces[i] = plate
                return True, f"{plate} beállt a(z) {i + 1}. helyre."

        return False, "A parkoló megtelt!"

    def leave_hr(self, plate):
        plate = plate.strip().upper()

        for i, car in enumerate(self.spaces):
            if car == plate:
                self.spaces[i] = None
                return True, f"{plate} távozott a(z) {i + 1}. helyről."

        return False, "A rendszám nem található!"

    def free_count_hr(self):
        return self.spaces.count(None)


def save_json_hr(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json_hr(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
