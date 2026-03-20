import tkinter as tk
from tkinter import filedialog, messagebox

def doc_file():
    file_path = filedialog.askopenfilename(
        title="Chọn file PERSON.DAT",
        filetypes=[("DAT files", "*.dat"), ("All files", "*.*")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        text.delete(1.0, tk.END)

        for line in lines:
            # Ví dụ: 1654:Jackie Chan,Hong Kong:7/22/54
            line = line.strip()
            if not line:
                continue

            try:
                code_part, rest = line.split(":", 1)
                name_part, rest2 = rest.split(",", 1)
                address_part, birthday = rest2.split(":")

                code = code_part.strip()
                name = name_part.strip()
                address = address_part.strip()
                birthday = birthday.strip()

                output = (
                    f"{name} [code: {code}]\n"
                    f"  Address : [{address}]\n"
                    f"  Birthday: [{birthday}]\n\n"
                )

                text.insert(tk.END, output)

            except:
                text.insert(tk.END, f"Lỗi dòng: {line}\n")

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


# GUI
root = tk.Tk()
root.title("Đọc file PERSON.DAT")
root.geometry("500x400")

btn = tk.Button(root, text="Chọn file PERSON.DAT", command=doc_file)
btn.pack(pady=10)

text = tk.Text(root)
text.pack(expand=True, fill="both")

root.mainloop()
