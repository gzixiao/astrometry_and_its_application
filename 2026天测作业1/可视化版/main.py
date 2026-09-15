# -*- coding: utf-8 -*-
"""
@Time    : 2026/9/15
@Author  : Zixiao Guo
"""
import tkinter as tk
from tkinter import messagebox
from rotation import calculate
from animation import rotation_animation

def run_calculation():

    try:

        longitude=float(
            entry_lon.get()
        )

        latitude=float(
            entry_lat.get()
        )


        z_angle=float(
            entry_z.get()
        )

        y_angle=float(
            entry_y.get()
        )

        x_angle=float(
            entry_x.get()
        )


        result = calculate(
            longitude,
            latitude,
            z_angle,
            y_angle,
            x_angle
        )



        output.delete(
            "1.0",
            tk.END
        )


        output.insert(
            tk.END,
            "----- 初始单位矢量 -----\n"
        )

        output.insert(
            tk.END,
            str(
                result["P"].flatten()
            )
            +
            "\n\n"
        )


        output.insert(
            tk.END,
            "----- Rx矩阵 -----\n"
        )

        output.insert(
            tk.END,
            str(
                result["Rx"]
            )
            +
            "\n"
        )


        output.insert(
            tk.END,
            "----- Ry矩阵 -----\n"
        )

        output.insert(
            tk.END,
            str(
                result["Ry"]
            )
            +
            "\n"
        )



        output.insert(
            tk.END,
            "----- Rz矩阵 -----\n"
        )


        output.insert(
            tk.END,
            str(
                result["Rz"]
            )
            +
            "\n"
        )



        output.insert(
            tk.END,
            "----- 旋转后XYZ分量 -----\n"
        )


        output.insert(
            tk.END,
            str(
                result["P_new"].flatten()
            )
            +
            "\n\n"
        )



        output.insert(
            tk.END,
            "----- 旋转后方向 -----\n"
        )


        output.insert(
            tk.END,
            f"经度：{result['longitude']:.4f}°    "
        )


        output.insert(
            tk.END,
            f"纬度：{result['latitude']:.4f}°"
        )

        # 显示动态旋转动画
        rotation_animation(
            result["P"],
            z_angle,
            y_angle,
            x_angle
        )


    except Exception as e:


        messagebox.showerror(
            "输入错误",
            str(e)
        )


# 创建窗口

window=tk.Tk()


window.title(
    "三维坐标旋转计算程序  郭子筱202528019532009"
)


window.geometry(
    "520x600"
)



# -------------------------
# 输入区域
# -------------------------


tk.Label(
    window,
    text="初始方向",
    font=(14)
).pack()



tk.Label(
    window,
    text="经度（°）"
).pack()


entry_lon=tk.Entry(window)

entry_lon.insert(
    0,
    "40"
)

entry_lon.pack()



tk.Label(
    window,
    text="纬度（°）"
).pack()


entry_lat=tk.Entry(window)

entry_lat.insert(
    0,
    "30"
)

entry_lat.pack()



tk.Label(
    window,
    text="旋转角度",
    font=(14)
).pack()



tk.Label(
    window,
    text="绕Z轴旋转（°）"
).pack()


entry_z=tk.Entry(window)

entry_z.insert(
    0,
    "120"
)

entry_z.pack()



tk.Label(
    window,
    text="绕Y轴旋转（°）"
).pack()


entry_y=tk.Entry(window)

entry_y.insert(
    0,
    "27"
)

entry_y.pack()



tk.Label(
    window,
    text="绕X轴旋转（°）"
).pack()


entry_x=tk.Entry(window)

entry_x.insert(
    0,
    "15"
)

entry_x.pack()



# 计算按钮

button=tk.Button(
    window,
    text="开始计算",
    width=20,
    height=1,
    command=run_calculation
)

button.pack(
    pady=5
)

# 输出窗口

output=tk.Text(
    window,
    width=70,
    height=20
)
output.pack()
window.mainloop()