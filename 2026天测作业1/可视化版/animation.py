# -*- coding: utf-8 -*-
"""
@Time    : 2026/9/15
@Author  : Zixiao Guo
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from rotation import Rx, Ry, Rz

def rotation_animation(
        P,
        z_angle,
        y_angle,
        x_angle
):
    P0 = P.reshape(3)

    # Z旋转过程
    z_frames=[]

    for angle in np.linspace(
        0,
        z_angle,
        40
    ):

        z_frames.append(
            Rz(angle) @ P0
        )

    P1 = Rz(z_angle) @ P0

    # Y旋转过程

    y_frames=[]

    for angle in np.linspace(
        0,
        y_angle,
        40
    ):

        y_frames.append(
            Ry(angle) @ P1
        )

    P2 = Ry(y_angle) @ P1

    # X旋转过程

    x_frames=[]

    for angle in np.linspace(
        0,
        x_angle,
        40
    ):

        x_frames.append(
            Rx(angle) @ P2
        )

    frames = (
        z_frames
        +
        y_frames
        +
        x_frames
    )
    fig = plt.figure(
        figsize=(7,7)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )
    L=1.2
    ax.quiver(
        0,0,0,
        L,0,0,
        color="black"
    )
    ax.text(
        L,0,0,
        "X"
    )
    ax.quiver(
        0,0,0,
        0,L,0,
        color="black"
    )
    ax.text(
        0,L,0,
        "Y"
    )
    ax.quiver(
        0,0,0,
        0,0,L,
        color="black"
    )
    ax.text(
        0,0,L,
        "Z"
    )
    # 初始箭头
    initial_arrow = ax.quiver(
        0,0,0,
        P0[0],
        P0[1],
        P0[2],
        color="blue",
        linewidth=3
    )
    moving_arrow = ax.quiver(
        0,0,0,
        P0[0],
        P0[1],
        P0[2],
        color="red",
        linewidth=3
    )
    ax.set_xlim(
        [-1,1]
    )

    ax.set_ylim(
        [-1,1]
    )

    ax.set_zlim(
        [-1,1]
    )
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    title=ax.set_title(
        "Coordinate Rotation Animation"
    )
    def update(frame):
        nonlocal moving_arrow
        # 删除旧箭头
        moving_arrow.remove()
        vector = frames[frame]
        moving_arrow=ax.quiver(
            0,0,0,
            vector[0],
            vector[1],
            vector[2],
            color="red",
            linewidth=3
        )
        if frame < 40:

            title.set_text(
                "Rotate around Z axis"
            )
        elif frame <80:
            title.set_text(
                "Rotate around Y axis"
            )

        else:

            title.set_text(
                "Rotate around X axis"
            )
        return moving_arrow,title

    ani=FuncAnimation(
        fig,
        update,
        frames=len(frames),
        interval=80,
        blit=False
    )
    plt.show()