# Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом. 
# Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции). 
# Ввод данных из файла с контролем правильности ввода. 
# Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами.
#  Для GUI и визуализации использовать библиотеку tkinter

# Вариант 5
# Объекты – договоры на аренду недвижимости
# Функции:
# сегментация по видам объектов недвижимости полного списка договоров 
# визуализация предыдущей функции в форме круговой диаграммы
# сегментация по менеджерам полного списка договоров 
# визуализация предыдущей функции в форме круговой диаграммы


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt

class RentalAgreement:
    def __init__(self, property_type, manager, rent_amount):
        self.property_type = property_type
        self.manager = manager
        self.rent_amount = rent_amount

class RentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер Договоров Аренды")
        self.agreements = []
        self.setup_gui()

    def setup_gui(self):
        ttk.Button(self.root, text="Загрузить договоры", command=self.load_agreements).pack(pady=5)
        ttk.Button(self.root, text="Сегментация по типу недвижимости", command=self.segment_by_property_type).pack(pady=5)
        ttk.Button(self.root, text="Сегментация по менеджерам", command=self.segment_by_manager).pack(pady=5)

        self.tree = ttk.Treeview(self.root, columns=("Тип недвижимости", "Менеджер", "Сумма аренды"), show="headings")
        self.tree.heading("Тип недвижимости", text="Тип недвижимости")
        self.tree.heading("Менеджер", text="Менеджер")
        self.tree.heading("Сумма аренды", text="Сумма аренды")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def load_agreements(self):
        file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, mode='r') as file:
                lines = file.readlines()
                self.agreements.clear()
                for line in lines[1:]:
                    row = line.strip().split(',')
                    if len(row) != 3 or not row[2].isdigit():
                        messagebox.showerror("Ошибка", "Неверный формат данных в файле.")
                        return
                    self.agreements.append(RentalAgreement(row[0], row[1], int(row[2])))

            self.update_treeview()
            messagebox.showinfo("Успешно", "Договоры успешно загружены.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for agreement in self.agreements:
            self.tree.insert("", tk.END, values=(agreement.property_type, agreement.manager, agreement.rent_amount))

    def segment_by_property_type(self):
        if not self.agreements:
            messagebox.showwarning("Предупреждение", "Нет договоров для сегментации.")
            return

        segmentation = {}
        for agreement in self.agreements:
            segmentation[agreement.property_type] = segmentation.get(agreement.property_type, 0) + 1

        self.plot_pie_chart(segmentation, "Сегментация по типу недвижимости")

    def segment_by_manager(self):
        if not self.agreements:
            messagebox.showwarning("Предупреждение", "Нет договоров для сегментации.")
            return

        segmentation = {}
        for agreement in self.agreements:
            segmentation[agreement.manager] = segmentation.get(agreement.manager, 0) + 1

        self.plot_pie_chart(segmentation, "Сегментация по менеджерам")

    def plot_pie_chart(self, data, title):
        labels = list(data.keys())
        sizes = list(data.values())

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(title)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = RentalApp(root)
    root.mainloop()
