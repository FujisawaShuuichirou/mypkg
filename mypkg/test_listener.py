import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def cb(msg):
    global node
    #node.get_logger().info("Listen: %s" % msg.data)
    print(msg.data)
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
                    elif i == "i":
                        hoge.append("き")
                    elif i == "u":
                        hoge.append("く")
                    elif i == "e":
                        hoge.append("け")
                    elif i == "o":
                        hoge.append("こ")
                    else:
                        hoge.append(i)
                    count = 0

            elif tmp1 == "s":
                if i == "y":
                    tmp2 = i
                    count = 2
                elif i == "w":
                    tmp2 = i
                    count = 2
                elif i == "h":
                    tmp2 == i
                    count = 2
                else:
                    if i == "a":
                        hoge.append("さ")
                    elif i == "i":
                        hoge.append("し")
                    elif i == "u":
                        hoge.append("す")
                    elif i == "e":
                        hoge.append("せ")
                    elif i == "o":
                        hoge.append("そ")
                    else:
                        hoge.append(i)
                    count = 0

            elif tmp1 == "t":
                if i == "y":
                    tmp2 = i
                    count = 2
                elif i == "s":
                    tmp2 = i
                    count = 2
                elif i == "h":
                    tmp2 == i
                    count = 2
                else:
                    if i == "a":
                        hoge.append("た")
                    elif i == "i":
                        hoge.append("ち")
                    elif i == "u":
                        hoge.append("つ")
                    elif i == "e":
                        hoge.append("て")
                    elif i == "o":
                        hoge.append("と")
                    else:
                        hoge.append(i)
                    count = 0

            elif tmp1 == "c":
                if i == "y":
                    tmp2 = i
                    count = 2
                elif i == "h":
                    tmp2 == i
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
                    else:
                        hoge.append(i)
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
                else:
                    hoge.append(i)
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
                    else:
                        hoge.append(i)
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
                    else:
                        hoge.append(tmp1)
                    count = 0

            hoge.append(i)
        count += 1

    result = ' '.join(map(str, hoge))
    print(result.replace(' ', ''))

rclpy.init()
node = Node("test_listener")
pub = node.create_subscription(String, "translation", cb, 10)
rclpy.spin(node)
