from turtle import *


def make_national_flag(flag_height=300, flag_border_width=6):
    # 国旗の横の長さ
    flag_width = flag_height * 3 / 2  # 2:3比率

    # 日の丸
    hinomaru_diameter = flag_height * 3 / 5
    hinomaru_radius = hinomaru_diameter / 2

    # 画面初期設定
    bgcolor("white")
    pensize(flag_border_width)
    pencolor("black")
    penup()

    # 中心線上の長方形パスの半分
    path_half_w = (flag_width - flag_border_width) / 2
    path_half_h = (flag_height - flag_border_width) / 2

    # 左上に移動
    setheading(90)  # 上向き
    forward(path_half_h)  # 中央から上辺中央
    setheading(180)  # 左向き
    forward(path_half_w)  # 上辺中央から左上

    # 枠を描く
    pendown()
    setheading(0)  # 右向き
    for _ in range(2):
        forward((flag_width - flag_border_width))
        right(90)
        forward((flag_height - flag_border_width))
        right(90)
    penup()

    # 左上中央へ戻る
    setheading(0)  # 右向き
    forward(path_half_w)  # 左上から上辺中央
    setheading(270)  # 下向き
    forward(path_half_h)  # 上辺中央から中央

    # 日の丸を中心に描写
    setheading(270)  # 下向き
    forward(hinomaru_radius)  # 中心から円の下端
    setheading(0)  # 右向きにして描き始める
    pendown()
    color("red")
    begin_fill()
    circle(hinomaru_radius)
    end_fill()
    penup()

    hideturtle()
    done()


# 比率を2:3にするため国旗の高さと縁の太さのみを指定可能
make_national_flag()
