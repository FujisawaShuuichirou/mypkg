# ノード
* talker       : 0から1ずつカウントアップしたものをInt16型のメッセージでcountupを通じて送信する。
* listener     : countupからメッセージをもらって表示する。
* tra_talker   : 標準入力からアルファベットを読み込みString型のメッセージでtranslationを通じて送信する。
* tra_listener : translationから受けっとたアルファベットを対応するひらがなに変換する。

![test](https://github.com/FujisawaShuuichirou/mypkg/actions/workflows/test.yml/badge.svg)

## ダウンロード方法
* 以下を端末で実行する
  ```
  $ git clone https://github.com/FujisawaShuuichirou/mypkg.git
  ```

## パッケージのビルド
* ビルド作業
  ```
  $ pwd
  /home/~/ros2_ws/src  #現在のディレクトリの確認
  $ cd ../             #~/ros2_wsへ移動
  $ colcon build
  ```
* ros2_ws下のパッケージを利用可能にする
  ````
  ```
  # ~/.bahsrcの末尾に下の二行を追加
  source ~/ros2_ws/install/setup.bash
  source ~/ros2_ws/install/local_setup.bash
  ```

  $ source ~/.bashrc
  ````


## talker listener

* talker   : 0から1ずつカウントアップしたものをInt16型のメッセージでcountupを通じて送信する。
* listener : countupからメッセージをもらって表示する。

* 使用例
  ```
  $ ros2 run mypkg talker

  もう一つ端末を開いて

  $ ros2 run mypkg listener
  [INFO] [1672501847.234085000] [listener]: Listen: 0
  [INFO] [1672501847.733796800] [listener]: Listen: 1
  [INFO] [1672501848.234175000] [listener]: Listen: 2
  [INFO] [1672501848.734066600] [listener]: Listen: 3
  [INFO] [1672501849.232931000] [listener]: Listen: 4
  [INFO] [1672501849.733842700] [listener]: Listen: 5
  [INFO] [1672501850.233608900] [listener]: Listen: 6
  [INFO] [1672501850.733801900] [listener]: Listen: 7
  [INFO] [1672501851.232465400] [listener]: Listen: 8
  [INFO] [1672501851.733883800] [listener]: Listen: 9
  [INFO] [1672501852.233563900] [listener]: Listen: 10
  ```

## tra_talker tra_listener

* tra_talker   : 標準入力からアルファベットを読み込みString型のメッセージでtranslationを通じて送信する。
* tra_listener : translationから受けっとたアルファベットを対応するひらがなに変換し画面に表示する。

* 使用例
  ```
  $ ros2 run mypkg tra_listener

  もう一つ端末を開いて以下のものを入力する。

  $ ros2 run mypkg tra_talker
  konbanha
  sayounara
  okaasan
  okaasann
  gakuseinokoroniganbattakotohanandesuka
  hogehoge

  変換後のtra_listener側の端末の表示

  $ ros2 run mypkg tra_listener
  こんばんは
  さようなら
  おかあさ
  おかあさん
  がくせいのころにがんばったことはなんですか
  ほげほげ
  ```

## 必要なソフトウェア
* Python
* ROS2

## テスト環境
* Ubuntu 20.04 on WSL

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
     * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2022 Shuichiro Fujisawa
