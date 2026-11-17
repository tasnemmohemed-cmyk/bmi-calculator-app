import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # تحويل الطول من سم إلى متر
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة أكبر من الصفر.")
            return
            
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            status = "وزن منخفض (Underweight)"
            color = "#3498db"
        elif 18.5 <= bmi < 24.9:
            status = "وزن مثالي وطبيعي (Normal)"
            color = "#2ecc71"
        elif 25 <= bmi < 29.9:
            status = "زيادة في الوزن (Overweight)"
            color = "#f1c40f"
        else:
            status = "سمنة (Obese)"
            color = "#e74c3c"
            
        result_label.config(text=f"النتيجة: {bmi} - {status}", fg=color)
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال أرقام صحيحة في الحقول.")

# إعداد واجهة التطبيق
root = tk.Tk()
root.title("حاسبة مؤشر كتلة الجسم - BMI")
root.geometry("400x350")
root.config(bg="#f5f6fa")

title_label = tk.Label(root, text="حاسبة مؤشر كتلة الجسم (BMI)", font=("Arial", 14, "bold"), bg="#f5f6fa", fg="#2c3e50")
title_label.pack(pady=20)

# حقل الوزن
weight_frame = tk.Frame(root, bg="#f5f6fa")
weight_frame.pack(pady=5)
tk.Label(weight_frame, text="الوزن (كجم):", font=("Arial", 11), bg="#f5f6fa").pack(side=tk.LEFT, padx=5)
weight_entry = tk.Entry(weight_frame, font=("Arial", 11), width=15)
weight_entry.pack(side=tk.LEFT, padx=5)

# حقل الطول
height_frame = tk.Frame(root, bg="#f5f6fa")
height_frame.pack(pady=10)
tk.Label(height_frame, text="الطول (سم):", font=("Arial", 11), bg="#f5f6fa").pack(side=tk.LEFT, padx=5)
height_entry = tk.Entry(height_frame, font=("Arial", 11), width=15)
height_entry.pack(side=tk.LEFT, padx=5)

# زر الحساب
calc_button = tk.Button(root, text="احسب النتيجة", font=("Arial", 11, "bold"), bg="#2980b9", fg="white", width=15, command=calculate_bmi)
calc_button.pack(pady=15)

# خانة النتيجة
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="#f5f6fa")
result_label.pack(pady=10)

root.mainloop()