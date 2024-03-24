import tkinter as tk


def create_gui(root):
    root.title("Simple GUI")
    root.geometry("500x500")

    hello_label = tk.Label(
        root, name="hello_label", text="Simple Python GUI", font=("Arial", 18)
    )
    hello_label.pack(pady=20)

    button = tk.Button(root, name="button", text="Click Me!", font=("Arial", 18))
    button.pack(padx=10, pady=10)

    return root


if __name__ == "__main__":
    root = tk.Tk()
    create_gui(root)
    root.mainloop()
