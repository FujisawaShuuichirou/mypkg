# SPDX-FileCopyrightText: 2022 Shuichiro Fujisawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def cb(msg):
    global node
    #node.get_logger().info("Listen: %s" % msg.data)
    #print(msg.data)
    #print(len(msg.data))
    hoge = []
    count = 0 

    for i in msg.data:
        if count == 0:
            if i == "a":
                hoge.append("あ")
            elif i == "i":
                hoge.append("い")
            elif i == "u":
                hoge.append("う")
            elif i == "e":
                hoge.append("え")
            elif i == "o":
                hoge.append("お")
            else:
                tmp1 = i
                count = 1
                continue

        while count != 0:
            fl = 0
            if count == 1:

                if tmp1 == "k":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    elif i == "w":
                        tmp2 = i
                        count == 2
                    else:
                        if i == "a":
                            hoge.append("か")
                            count = 0
                        elif i == "i":
                            hoge.append("き")
                            count = 0
                        elif i == "u":
                            hoge.append("く")
                            count = 0
                        elif i == "e":
                            hoge.append("け")
                            count = 0
                        elif i == "o":
                            hoge.append("こ")
                            count = 0
                        elif i == "k":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "s":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    elif i == "w":
                        tmp2 = i
                        count = 2
                    elif i == "h":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("さ")
                            count = 0
                        elif i == "i":
                            hoge.append("し")
                            count = 0
                        elif i == "u":
                            hoge.append("す")
                            count = 0
                        elif i == "e":
                            hoge.append("せ")
                            count = 0
                        elif i == "o":
                            hoge.append("そ")
                            count = 0
                        elif i == "s":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "t":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    elif i == "s":
                        tmp2 = i
                        count = 2
                    elif i == "h":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("た")
                            count = 0
                        elif i == "i":
                            hoge.append("ち")
                            count = 0
                        elif i == "u":
                            hoge.append("つ")
                            count = 0
                        elif i == "e":
                            hoge.append("て")
                            count = 0
                        elif i == "o":
                            hoge.append("と")
                            count = 0
                        elif i == "t":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "c":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    elif i == "h":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("か")
                        elif i == "i":
                            hoge.append("し")
                        elif i == "u":
                            hoge.append("く")
                        elif i == "e":
                            hoge.append("せ")
                        elif i == "o":
                            hoge.append("こ")
                        elif i == "c":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "q":
                    if i == "a":
                        hoge.append("くぁ")
                    elif i == "i":
                        hoge.append("くぃ")
                    elif i == "u":
                        hoge.append("く")
                    elif i == "e":
                        hoge.append("くぇ")
                    elif i == "o":
                        hoge.append("くぉ")
                    elif i == "q":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                    else:
                        hoge.append(tmp1)
                        fl = 1
                        tmp1 = i
                        break
                    if fl == 0:
                        count = 0

                elif tmp1 == "n":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    elif i == "w":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("な")
                        elif i == "i":
                            hoge.append("に")
                        elif i == "u":
                            hoge.append("ぬ")
                        elif i == "e":
                            hoge.append("ね")
                        elif i == "o":
                            hoge.append("の")
                        elif i == "n":
                            hoge.append("ん")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append("ん")
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "h":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("は")
                        elif i == "i":
                            hoge.append("ひ")
                        elif i == "u":
                            hoge.append("ふ")
                        elif i == "e":
                            hoge.append("へ")
                        elif i == "o":
                            hoge.append("ほ")
                        elif i == "h":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "f":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("ふぁ")
                        elif i == "i":
                            hoge.append("ふぃ")
                        elif i == "u":
                            hoge.append("ふ")
                        elif i == "e":
                            hoge.append("ふぇ")
                        elif i == "o":
                            hoge.append("ふぉ")
                        elif i == "f":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "m":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("ま")
                        elif i == "i":
                            hoge.append("み")
                        elif i == "u":
                            hoge.append("む")
                        elif i == "e":
                            hoge.append("め")
                        elif i == "o":
                            hoge.append("も")
                        elif i == "m":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "y":
                    if i == "a":
                        hoge.append("や")
                    elif i == "i":
                        hoge.append("い")
                    elif i == "u":
                        hoge.append("ゆ")
                    elif i == "e":
                        hoge.append("いぇ")
                    elif i == "o":
                        hoge.append("よ")
                    elif i == "y":
                        hoge.append("っ")
                        tmp1 = i
                        fl = 1
                        break
                    else:
                        hoge.append(tmp1)
                        fl = 1
                        tmp1 = i
                        break
                    if fl == 0:
                        count = 0

                elif tmp1 == "r":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("ら")
                        elif i == "i":
                            hoge.append("り")
                        elif i == "u":
                            hoge.append("る")
                        elif i == "e":
                            hoge.append("れ")
                        elif i == "o":
                            hoge.append("ろ")
                        elif i == "r":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "w":
                    if i == "a":
                        hoge.append("わ")
                    elif i == "i":
                        hoge.append("うぃ")
                    elif i == "u":
                        hoge.append("う")
                    elif i == "e":
                        hoge.append("うぇ")
                    elif i == "o":
                        hoge.append("を")
                    elif i == "w":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                    else:
                        hoge.append(tmp1)
                        fl = 1
                        tmp1 = i
                        break
                    if fl == 0:
                        count = 0

                elif tmp1 == "g":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("が")
                        elif i == "i":
                            hoge.append("ぎ")
                        elif i == "u":
                            hoge.append("ぐ")
                        elif i == "e":
                            hoge.append("げ")
                        elif i == "o":
                            hoge.append("ご")
                        elif i == "g":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "z":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("ざ")
                        elif i == "i":
                            hoge.append("じ")
                        elif i == "u":
                            hoge.append("ず")
                        elif i == "e":
                            hoge.append("ぜ")
                        elif i == "o":
                            hoge.append("ぞ")
                        elif i == "z":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "j":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("じゃ")
                        elif i == "i":
                            hoge.append("じ")
                        elif i == "u":
                            hoge.append("じゅ")
                        elif i == "e":
                            hoge.append("じぇ")
                        elif i == "o":
                            hoge.append("じょ")
                        elif i == "j":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "d":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    elif i == "h":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("だ")
                        elif i == "i":
                            hoge.append("ぢ")
                        elif i == "u":
                            hoge.append("づ")
                        elif i == "e":
                            hoge.append("で")
                        elif i == "o":
                            hoge.append("ど")
                        elif i == "d":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "b":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("ば")
                        elif i == "i":
                            hoge.append("び")
                        elif i == "u":
                            hoge.append("ぶ")
                        elif i == "e":
                            hoge.append("べ")
                        elif i == "o":
                            hoge.append("ぼ")
                        elif i == "b":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "v":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("ヴぁ")
                        elif i == "i":
                            hoge.append("ヴぃ")
                        elif i == "u":
                            hoge.append("ヴ")
                        elif i == "e":
                            hoge.append("ヴぇ")
                        elif i == "o":
                            hoge.append("ヴぉ")
                        elif i == "v":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0

                elif tmp1 == "p":
                    if i == "y":
                        tmp2 = i
                        count = 2
                    else:
                        if i == "a":
                            hoge.append("ぱ")
                        elif i == "i":
                            hoge.append("ぴ")
                        elif i == "u":
                            hoge.append("ぷ")
                        elif i == "e":
                            hoge.append("ぺ")
                        elif i == "o":
                            hoge.append("ぽ")
                        elif i == "p":
                            hoge.append("っ")
                            tmp1 = i
                            fl = 1
                            break
                        else:
                            hoge.append(tmp1)
                            fl = 1
                            tmp1 = i
                            break
                        if fl == 0:
                            count = 0
                        
            else:
                hoge.append(i)
                count = 0

    result = ' '.join(map(str, hoge))
    print(result.replace(' ', ''))

rclpy.init()
node = Node("tra_listnener")
pub = node.create_subscription(String, "translation", cb, 10)
rclpy.spin(node)
