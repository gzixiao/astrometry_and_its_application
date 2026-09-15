# -*- coding: utf-8 -*-
"""
@Time    : 2026/9/15
@Author  : Zixiao Guo
"""
import numpy as np
import math

# 绕X轴旋转矩阵
def Rx(alpha):

    a = math.radians(alpha)

    R = np.array([
        [1, 0, 0],
        [0, math.cos(a), math.sin(a)],
        [0, -math.sin(a), math.cos(a)]
    ])

    return R
# 绕Y轴旋转矩阵
def Ry(beta):

    b = math.radians(beta)

    R = np.array([
        [math.cos(b), 0, -math.sin(b)],
        [0, 1, 0],
        [math.sin(b), 0, math.cos(b)]
    ])

    return R

# 绕Z轴旋转矩阵
def Rz(gamma):

    g = math.radians(gamma)

    R = np.array([
        [math.cos(g), math.sin(g), 0],
        [-math.sin(g), math.cos(g), 0],
        [0, 0, 1]
    ])

    return R

# 经纬度转换为单位方向矢量
def lon_lat_to_vector(longitude, latitude):
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

# 三维向量转换回经纬度
def vector_to_lon_lat(vector):
    x = vector[0,0]
    y = vector[1,0]
    z = vector[2,0]
    longitude = math.degrees(
        math.atan2(y,x)
    )
    latitude = math.degrees(
        math.asin(z)
    )
    return longitude, latitude

def calculate(
        longitude,
        latitude,
        z_angle,
        y_angle,
        x_angle
):
    P = lon_lat_to_vector(
        longitude,
        latitude
    )
    Rz_matrix = Rz(z_angle)
    Ry_matrix = Ry(y_angle)
    Rx_matrix = Rx(x_angle)
    P_new = (
        Rx_matrix
        @
        Ry_matrix
        @
        Rz_matrix
        @
        P
    )

    new_lon,new_lat = vector_to_lon_lat(
        P_new
    )
    return {
        "P":P,
        "Rx":Rx_matrix,
        "Ry":Ry_matrix,
        "Rz":Rz_matrix,
        "P_new":P_new,
        "longitude":new_lon,
        "latitude":new_lat
    }