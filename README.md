# Parkoló HR

**Hallgató neve:** Herman Richárd  
**Neptun-kód:** EO5J9V  
**Monogram:** HR

## A program bemutatása

A Parkoló HR egy Python nyelven készített grafikus parkolónyilvántartó alkalmazás. A program 12 parkolóhelyet kezel, amelyek állapotát színes téglalapokkal jeleníti meg.

A zöld parkolóhelyek szabadok, a piros parkolóhelyek foglaltak. A felhasználó rendszám megadásával járművet állíthat be a parkolóba, illetve távolíthat el onnan.

A program kijelzi a szabad és foglalt helyek számát, valamint eseménynaplót vezet a végrehajtott műveletekről. A parkoló aktuális állapota JSON-fájlba menthető és később visszatölthető.

A JSON-előnézet funkció segítségével a parkolóhelyek aktuális adatai külön ablakban, JSON-formátumban is megtekinthetők.

## A program felépítése

A program két Python-fájlból áll:

- `main.py` – a grafikus felület és az eseménykezelés megvalósítása
- `parking_hr.py` – saját készítésű modul, amely a parkoló működését és a JSON-fájlkezelést valósítja meg

A főablak változója `root`, a program beállításait az `app` szótár tartalmazza.

## Felhasznált modulok

### Tanult modul - tkinter

A grafikus felület kialakításához és az események kezeléséhez használt modul.

Alkalmazott elemek és metódusok:

- `Tk()` – főablak létrehozása
- `Canvas()` – parkolótérkép megjelenítése
- `create_rectangle()` – parkolóhelyek kirajzolása
- `create_text()` – feliratok megjelenítése
- `bind()` – egér- és billentyűzetes események kezelése
- `delete()` – rajzelemek törlése és frissítése

A program a `ttk`, `filedialog` és `messagebox` elemeket is használja.

### Bemutatandó modul - json

A parkolóhelyek állapotának fájlba mentéséhez, visszatöltéséhez és megjelenítéséhez használt modul.

Alkalmazott függvények:

- `json.dump()` – adatok mentése JSON-formátumban
- `json.load()` – adatok betöltése JSON-fájlból
- `json.dumps()` – az aktuális parkolóadatok JSON-szöveggé alakítása az előnézeti ablak számára

### Saját modul - parking_hr.py

Saját készítésű modul, amely tartalmazza a `ParkingHR` osztályt és a JSON-fájlkezelő függvényeket.

## Saját osztály

### ParkingHR

A parkoló kapacitását és a parkolóhelyek foglaltságát kezeli.

Metódusai:

- `__init__()` – a parkoló inicializálása
- `park_hr()` – jármű beállítása
- `leave_hr()` – jármű távozása
- `free_count_hr()` – szabad parkolóhelyek megszámlálása

A parkoló 12 férőhellyel rendelkezik. A járművek rendszámát a program listában tárolja, a szabad helyeket `None` érték jelöli.

A program ellenőrzi, hogy a megadott rendszám szerepel-e már a parkolóban, és figyelmeztet, ha a parkoló megtelt.

## Saját függvények

### A parking_hr.py modulban

- `save_json_hr()` – parkolóadatok mentése JSON-fájlba
- `load_json_hr()` – parkolóadatok betöltése JSON-fájlból

### A main.py fájlban

- `refresh_hr()` – a grafikus megjelenítés és a foglaltsági adatok frissítése
- `add_log_hr()` – eseménynapló bővítése
- `park_car()` – jármű beállásának kezelése
- `leave_car()` – jármű távozásának kezelése
- `save()` – parkolóállapot mentése
- `save_as()` – parkolóállapot mentése másként
- `load()` – mentett parkolóállapot megnyitása
- `clear_log()` – eseménynapló törlése
- `json_preview()` – az aktuális parkolóadatok megjelenítése JSON-formátumban
- `select_space()` – parkolóhely kiválasztása egérrel

## Eseménykezelés

A program gombnyomásokkal, egérkattintással és az Enter billentyűvel vezérelhető.

A **Beállás** gombbal a megadott rendszámú jármű a következő szabad parkolóhelyre kerül. A **Távozás** gomb eltávolítja a járművet a parkolóból.

A parkolóhelyekre egérrel is rá lehet kattintani. Foglalt parkolóhely kiválasztásakor a hozzá tartozó rendszám bekerül a beviteli mezőbe.

A **Mentés** és **Mentés másként** gombokkal az aktuális parkolóállapot JSON-fájlba menthető, a **Megnyitás** gombbal pedig visszatölthető.

A **Napló törlése** gomb kiüríti az eseménynaplót.

A **JSON előnézet** gomb megnyomásával a parkoló aktuális állapota külön ablakban, JSON-formátumban tekinthető meg. Ehhez a program a `json.dumps()` függvényt használja.

A **Kilépés** gomb bezárja az alkalmazást.

## A program futtatása

A program Python 3 környezetben futtatható, külön csomagok telepítése nélkül, amennyiben a Tkinter rendelkezésre áll.

Indítás:

```bash
python main.py
```

## Fájlok

- `main.py` – főprogram
- `parking_hr.py` – saját modul
- `README.md` – a program dokumentációja
- `.gitignore` – a Git által figyelmen kívül hagyott fájlok meghatározása

A mentett parkolóállapotot a program JSON-formátumban tárolja.