import tkinter as tk

def my_strlen(s):
    count = 0
    for _ in s:
        count += 1
    return count

def my_strcpy(s1, s2):
    return s2

def my_strcat(s1, s2):
    return s1 + s2

def do_strlen():
    s = entry1.get()
    result.set(f"Độ dài: {my_strlen(s)}")

def do_strcpy():
    s1 = entry1.get()
    s2 = entry2.get()
    kq = my_strcpy(s1, s2)
    result.set(f"KQ strcpy: {kq} ({my_strlen(kq)})")

def do_strcat():
    s1 = entry1.get()
    s2 = entry2.get()
    kq = my_strcat(s1, s2)
    result.set(f"KQ strcat: {kq} ({my_strlen(kq)})")

# GUI
root = tk.Tk()
root.title("Mô phỏng string.h")
root.geometry("400x300")

tk.Label(root, text="Chuỗi 1:").pack()
entry1 = tk.Entry(root, width=40)
entry1.pack()

tk.Label(root, text="Chuỗi 2:").pack()
entry2 = tk.Entry(root, width=40)
entry2.pack()

tk.Button(root, text="strlen", command=do_strlen).pack(pady=5)
tk.Button(root, text="strcpy", command=do_strcpy).pack(pady=5)
tk.Button(root, text="strcat", command=do_strcat).pack(pady=5)

result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").pack(pady=10)

root.mainloop()
