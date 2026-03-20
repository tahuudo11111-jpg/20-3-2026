import tkinter as tk
from tkinter import messagebox

def nhap_he_so(chuoi):
    try:
        return list(map(float, chuoi.split()))
    except:
        return None

def nhan_da_thuc(a, b):
    n = len(a)
    m = len(b)
    c = [0]*(n+m-1)
    for i in range(n):
        for j in range(m):
            c[i+j] += a[i]*b[j]
    return c

def horner(a, x):
    result = a[0]
    for i in range(1, len(a)):
        result = result*x + a[i]
    return result

def hien_thi(a):
    deg = len(a) - 1
    s = ""
    for i in range(len(a)):
        if a[i] != 0:
            mu = deg - i
            if mu == 0:
                s += f"{a[i]:+}"
            elif mu == 1:
                s += f"{a[i]:+}x"
            else:
                s += f"{a[i]:+}x^{mu}"
    return s.lstrip('+')

def tinh():
    a = nhap_he_so(entry_p1.get())
    b = nhap_he_so(entry_p2.get())

    if a is None or b is None:
        messagebox.showerror("Lỗi", "Nhập hệ số không hợp lệ!")
        return

    try:
        x = float(entry_x.get())
    except:
        messagebox.showerror("Lỗi", "Giá trị x không hợp lệ!")
        return

    c = nhan_da_thuc(a, b)
    val = horner(c, x)

    result_text.set(
        f"p1(x) = {hien_thi(a)}\n"
        f"p2(x) = {hien_thi(b)}\n"
        f"p(x) = {hien_thi(c)}\n"
        f"p({x}) = {val}"
    )

# GUI
root = tk.Tk()
root.title("Nhân đa thức")

tk.Label(root, text="Hệ số p1 (cách nhau bởi dấu cách):").pack()
entry_p1 = tk.Entry(root, width=50)
entry_p1.pack()

tk.Label(root, text="Hệ số p2:").pack()
entry_p2 = tk.Entry(root, width=50)
entry_p2.pack()

tk.Label(root, text="Giá trị x:").pack()
entry_x = tk.Entry(root)
entry_x.pack()

tk.Button(root, text="Tính toán", command=tinh).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left").pack()

root.mainloop()
