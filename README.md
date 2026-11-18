# Parkoló HR

**Hallgató neve:** Herman Richárd  
**Neptun-kód:** EO5J9V  


## A program bemutatása

A Parkoló HR egy Python nyelven készített grafikus parkolónyilvántartó alkalmazás. A program 12 parkolóhelyet kezel, amelyek állapotát színes téglalapokkal jeleníti meg.

A zöld parkolóhelyek szabadok, a piros parkolóhelyek foglaltak. A felhasználó rendszám megadásával járművet állíthat be a parkolóba, illetve távolíthat el onnan.

A program kijelzi a szabad és foglalt helyek számát, valamint eseménynaplót vezet a végrehajtott műveletekről. A parkoló aktuális állapota JSON-fájlba menthető és később visszatölthető.

## A program felépítése

- `main.py` – a grafikus felület és az eseménykezelés
- `parking_hr.py` – a saját modul, amely a parkoló működését és a fájlkezelést valósítja meg

A főablak változója `root`, a program beállításait az `app` szótár tartalmazza.

## Felhasznált modulok

### tkinter

A grafikus felület kialakításához és az események kezeléséhez használt modul.

Alkalmazott elemek és metódusok:

- `Tk()` – főablak létrehozása
- `Canvas()` – parkolótérkép megjelenítése
- `create_rectangle()` – parkolóhelyek kirajzolása
- `create_text()` – feliratok megjelenítése
- `bind()` – egér- és billentyűzetes események kezelése
- `delete()` – rajzelemek törlése és frissítése

A program a `ttk`, `filedialog` és `messagebox` elemeket is használja.

### json

A parkolóhelyek állapotának fájlba mentéséhez és visszatöltéséhez használt modul.

- `json.dump()` – adatok mentése JSON-formátumban
- `json.load()` – adatok betöltése JSON-fájlból

### parking_hr.py

Saját készítésű modul, amely tartalmazza a `ParkingHR` osztályt és a JSON-fájlkezelő függvényeket.

## Saját osztály

**ParkingHR**

A parkoló kapacitását és a parkolóhelyek foglaltságát kezeli.

Metódusai:

- `__init__()` – parkoló inicializálása
- `park_hr()` – jármű beállítása
- `leave_hr()` – jármű távozása
- `free_count_hr()` – szabad helyek megszámlálása

## Saját függvények

A `parking_hr.py` modulban:

- `save_json_hr()` – parkolóadatok mentése
- `load_json_hr()` – parkolóadatok betöltése

A `main.py` fájlban:

- `refresh_hr()` – grafikus megjelenítés frissítése
- `add_log_hr()` – eseménynapló bővítése
- `park_car()` – beállás kezelése
- `leave_car()` – távozás kezelése
- `save()` – mentés
- `save_as()` – mentés másként
- `load()` – megnyitás
- `clear_log()` – napló törlése
- `select_space()` – parkolóhely kiválasztása egérrel

## Eseménykezelés

A program gombnyomásokkal, egérkattintással és az Enter billentyűvel vezérelhető.

Foglalt parkolóhelyre kattintva a rendszám bekerül a beviteli mezőbe.

## A program futtatása

A program Python 3 környezetben futtatható, külön csomagok telepítése nélkül.

Indítás:

`python main.py`

## Fájlok

- `main.py`
- `parking_hr.py`
- `README.md`

A mentett parkolóállapotot a program JSON-formátumban tárolja.