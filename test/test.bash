#!/bin/bash
# SPDX-FileCopyrightText: 2022 Shuichiro Fujisawa
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 10'

#gnome-terminal ros2 run mypkg tra_listener > /tmp/mypkg.log
#timeout 5 ros2 run mypkg test_talker
#timeout 5 ros2 run mypkg tra_listener > /tmp/mypkg.log

#cat /tmp/mypkg.log |
#grep 'こんばんはあしたもよろしくおねがいします'

