# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag1_40223153a = Blueprint('ag1_40223153a', __name__, url_prefix='/ag1_40223153a', template_folder='templates')

@ag1_40223153a.route('/aaaa')
def aaaa():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic6 = cmbr.dup()
    basic6.rotate(150)
    basic6.translate(0, 40)
    
    basic7 = cmbr.dup()
    basic7.rotate(210)
    basic7.translate(40, 40)
    
    basic8 = cmbr.dup()
    basic8.rotate(270)
    basic8.translate(30, 57.5)
    
    basic9 = cmbr.dup()
    basic9.rotate(270)
    basic9.translate(20, 0)
    
    basic10 = cmbr.dup()
    basic10.rotate(270)
    basic10.translate(40, 0)
    
    basic11 = cmbr.dup()
    basic11.rotate(180)
    basic11.translate(40, 0)
    
    basic12 = cmbr.dup()
    basic12.rotate(180)
    basic12.translate(40, 20)
    
    basic13 = cmbr.dup()
    basic13.rotate(180)
    basic13.translate(0, 20)
   
    basic14 = cmbr.dup()
    basic14.rotate(180)
    basic14.translate(0, 0)
    
    basic15 = cmbr.dup()
    basic15.rotate(360)
    basic15.translate(40, 0)
    
    basic16 = cmbr.dup()
    basic16.rotate(150)
    basic16.translate(70, 40)
    
    basic17 = cmbr.dup()
    basic17.rotate(210)
    basic17.translate(110, 40)
    
    basic18 = cmbr.dup()
    basic18.rotate(270)
    basic18.translate(100, 57.5)

    basic19 = cmbr.dup()
    basic19.rotate(270)
    basic19.translate(90, 0)
   
    basic20 = cmbr.dup()
    basic20.rotate(270)
    basic20.translate(110, 0)
    
    basic21 = cmbr.dup()
    basic21.rotate(180)
    basic21.translate(110, 0)
    
    basic22 = cmbr.dup()
    basic22.rotate(180)
    basic22.translate(110, 20)
    
    basic23 = cmbr.dup()
    basic23.rotate(180)
    basic23.translate(70, 20)
    
    basic24 = cmbr.dup()
    basic24.rotate(180)
    basic24.translate(70, 0)
    
    basic25 = cmbr.dup()
    basic25.rotate(360)
    basic25.translate(110, 0)
    
    basic26 = cmbr.dup()
    basic26.rotate(150)
    basic26.translate(140, 40)
    
    basic27 = cmbr.dup()
    basic27.rotate(210)
    basic27.translate(180, 40)
    
    basic28 = cmbr.dup()
    basic28.rotate(270)
    basic28.translate(170, 57.5)
    
    basic29 = cmbr.dup()
    basic29.rotate(270)
    basic29.translate(160, 0)
    
    basic30 = cmbr.dup()
    basic30.rotate(270)
    basic30.translate(180, 0)
    
    basic31 = cmbr.dup()
    basic31.rotate(180)
    basic31.translate(180, 0)
    
    basic32 = cmbr.dup()
    basic32.rotate(180)
    basic32.translate(180, 20)
    
    basic33 = cmbr.dup()
    basic33.rotate(180)
    basic33.translate(140, 20)
    
    basic34 = cmbr.dup()
    basic34.rotate(180)
    basic34.translate(140, 0)
    
    basic35 = cmbr.dup()
    basic35.rotate(360)
    basic35.translate(180, 0)
    
    basic36 = cmbr.dup()
    basic36.rotate(150)
    basic36.translate(210, 40)
    
    basic37 = cmbr.dup()
    basic37.rotate(210)
    basic37.translate(250, 40)
    
    basic38 = cmbr.dup()
    basic38.rotate(270)
    basic38.translate(240, 57.5)
    
    basic39 = cmbr.dup()
    basic39.rotate(270)
    basic39.translate(230, 0)
    
    basic40 = cmbr.dup()
    basic40.rotate(270)
    basic40.translate(250, 0)
    
    basic41 = cmbr.dup()
    basic41.rotate(180)
    basic41.translate(250, 0)
    
    basic42 = cmbr.dup()
    basic42.rotate(180)
    basic42.translate(250, 20)
    
    basic43 = cmbr.dup()
    basic43.rotate(180)
    basic43.translate(210, 20)
    
    basic44 = cmbr.dup()
    basic44.rotate(180)
    basic44.translate(210, 0)
    
    basic45 = cmbr.dup()
    basic45.rotate(360)
    basic45.translate(250, 0)
     
    basic46 = cmbr.dup()
    basic46.rotate(360)
    basic46.translate(70, 0)
    
    basic47 = cmbr.dup()
    basic47.rotate(360)
    basic47.translate(140, 0)
    
    basic48 = cmbr.dup()
    basic48.rotate(360)
    basic48.translate(210, 0)
    
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
    cmbr.appendPath(basic45)
    cmbr.appendPath(basic46)
    cmbr.appendPath(basic47)
    cmbr.appendPath(basic48)
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 0.9, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 0.9, rot)

O(0, 20, 0, 0, 0, "green", True, 4)
</script>

<script type="text/python" src="/ag1_40323105/task1"></script>

</body>
</html>
'''
    return outstring
    
@ag1_40223153a.route('/badc')
def badc():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    basic1.rotate(180)
    basic1.translate(0, 0)
    
    basic2 = cmbr.dup()
    basic2.rotate(180)
    basic2.translate(0,20)
    
    basic3 = cmbr.dup()
    basic3.rotate(180)
    basic3.translate(0,40)
    
    basic4 = cmbr.dup()
    basic4.rotate(-270)
    basic4.translate(0,60)
  
    basic5 = cmbr.dup()
    basic5.rotate(-300)
    basic5.translate(20,60)
    
    basic6 = cmbr.dup()
    basic6.rotate(360)
    basic6.translate(37,50)
    
    basic7 = cmbr.dup()
    basic7.rotate(270)
    basic7.translate(20,20)
    
    basic8 = cmbr.dup()
    basic8.rotate(-58)
    basic8.translate(37,30)
    
    basic9 = cmbr.dup()
    basic9.rotate(58)
    basic9.translate(20,20)
    
    basic10 = cmbr.dup()
    basic10.rotate(180)
    basic10.translate(37,-10)
    
    basic11 = cmbr.dup()
    basic11.rotate(300)
    basic11.translate(37,-10)
    
    basic12 = cmbr.dup()
    basic12.rotate(270)
    basic12.translate(20,-20)
    
    basic13 = cmbr.dup()
    basic13.rotate(360)
    basic13.translate(70, 0)
    
    basic16 = cmbr.dup()
    basic16.rotate(150)
    basic16.translate(70, 40)
    
    basic17 = cmbr.dup()
    basic17.rotate(210)
    basic17.translate(110, 40)
    
    basic18 = cmbr.dup()
    basic18.rotate(270)
    basic18.translate(100, 57.5)

    basic19 = cmbr.dup()
    basic19.rotate(270)
    basic19.translate(90, 0)
   
    basic20 = cmbr.dup()
    basic20.rotate(270)
    basic20.translate(110, 0)
    
    basic21 = cmbr.dup()
    basic21.rotate(180)
    basic21.translate(110, 0)
    
    basic22 = cmbr.dup()
    basic22.rotate(180)
    basic22.translate(110, 20)
    
    basic23 = cmbr.dup()
    basic23.rotate(180)
    basic23.translate(70, 20)
    
    basic24 = cmbr.dup()
    basic24.rotate(180)
    basic24.translate(70, 0)
    
    basic25 = cmbr.dup()
    basic25.rotate(360)
    basic25.translate(110, 0)
    
    basic26 = cmbr.dup()
    basic26.rotate(360)
    basic26.translate(70, 0)
   
    basic27 = cmbr.dup()
    basic27.rotate(360)
    basic27.translate(140, 0)
    
    basic28 = cmbr.dup()
    basic28.rotate(360)
    basic28.translate(140,20)
    
    basic29 = cmbr.dup()
    basic29.rotate(360)
    basic29.translate(140,40)
    
    basic30 = cmbr.dup()
    basic30.rotate(360)
    basic30.translate(140,60)
    
    basic31 = cmbr.dup()
    basic31.rotate(-270)
    basic31.translate(140,-20)
    
    basic32 = cmbr.dup()
    basic32.rotate(135)
    basic32.translate(160,-20)
    
    basic33 = cmbr.dup()
    basic33.rotate(170)
    basic33.translate(174,-6)
    
    basic34 = cmbr.dup()
    basic34.rotate(180)
    basic34.translate(177,13)
    
    basic35 = cmbr.dup()
    basic35.rotate(-170)
    basic35.translate(177,33)
    
    basic36 = cmbr.dup()
    basic36.rotate(-111)
    basic36.translate(174,53)
    
    basic37 = cmbr.dup()
    basic37.rotate(-270)
    basic37.translate(140,60)
    
    basic38 = cmbr.dup()
    basic38.rotate(-270)
    basic38.translate(230,-20)
    
    basic39 = cmbr.dup()
    basic39.rotate(-120)
    basic39.translate(230,-20)
    
    basic40 = cmbr.dup()
    basic40.rotate(-160)
    basic40.translate(213,-10)
    
    basic41 = cmbr.dup()
    basic41.rotate(-180)
    basic41.translate(206,9)
    
    basic42 = cmbr.dup()
    basic42.rotate(160)
    basic42.translate(206,30)
    
    basic43 = cmbr.dup()
    basic43.rotate(120)
    basic43.translate(213,49)
    
    basic44 = cmbr.dup()
    basic44.rotate(120)
    basic44.translate(213,49)
    
    basic45 = cmbr.dup()
    basic45.rotate(90)
    basic45.translate(230,59)
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
    cmbr.appendPath(basic45)
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 0.9, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 0.9, rot)

O(0, 20, 0, 0, 0, "green", True, 4)
</script>

<script type="text/python" src="/ag1_40323105/task1"></script>

</body>
</html>
'''
    return outstring
    
@ag1_40223153a.route('/abcd')
def task3():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -300, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic10 = cmbr.dup()
    basic10.rotate(0)
    basic10.translate(0, 20)
    
    basic11 = cmbr.dup()
    basic11.rotate(170)
    basic11.translate(0, 20)
    
    basic12 = cmbr.dup()
    basic12.rotate(165)
    basic12.translate(3, 40)
    
    basic13 = cmbr.dup()
    basic13.rotate(90)
    basic13.translate(11, 59)
    
    basic14 = cmbr.dup()
    basic14.rotate(90)
    basic14.translate(0, 0)
    
    basic15 = cmbr.dup()
    basic15.rotate(90)
    basic15.translate(20, 0)
    
    basic16 = cmbr.dup()
    basic16.rotate(0)
    basic16.translate(40, 0)
    
    basic17 = cmbr.dup()
    basic17.rotate(195)
    basic17.translate(38,40)
    
    basic18 = cmbr.dup()
    basic18.rotate(10)
    basic18.translate(37,40)
    
    basic19 = cmbr.dup()
    basic19.rotate(0)
    basic19.translate(40,20)
    
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(0, -80)
    
    basic21 = cmbr.dup()
    basic21.rotate(0)
    basic21.translate(0, -80)
    
    basic22 = cmbr.dup()
    basic22.rotate(0)
    basic22.translate(0, -60)
    
    basic23 = cmbr.dup()
    basic23.rotate(0)
    basic23.translate(0, -40)
    
    basic24 = cmbr.dup()
    basic24.rotate(90)
    basic24.translate(0,-40)
    
    basic25 = cmbr.dup()
    basic25.rotate(90)
    basic25.translate(0, -80)
    
    basic26 = cmbr.dup()
    basic26.rotate(90)
    basic26.translate(0,-120)
    
    basic27 = cmbr.dup()
    basic27.rotate(300)
    basic27.translate(37, -110)
    
    basic28 = cmbr.dup()
    basic28.rotate(60)
    basic28.translate(20,-40)
    
    basic29 = cmbr.dup()
    basic29.rotate(0)
    basic29.translate(37,-90)
    
    basic210 = cmbr.dup()
    basic210.rotate(60)
    basic210.translate(20,-80)
    
    basic211 = cmbr.dup()
    basic211.rotate(0)
    basic211.translate(0,-100)
    
    basic212 = cmbr.dup()
    basic212.rotate(0)
    basic212.translate(38,-50)
    
    basic213 = cmbr.dup()
    basic213.rotate(300)
    basic213.translate(38,-70)
    
    basic30 = cmbr.dup()
    basic30.rotate(60)
    basic30.translate(3, -210)
    
    basic31 = cmbr.dup()
    basic31.rotate(340)
    basic31.translate(3, -150)
    
    basic32 = cmbr.dup()
    basic32.rotate(300)
    basic32.translate(20, -140)
    
    basic33 = cmbr.dup()
    basic33.rotate(90)
    basic33.translate(20, -140)
    
    basic34 = cmbr.dup()
    basic34.rotate(0)
    basic34.translate(-4, -170)
    
    basic35 = cmbr.dup()
    basic35.rotate(90)
    basic35.translate(20, -220)
    
    basic36 = cmbr.dup()
    basic36.rotate(20)
    basic36.translate(-4, -190)
    
    basic40 = cmbr.dup()
    basic40.rotate(0)
    basic40.translate(0, -280)
    
    basic41 = cmbr.dup()
    basic41.rotate(0)
    basic41.translate(0, -260)
    
    basic42 = cmbr.dup()
    basic42.rotate(0)
    basic42.translate(0, -240)
    
    basic43 = cmbr.dup()
    basic43.rotate(0)
    basic43.translate(0, -300)
    
    basic44 = cmbr.dup()
    basic44.rotate(90)
    basic44.translate(0, -320)
    
    basic45 = cmbr.dup()
    basic45.rotate(90)
    basic45.translate(0, -240)
    
    basic46 = cmbr.dup()
    basic46.rotate(300)
    basic46.translate(40, -310)
    
    basic47 = cmbr.dup()
    basic47.rotate(240)
    basic47.translate(38,-250)
    
    basic48 = cmbr.dup()
    basic48.rotate(210)
    basic48.translate(48,-267)
    
    basic49 = cmbr.dup()
    basic49.rotate(0)
    basic49.translate(48,-267)
    
    basic410 = cmbr.dup()
    basic410.rotate(160)
    basic410.translate(40,-310)
    
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic210)
    cmbr.appendPath(basic211)
    cmbr.appendPath(basic212)
    cmbr.appendPath(basic213)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
    cmbr.appendPath(basic45)
    cmbr.appendPath(basic46)
    cmbr.appendPath(basic47)
    cmbr.appendPath(basic48)
    cmbr.appendPath(basic49)
    cmbr.appendPath(basic410)

    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 0.9, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 0.9, rot)

O(0, 20, 0, 0, 0, "green", True, 4)
</script>

<script type="text/python" src="/ag1_40223153/task3"></script>

</body>
</html>
'''
    return outstring