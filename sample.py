import pyxel

pyxel.init(160,120)

while True:
    pyxel.cls(pyxel.COLOR_GREEN) # 緑の画面
    # 座標 (x, y) で大きさ w × h の長方形
    pyxel.rectb(x=pyxel.frame_count % 160 - 40, y=20, w=40, h=40,
                       col=pyxel.COLOR_WHITE)
    pyxel.flip() # 画面を更新