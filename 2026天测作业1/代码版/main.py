# -*- coding: utf-8 -*-
"""
@Time    : 2026/9/15
@Author  : Zixiao Guo
"""
import numpy as np
import math

# 子程序1：生成绕X轴旋转矩阵 Rx(alpha)
def Rx(alpha):
    """
    绕X轴旋转矩阵
    alpha: 旋转角度(单位：度)
    """
    a = math.radians(alpha)

    R = np.array([
        [1, 0, 0],
        [0, math.cos(a), math.sin(a)],
        [0, -math.sin(a), math.cos(a)]
    ])

    return R


# 子程序2：生成绕Y轴旋转矩阵 Ry(beta)
def Ry(beta):
    """
    绕Y轴旋转矩阵
    beta: 旋转角度(单位：度)
    """
    b = math.radians(beta)

    R = np.array([
        [math.cos(b), 0, -math.sin(b)],
        [0, 1, 0],
        [math.sin(b), 0, math.cos(b)]
    ])

    return R


# 子程序3：生成绕Z轴旋转矩阵 Rz(gamma)
def Rz(gamma):
    """
    绕Z轴旋转矩阵
    gamma: 旋转角度(单位：度)
    """
    g = math.radians(gamma)

    R = np.array([
        [math.cos(g), math.sin(g), 0],
        [-math.sin(g), math.cos(g), 0],
        [0, 0, 1]
    ])

    return R



# 经纬度转换为单位矢量
def lon_lat_to_vector(longitude, latitude):
    """
    根据经纬度生成单位矢量
    longitude: 经度(度)
    latitude: 纬度(度)
    """

    lon = math.radians(longitude)
    lat = math.radians(latitude)

    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)

    vector = np.array([
        [x],
        [y],
        [z]
    ])

    return vector

# 单位矢量转换为经纬度
def vector_to_lon_lat(vector):
    """
    根据单位矢量生成经纬度
    """

    x = vector[0,0]
    y = vector[1,0]
    z = vector[2,0]

    longitude = math.degrees(math.atan2(y,x))
    latitude = math.degrees(math.asin(z))

    return longitude, latitude

# 主程序
def main():

    # 1. 初始单位矢量
    # 指向经度40°，纬度30°
    longitude = 40
    latitude = 30

    P = lon_lat_to_vector(longitude, latitude)

    print("初始单位矢量：")
    print(P)


    # 2. 生成三个旋转矩阵
    # 顺序：
    # 绕Z轴旋转120°
    # 绕Y轴旋转27°
    # 绕X轴旋转15°

    Rz_matrix = Rz(120)
    Ry_matrix = Ry(27)
    Rx_matrix = Rx(15)


    print("\n绕X轴旋转矩阵 Rx:")
    print(Rx_matrix)
    print("\n绕Y轴旋转矩阵 Ry:")
    print(Ry_matrix)
    print("\n绕Z轴旋转矩阵 Rz:")
    print(Rz_matrix)


    # 3. 坐标旋转变换
    # P' = Rx * Ry * Rz * P

    P_new = Rx_matrix @ Ry_matrix @ Rz_matrix @ P


    # 4. 输出结果
    print("\n旋转后的单位矢量：")

    print(P_new)

    print("\n新坐标系中的三个分量：")
    print("x =", P_new[0,0])
    print("y =", P_new[1,0])
    print("z =", P_new[2,0])
    lon, lat = vector_to_lon_lat(P_new)

    print("旋转后的经度:", lon)
    print("旋转后的纬度:", lat)

# 程序入口
if __name__ == "__main__":
    main()
