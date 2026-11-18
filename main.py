
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from parking_hr import ParkingHR, save_json_hr, load_json_hr

app = {
    "title": "Parkoló HR",
    "width": 800,
    "height": 680,
    "file": "parkolo_hr.json"
}

root = tk.Tk()
root.title(app["title"])
root.geometry(f"{app['width']}x{app['height']}")
root.resizable(False, False)
root.configure(bg="#eeeeee")

style = ttk.Style()
style.theme_use("clam")

parking = ParkingHR(12)

tk.Label(root, text="Parkoló HR", font=("Arial", 20, "bold"),
         bg="#eeeeee").pack(pady=12)

status_label = tk.Label(root, font=("Arial", 12), bg="#eeeeee")
status_label.pack(pady=5)

canvas = tk.Canvas(root, width=720, height=320, bg="#dddddd",
                   highlightthickness=0)
canvas.pack(pady=10)

tk.Label(root, text="Zöld: szabad     Piros: foglalt",
         bg="#eeeeee").pack()

controls = tk.Frame(root, bg="#eeeeee")
controls.pack(pady=12)

tk.Label(controls, text="Rendszám:", bg="#eeeeee").pack(
    side="left", padx=5
)

plate_entry = ttk.Entry(controls, width=18)
plate_entry.pack(side="left", padx=5)

buttons = tk.Frame(root, bg="#eeeeee")
buttons.pack(pady=5)

log_frame = tk.Frame(root, bg="#eeeeee")
log_frame.pack(fill="both", expand=True, padx=30, pady=10)

tk.Label(log_frame, text="Eseménynapló", bg="#eeeeee",
         font=("Arial", 11, "bold")).pack(anchor="w")

log_list = tk.Listbox(log_frame, height=6)
log_list.pack(fill="both", expand=True, pady=5)


def refresh_hr():
    canvas.delete("all")

    for i, plate in enumerate(parking.spaces):
        row = i // 4
        col = i % 4

        x1 = 25 + col * 175
        y1 = 20 + row * 100
        x2 = x1 + 145
        y2 = y1 + 80

        color = "#90ee90" if plate is None else "#ff9999"

        canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline="#555555",
            width=2,
            tags=f"space_{i}"
        )

        canvas.create_text(
            (x1 + x2) // 2,
            y1 + 25,
            text=f"{i + 1}. hely",
            font=("Arial", 12, "bold"),
            tags=f"space_{i}"
        )

        canvas.create_text(
            (x1 + x2) // 2,
            y1 + 52,
            text=plate if plate else "SZABAD",
            font=("Arial", 11),
            tags=f"space_{i}"
        )

    free = parking.free_count_hr()
    status_label.config(
        text=f"Szabad helyek: {free}     Foglalt helyek: {parking.capacity - free}"
    )


def add_log_hr(message):
    log_list.insert(0, message)


def park_car():
    success, message = parking.park_hr(plate_entry.get())

    if success:
        add_log_hr(message)
        plate_entry.delete(0, tk.END)
        refresh_hr()
    else:
        messagebox.showwarning("Figyelmeztetés", message)


def leave_car():
    success, message = parking.leave_hr(plate_entry.get())

    if success:
        add_log_hr(message)
        plate_entry.delete(0, tk.END)
        refresh_hr()
    else:
        messagebox.showwarning("Figyelmeztetés", message)


def save():
    try:
        save_json_hr(app["file"], {"spaces": parking.spaces})
        add_log_hr("Parkolóállapot mentve.")
    except OSError:
        messagebox.showerror("Hiba", "A mentés nem sikerült!")


def save_as():
    path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON-fájl", "*.json")]
    )

    if path:
        app["file"] = path
        save()


def load():
    path = filedialog.askopenfilename(
        filetypes=[("JSON-fájl", "*.json")]
    )

    if not path:
        return

    try:
        data = load_json_hr(path)
    except (OSError, UnicodeError):
        data = None

    if not isinstance(data, dict):
        messagebox.showerror("Hiba", "Nem sikerült betölteni a fájlt!")
        return

    spaces = data.get("spaces")

    if not isinstance(spaces, list) or len(spaces) != parking.capacity:
        messagebox.showerror("Hiba", "Érvénytelen parkolóadatok!")
        return

    plates = [plate for plate in spaces if plate is not None]

    if any(not isinstance(plate, str) or not plate.strip() for plate in plates):
        messagebox.showerror("Hiba", "Érvénytelen parkolóadatok!")
        return

    if len(plates) != len(set(plates)):
        messagebox.showerror("Hiba", "Ismétlődő rendszámok!")
        return

    parking.spaces = spaces.copy()
    app["file"] = path
    refresh_hr()
    add_log_hr("Parkolóállapot betöltve.")


def clear_log():
    log_list.delete(0, tk.END)


def select_space(event):
    items = canvas.find_overlapping(event.x, event.y, event.x, event.y)

    for item in reversed(items):
        tags = canvas.gettags(item)

        for tag in tags:
            if tag.startswith("space_"):
                index = int(tag.split("_")[1])
                plate = parking.spaces[index]

                if plate:
                    plate_entry.delete(0, tk.END)
                    plate_entry.insert(0, plate)
                    add_log_hr(f"{index + 1}. hely kiválasztva: {plate}")
                else:
                    add_log_hr(f"{index + 1}. hely szabad.")
                return


ttk.Button(buttons, text="Beállás", command=park_car).pack(
    side="left", padx=4
)
ttk.Button(buttons, text="Távozás", command=leave_car).pack(
    side="left", padx=4
)
ttk.Button(buttons, text="Mentés", command=save).pack(
    side="left", padx=4
)
ttk.Button(buttons, text="Mentés másként", command=save_as).pack(
    side="left", padx=4
)
ttk.Button(buttons, text="Megnyitás", command=load).pack(
    side="left", padx=4
)
ttk.Button(buttons, text="Napló törlése", command=clear_log).pack(
    side="left", padx=4
)
ttk.Button(buttons, text="Kilépés", command=root.destroy).pack(
    side="left", padx=4
)

plate_entry.bind("<Return>", lambda event: park_car())
canvas.bind("<Button-1>", select_space)

refresh_hr()
root.mainloop()
