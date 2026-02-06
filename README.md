# 🎮 Slovní Fotbal – Interaktivní hra proti počítači

![Status](https://img.shields.io/badge/status-v1.0-brightgreen)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20|%20Linux%20|%20macOS-lightgrey)
![Jazyk](https://img.shields.io/badge/jazyk-Python-darkblue)
![Licence](https://img.shields.io/badge/licence-MIT-green)

---

## 🔗 GitHub Repositář

[https://github.com/artur-ver/slovni_fotbal](https://github.com/artur-ver/slovni_fotbal)

---

## 📖 O hře

**Slovní fotbal** je interaktivní hra příkazové řádky, kde hrajete proti počítači pojmenovanému **Eda**.

### Hlavní rysy:
- ✅ Interaktivní CLI interface
- ✅ Práce s češtinou (diakritika, "ch" jako jeden znak)
- ✅ Tvárenlivý zdroj slov (`.txt` a `.json` soubory)
- ✅ Žádné opakování slov
- ✅ Multiplatformní (Windows, Linux, macOS)
- ✅ Bez vnějších závislostí – čistě Python
- ✅ Jednoduchá instalace

---

## 🚀 Instalace a spuštění

### Požadavky
- **Python 3.8+** (s `python` nebo `python3` příkazem)
- Operační systém: Windows, Linux nebo macOS

### Krok 1: Kontrola Pythonu

Ověřete, zda máte Python nainstalován:

```bash
python --version
# nebo
python3 --version
```

Pokud Python nemáte, stáhněte jej z: **[python.org](https://www.python.org/downloads/)**

### Krok 2: Příprava složky se slovy

Vytvořte složku `vstupy` v adresáři projektu a vložte do ní soubory se slovy.

#### Podporované formáty:

**📄 Textový soubor (vstupy/slova.txt):**
```
akord
dama
ananas
sluch
chobot
kočka
```

**📋 JSON soubor (vstupy/slova.json):**
```json
{
  "kategorie1": ["akord", "dama", "ananas"],
  "kategorie2": ["sluch", "chobot", "kočka"]
}
```

nebo jednoduché pole:
```json
["akord", "dama", "ananas", "sluch"]
```

### Krok 3: Spuštění hry

**Windows (CMD/PowerShell):**
```bash
python main.py
```

**macOS / Linux:**
```bash
python3 main.py
```

---

## 🎯 Pravidla hry

1. **Počítač začíná** – Eda zvolí první slovo z vašeho slovníku
2. **Váš tah** – Musíte zadat slovo, které **začíná poslední písmeny předchozího slova**
3. **Zvláštní tratman: "CH"** – V češtině se "ch" počítá jako **jedno písmeno**
4. **Bez opakování** – Jakmile je slovo použito, nelze jej znovu
5. **Konec hry** – Pokud počítač nenalezne slovo, vyhráváte! 🎉
6. **Složitost** – Kdyžtak se můžete vzdát (`quit` nebo `im a loser`)

### Příklad partie:

```
Eda: CHOBOT (začíná s "ch", končí na "t")
↓
Váš tah: t → TABLO (začíná na "t", končí na "o")
↓
Eda: OSTROV (začíná na "o", končí na "v")
↓
Váš tah: v → VODA (začíná na "v", končí na "a")
↓
Eda: ASTRONAUT (začíná na "a", končí na "t")
...a tak dále
```

---

## 🔧 Technické detaily

### Normalizace slov

Program automaticky:
- Převádí na **malá písmena**
- Odstraňuje **háčky a čárky** (diakritiku)
- Ponechává pouze **písmena** (čísla a speciální znaky jsou ignorovány)
- Příklady:
  - `"Řeka"` → `"reka"`
  - `"CHOBOTNICE"` → `"chobotnice"`
  - `"Čaj123"` → `"caj"`

### Zpracování souborů

- 📄 `.txt` soubory: čte se řádek po řádku
- 📋 `.json` soubory: podporuje pole nebo slovník s poli
- ⚠️ Pokud soubor selhá, program upozorní, ale bude pokračovat
- Slova se **automaticky deduplikují** (jedno slovo se načte jen jednou)

### Struktura projektu

```
slovni-fotbal/
│
├── main.py                    # Hlavní soubor hry
├── README.md                  # Dokumentace (tento soubor)
│
└── vstupy/                    # Složka se slovníky (vytvoříte sami)
    ├── slova_jednoducha.txt
    ├── slova_pokrocila.json
    └── ... (další soubory)
```
---

## 📋 Důležité poznámky

✅ **Kódování souborů**
- Všechny `.txt` a `.json` soubory musí být v **UTF-8** kódování
- Windows: Uložte v Poznámkovém bloku s kódováním UTF-8 (Soubor → Uložit jako → Typ: UTF-8)

✅ **Umístění složky vstupy**
- Složka `vstupy` musí být **ve stejném adresáři** jako `main.py`
- Správně: `projekt/main.py` a `projekt/vstupy/slova.txt`
- Chybně: `projekt/vstupy/main.py`

✅ **Verze Pythonu**
- Python **3.8+** je povinný (pro type hints a f-strings)
- Starší verze nebudou fungovat

✅ **Bez vnějších knihoven**
- Hra používá pouze **vestavěné moduly** Pythonu
- Žádný `pip install` není potřeba

---

## ❓ Časté otázky (FAQ)

### ❌ ERROR: No words loaded in 'vstupy'

**Příčina:** Složka `vstupy` není vytvořena nebo neobsahuje soubory.

**Řešení:**
1. Vytvořte složku `vstupy` v adresáři projektu
2. Přidejte `.txt` nebo `.json` soubory se slovy
3. Spusťte hru znovu

```bash
# Příklad: vytvoření složky
mkdir vstupy
# Přidejte soubor: vstupy/slova.txt
```

### ❌ Invalid move: Must start with 'X'

**Příčina:** Slovo nezačíná na požadované písmeno.

**Řešení:** Počítač skončil na určitém písmenu – vaše slovo musí tímto **začínat**.

### ❌ Invalid move: Word already used!

**Příčina:** Toto slovo bylo již v hře použito.

**Řešení:** Zvolte jiné slovo ze slovníku.

### ❌ UnicodeDecodeError

**Příčina:** Soubor není v UTF-8 kódování.

**Řešení:** Znovu uložte soubor v UTF-8:
- VS Code: Spodní lišta → UTF-8
- Windows Poznámkový blok: Soubor → Uložit jako → Encoding: UTF-8

### ❓ Jak se počítají "CH"?

"CH" se v češtině počítá jako **jedno písmeno**.

Příklady:
- `CHOBOT` → poslední písmeno je **T** (CH + O + B + O + T)
- `CHOBOTNICE` → poslední písmeno je **E** (CH + O + B + O + T + N + I + C + E)
- `CHRUSTÁLEK` → poslední písmeno je **K** – a začíná na **CH**!

---

## 🎓 Příklady používání

### Přidání vlastního slovníku

**Soubor: vstupy/soupiska_zvirat.txt**
```
kůň
medvěd
čáp
pták
kočka
ryba
```

**Příkazový řádek:**
```bash
python main.py
```

Hra nyní bude používat tato zvířata!

### Pokročilý JSON slovník

**Soubor: vstupy/slovnik_pro_skoly.json**
```json
{
  "snadne": ["kůň", "pes", "kočka"],
  "stredne": ["astronaut", "čokolád", "elektromotor"],
  "tezkostredne": ["chobotnice", "jaguár", "kybernetika"],
  "slozenych_slov": ["automobil", "obrazovka", "zahradnictví"]
}
```

Hra načte **všechna slova** z JSON souboru bez ohledu na strukturu.

---

## 💪 Tipy pro zlepšení hry

1. **Větší slovník** – Přidejte více slov do `vstupy/` složky
2. **Slovníky po kategoriích** – Můžete mít `slova_zvířat.txt`, `slova_potravin.json` apod.
3. **Soutěž** – Hrát v týmech s úkolem překonat výkon počítače
4. **Časový limit** – Používejte externí stopky pro dodatečné drama

---

## 📄 Licence

Tento projekt je volně dostupný pro osobní i vzdělávací použití.

---

## 🤝 Přispívání

Máte nápad na vylepšení? Chybu jste našli? Dejte vědět!

**Kontroly kvality:**
- ✅ Hra musí fungovat v Pythonu 3.8+
- ✅ Kód musí korektně zpracovat češtinu
- ✅ Musí fungovat na Windows, Linux a macOS

---
