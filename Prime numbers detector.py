import tkinter as tk
from tkinter import messagebox

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def set_prime():
    A = int(entry1.get())
    B = int(entry2.get())
    primes = [i for i in range(A, B + 1) if is_prime(i)]
    result = f"Ilość liczb pierwszych wynosi: {len(primes)}\nTe liczby pierwsze to:\n{', '.join(map(str, primes))}"
    messagebox.showinfo("Wynik", result)

root = tk.Tk()
root.title("Liczydło liczb pierwszych")

label1 = tk.Label(root, text="Podaj zakres dolny:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Podaj zakres górny:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(root, text="Znajdź liczby pierwsze", command=set_prime)
button.grid(row=2, columnspan=2, padx=5, pady=5)

# Dodanie podpisu
signature_label = tk.Label(root, text="Jan Ślusarek", font=("Arial", 10, "italic"))
signature_label.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()