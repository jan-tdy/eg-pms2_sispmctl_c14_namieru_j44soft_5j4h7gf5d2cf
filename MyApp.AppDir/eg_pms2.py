import subprocess
import tkinter as tk

def zapni_zasuvku(cislo_zasuvky, stav_label):
    """Zapne zadanú zásuvku a aktualizuje stav."""
    try:
        subprocess.check_call(["sispmctl", "-o", str(cislo_zasuvky)])
        stav_label.set("ZAPNUTE")
        print(f"Zásuvka {cislo_zasuvky} bola zapnutá.")
    except subprocess.CalledProcessError as e:
        print(f"Chyba pri zapínaní zásuvky {cislo_zasuvky}: {e}")

def vypni_zasuvku(cislo_zasuvky, stav_label):
    """Vypne zadanú zásuvku a aktualizuje stav."""
    try:
        subprocess.check_call(["sispmctl", "-f", str(cislo_zasuvky)])
        stav_label.set("VYPNUTE")
        print(f"Zásuvka {cislo_zasuvky} bola vypnutá.")
    except subprocess.CalledProcessError as e:
        print(f"Chyba pri vypínaní zásuvky {cislo_zasuvky}: {e}")

def vytvor_gui():
    """Vytvorí grafické rozhranie s tlačidlami pre ovládanie zásuviek."""

    okno = tk.Tk()
    okno.title("j44soft: EG-PMS2 C14")

    # Odstránenie ikony
    # ikona = PhotoImage(file=ikon_path)
    # okno.iconphoto(False, ikona)

    nazvy_zasuviek = ["none", "AZ2000", "C14", "UNKNOWN"]
    stavy_zasuviek = []

    for i in range(1, 5):
        ramec_zasuvky = tk.Frame(okno)
        ramec_zasuvky.pack()

        nazov_label = tk.Label(ramec_zasuvky, text=nazvy_zasuviek[i-1])
        nazov_label.grid(row=0, column=0, padx=10, pady=5)

        stav_premenna = tk.StringVar(value="VYPNUTE-PREDVOLENE")
        stavy_zasuviek.append(stav_premenna)
        stav_label = tk.Label(ramec_zasuvky, textvariable=stav_premenna)
        stav_label.grid(row=0, column=1, padx=10, pady=5)

        zapni_tlacidlo = tk.Button(ramec_zasuvky, text="Zapnúť",
                                  command=lambda i=i, stav=stav_premenna: zapni_zasuvku(i, stav))
        zapni_tlacidlo.grid(row=0, column=2, padx=10, pady=5)

        vypni_tlacidlo = tk.Button(ramec_zasuvky, text="Vypnúť",
                                  command=lambda i=i, stav=stav_premenna: vypni_zasuvku(i, stav))
        vypni_tlacidlo.grid(row=0, column=3, padx=10, pady=5)

    okno.mainloop()

if __name__ == "__main__":
    vytvor_gui()
