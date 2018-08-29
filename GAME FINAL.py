import time
import sys

import turtle as t

def drawline(x1,y1,x2,y2):
    t.speed(4)
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
def map():
    x1=-600
    y1=300
    x2=-450
    y2=300
    drawline(x1,y1,x2,y2)

    x1=-450
    y1=300
    x2=-450
    y2=150
    drawline(x1,y1,x2,y2)

    x1=-450
    y1=150
    x2=-600
    y2=150
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=150
    x2=-600
    y2=300
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=300
    x2=-600
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=200
    x2=-450
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-450
    y1=200
    x2=-450
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-450
    y1=250
    x2=-600
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=250
    x2=-600
    y2=150
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=150
    x2=-590
    y2=150
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=150
    x2=-590
    y2=170
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=170
    x2=-580
    y2=170
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=170
    x2=-580
    y2=150
    drawline(x1,y1,x2,y2)


    x1=-580
    y1=150
    x2=-600
    y2=150
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=150
    x2=-600
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=200
    x2=-590
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=200
    x2=-590
    y2=220
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=220
    x2=-580
    y2=220
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=220
    x2=-580
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=200
    x2=-600
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=200
    x2=-600
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=250
    x2=-590
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=250
    x2=-590
    y2=270
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=270
    x2=-580
    y2=270
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=270
    x2=-580
    y2=250
    drawline(x1,y1,x2,y2)

    #window 1 (221C Bakers Street)
    x1=-560
    y1=280
    x2=-540
    y2=280
    drawline(x1,y1,x2,y2)

    x1=-540
    y1=280
    x2=-540
    y2=260
    drawline(x1,y1,x2,y2)

    x1=-540
    y1=260
    x2=-560
    y2=260
    drawline(x1,y1,x2,y2)

    x1=-560
    y1=260
    x2=-560
    y2=280
    drawline(x1,y1,x2,y2)

    x1=-540
    y1=280
    x2=-435
    y2=350
    drawline(x1,y1,x2,y2)

    x1=-435
    y1=350
    x2=-300
    y2=350
    drawline(x1,y1,x2,y2)

    x1=-300
    y1=350
    x2=-300
    y2=280
    drawline(x1,y1,x2,y2)

    x1=-300
    y1=280
    x2=-435
    y2=280
    drawline(x1,y1,x2,y2)

    x1=-435
    y1=280
    x2=-435
    y2=340
    drawline(x1,y1,x2,y2)

    x1=-435
    y1=340
    x2=-540
    y2=280
    drawline(x1,y1,x2,y2)
    #window 2 (221B Bakers Street)
    x1=-490
    y1=210
    x2=-470
    y2=210
    drawline(x1,y1,x2,y2)

    x1=-470
    y1=210
    x2=-470
    y2=230
    drawline(x1,y1,x2,y2)

    x1=-470
    y1=230
    x2=-490
    y2=230
    drawline(x1,y1,x2,y2)

    x1=-490
    y1=230
    x2=-490
    y2=210
    drawline(x1,y1,x2,y2)

    x1=-490
    y1=210
    x2=-470
    y2=210
    drawline(x1,y1,x2,y2)

    x1=-470
    y1=210
    x2=-430
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-430
    y1=200
    x2=-300
    y2=200
    drawline(x1,y1,x2,y2)

    x1=-300
    y1=200
    x2=-300
    y2=120
    drawline(x1,y1,x2,y2)

    x1=-300
    y1=120
    x2=-430
    y2=120
    drawline(x1,y1,x2,y2)

    x1=-430
    y1=120
    x2=-430
    y2=190
    drawline(x1,y1,x2,y2)

    x1=-430
    y1=190
    x2=-470
    y2=210
    drawline(x1,y1,x2,y2)

    #hospital
    x1=-600
    y1=10
    x2=-480
    y2=10
    drawline(x1,y1,x2,y2)

    x1=-480
    y1=10
    x2=-480
    y2=90
    drawline(x1,y1,x2,y2)

    x1=-480
    y1=90
    x2=-600
    y2=90
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=90
    x2=-600
    y2=10
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=10
    x2=-580
    y2=10
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=10
    x2=-580
    y2=30
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=30
    x2=-570
    y2=30
    drawline(x1,y1,x2,y2)

    x1=-570
    y1=30
    x2=-570
    y2=10
    drawline(x1,y1,x2,y2)

    #hospital window (Sherlock's lab)
    x1=-550
    y1=80
    x2=-530
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-530
    y1=80
    x2=-530
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-530
    y1=60
    x2=-550
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-550
    y1=60
    x2=-550
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-530
    y1=80
    x2=-530
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-530
    y1=60
    x2=-460
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-460
    y1=80
    x2=-360
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-360
    y1=80
    x2=-360
    y2=0
    drawline(x1,y1,x2,y2)

    x1=-360
    y1=0
    x2=-460
    y2=0
    drawline(x1,y1,x2,y2)

    x1=-460
    y1=0
    x2=-460
    y2=70
    drawline(x1,y1,x2,y2)

    x1=-460
    y1=70
    x2=-530
    y2=60
    drawline(x1,y1,x2,y2)

    #boarding school
    x1=-600
    y1=-70
    x2=-480
    y2=-70
    drawline(x1,y1,x2,y2)

    x1=-480
    y1=-70
    x2=-480
    y2=-150
    drawline(x1,y1,x2,y2)

    x1=-480
    y1=-150
    x2=-600
    y2=-150
    drawline(x1,y1,x2,y2)

    x1=-600
    y1=-150
    x2=-600
    y2=-70
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=-150
    x2=-580
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=-130
    x2=-570
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=-570
    y1=-130
    x2=-570
    y2=-150
    drawline(x1,y1,x2,y2)

    #sea shore
    x1=-600
    y1=-300
    x2=-590
    y2=-290
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=-290
    x2=-580
    y2=-270
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=-270
    x2=-570
    y2=-260
    drawline(x1,y1,x2,y2)

    x1=-570
    y1=-260
    x2=-560
    y2=-250
    drawline(x1,y1,x2,y2)

    x1=-560
    y1=-250
    x2=-540
    y2=-245
    drawline(x1,y1,x2,y2)

    x1=-540
    y1=-245
    x2=-520
    y2=-220
    drawline(x1,y1,x2,y2)

    x1=-520
    y1=-220
    x2=-510
    y2=-210
    drawline(x1,y1,x2,y2)

    x1=-510
    y1=-210
    x2=-490
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=-490
    y1=-200
    x2=-480
    y2=-210
    drawline(x1,y1,x2,y2)

    x1=-480
    y1=-210
    x2=-470
    y2=-220
    drawline(x1,y1,x2,y2)

    x1=-470
    y1=-220
    x2=-460
    y2=-225
    drawline(x1,y1,x2,y2)

    x1=-460
    y1=-225
    x2=-455
    y2=-230
    drawline(x1,y1,x2,y2)

    x1=-455
    y1=-230
    x2=-450
    y2=-240
    drawline(x1,y1,x2,y2)

    x1=-450
    y1=-240
    x2=-445
    y2=-245
    drawline(x1,y1,x2,y2)

    x1=-445
    y1=-245
    x2=-445
    y2=-250
    drawline(x1,y1,x2,y2)

    x1=-445
    y1=-250
    x2=-445
    y2=-255
    drawline(x1,y1,x2,y2)

    x1=-445
    y1=-255
    x2=-440
    y2=-255
    drawline(x1,y1,x2,y2)

    x1=-440
    y1=-255
    x2=-435
    y2=-260
    drawline(x1,y1,x2,y2)

    x1=-435
    y1=-260
    x2=-430
    y2=-265
    drawline(x1,y1,x2,y2)

    x1=-430
    y1=-265
    x2=-420
    y2=-265
    drawline(x1,y1,x2,y2)

    x1=-420
    y1=-265
    x2=-420
    y2=-275
    drawline(x1,y1,x2,y2)

    x1=-420
    y1=-275
    x2=-415
    y2=-280
    drawline(x1,y1,x2,y2)

    x1=-415
    y1=-280
    x2=-410
    y2=-285
    drawline(x1,y1,x2,y2)

    x1=-410
    y1=-285
    x2=-405
    y2=-290
    drawline(x1,y1,x2,y2)

    x1=-405
    y1=-290
    x2=-400
    y2=-295
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=-295
    x2=-395
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=-395
    y1=-300
    x2=-400
    y2=-320
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=-320
    x2=-400
    y2=-330
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=-330
    x2=-550
    y2=-330
    drawline(x1,y1,x2,y2)

    x1=-550
    y1=-330
    x2=-600
    y2=-300
    drawline(x1,y1,x2,y2)

    #car
    x1=-540
    y1=-250
    x2=-500
    y2=-250
    drawline(x1,y1,x2,y2)

    x1=-500
    y1=-250
    x2=-500
    y2=-270
    drawline(x1,y1,x2,y2)

    x1=-500
    y1=-270
    x2=-540
    y2=-270
    drawline(x1,y1,x2,y2)

    x1=-540
    y1=-270
    x2=-540
    y2=-250
    drawline(x1,y1,x2,y2)

    x1=-500
    y1=-255
    x2=-490
    y2=-260
    drawline(x1,y1,x2,y2)

    x1=-490
    y1=-260
    x2=-480
    y2=-270
    drawline(x1,y1,x2,y2)

    x1=-480
    y1=-270
    x2=-500
    y2=-270
    drawline(x1,y1,x2,y2)

    x1=-500
    y1=-280
    x2=-500
    y2=-280
    drawline(x1,y1,x2,y2)
    t.circle(5)

    x1=-530
    y1=-280
    x2=-530
    y2=-280
    drawline(x1,y1,x2,y2)
    t.circle(5)

    #police station
    x1=-250
    y1=350
    x2=-150
    y2=350
    drawline(x1,y1,x2,y2)

    x1=-150
    y1=350
    x2=-150
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-150
    y1=250
    x2=-250
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-250
    y1=350
    x2=-250
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-250
    y1=250
    x2=-245
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-245
    y1=250
    x2=-245
    y2=270
    drawline(x1,y1,x2,y2)

    x1=-245
    y1=270
    x2=-235
    y2=270
    drawline(x1,y1,x2,y2)

    x1=-235
    y1=270
    x2=-235
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-230
    y1=300
    x2=-170
    y2=300
    drawline(x1,y1,x2,y2)

    x1=-170
    y1=300
    x2=-170
    y2=340
    drawline(x1,y1,x2,y2)

    x1=-170
    y1=340
    x2=-230
    y2=340
    drawline(x1,y1,x2,y2)

    x1=-230
    y1=340
    x2=-230
    y2=300
    drawline(x1,y1,x2,y2)

    x1=-200
    y1=305
    x2=-200
    y2=305
    drawline(x1,y1,x2,y2)
    t.circle(14)

    #police inspection area
    x1=-150
    y1=330
    x2=-70
    y2=330
    drawline(x1,y1,x2,y2)

    x1=-70
    y1=330
    x2=-70
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-70
    y1=250
    x2=-150
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-150
    y1=250
    x2=-140
    y2=250
    drawline(x1,y1,x2,y2)

    x1=-140
    y1=250
    x2=-140
    y2=270
    drawline(x1,y1,x2,y2)

    x1=-140
    y1=270
    x2=-130
    y2=270
    drawline(x1,y1,x2,y2)

    x1=-130
    y1=270
    x2=-130
    y2=250
    drawline(x1,y1,x2,y2)

    #police cab
    x1=-70
    y1=240
    x2=-20
    y2=240
    drawline(x1,y1,x2,y2)

    x1=-20
    y1=240
    x2=-20
    y2=210
    drawline(x1,y1,x2,y2)

    x1=-20
    y1=210
    x2=-70
    y2=210
    drawline(x1,y1,x2,y2)

    x1=-70
    y1=210
    x2=-70
    y2=240
    drawline(x1,y1,x2,y2)

    x1=-20
    y1=230
    x2=-10
    y2=230
    drawline(x1,y1,x2,y2)

    x1=-10
    y1=230
    x2=0
    y2=210
    drawline(x1,y1,x2,y2)

    x1=0
    y1=210
    x2=-70
    y2=210
    drawline(x1,y1,x2,y2)

    x1=-60
    y1=205
    x2=-60
    y2=205
    drawline(x1,y1,x2,y2)
    t.circle(3)

    x1=-20
    y1=205
    x2=-20
    y2=205
    drawline(x1,y1,x2,y2)
    t.circle(3)

    #court
    x1=50
    y1=300
    x2=100
    y2=350
    drawline(x1,y1,x2,y2)

    x1=100
    y1=350
    x2=150
    y2=300
    drawline(x1,y1,x2,y2)

    x1=150
    y1=300
    x2=50
    y2=300
    drawline(x1,y1,x2,y2)

    x1=70
    y1=300
    x2=70
    y2=250
    drawline(x1,y1,x2,y2)

    x1=70
    y1=250
    x2=130
    y2=250
    drawline(x1,y1,x2,y2)

    x1=130
    y1=250
    x2=130
    y2=300
    drawline(x1,y1,x2,y2)

    x1=110
    y1=250
    x2=110
    y2=270
    drawline(x1,y1,x2,y2)

    x1=110
    y1=270
    x2=90
    y2=270
    drawline(x1,y1,x2,y2)

    x1=90
    y1=270
    x2=90
    y2=250
    drawline(x1,y1,x2,y2)

    #restaurant
    x1=400
    y1=350
    x2=550
    y2=350
    drawline(x1,y1,x2,y2)

    x1=550
    y1=350
    x2=550
    y2=320
    drawline(x1,y1,x2,y2)

    x1=550
    y1=320
    x2=400
    y2=320
    drawline(x1,y1,x2,y2)

    x1=400
    y1=320
    x2=400
    y2=350
    drawline(x1,y1,x2,y2)

    x1=420
    y1=320
    x2=420
    y2=250
    drawline(x1,y1,x2,y2)

    x1=420
    y1=250
    x2=530
    y2=250
    drawline(x1,y1,x2,y2)

    x1=530
    y1=250
    x2=530
    y2=320
    drawline(x1,y1,x2,y2)

    x1=450
    y1=250
    x2=450
    y2=270
    drawline(x1,y1,x2,y2)

    x1=450
    y1=270
    x2=490
    y2=270
    drawline(x1,y1,x2,y2)

    x1=490
    y1=270
    x2=490
    y2=250
    drawline(x1,y1,x2,y2)

    #lauriston's garden
    x1=400
    y1=80
    x2=450
    y2=150
    drawline(x1,y1,x2,y2)

    x1=450
    y1=150
    x2=500
    y2=80
    drawline(x1,y1,x2,y2)

    x1=500
    y1=80
    x2=400
    y2=80
    drawline(x1,y1,x2,y2)

    x1=420
    y1=80
    x2=420
    y2=30
    drawline(x1,y1,x2,y2)

    x1=420
    y1=30
    x2=480
    y2=30
    drawline(x1,y1,x2,y2)

    x1=480
    y1=30
    x2=480
    y2=80
    drawline(x1,y1,x2,y2)

    x1=440
    y1=30
    x2=440
    y2=50
    drawline(x1,y1,x2,y2)

    x1=440
    y1=50
    x2=460
    y2=50
    drawline(x1,y1,x2,y2)

    x1=460
    y1=50
    x2=460
    y2=30
    drawline(x1,y1,x2,y2)

    x1=440
    y1=70
    x2=460
    y2=70
    drawline(x1,y1,x2,y2)

    x1=460
    y1=70
    x2=460
    y2=60
    drawline(x1,y1,x2,y2)

    x1=460
    y1=60
    x2=440
    y2=60
    drawline(x1,y1,x2,y2)

    x1=440
    y1=60
    x2=440
    y2=70
    drawline(x1,y1,x2,y2)

    x1=440
    y1=70
    x2=390
    y2=60
    drawline(x1,y1,x2,y2)

    x1=390
    y1=60
    x2=300
    y2=60
    drawline(x1,y1,x2,y2)

    x1=300
    y1=60
    x2=300
    y2=10
    drawline(x1,y1,x2,y2)

    x1=300
    y1=10
    x2=390
    y2=10
    drawline(x1,y1,x2,y2)

    x1=390
    y1=10
    x2=390
    y2=50
    drawline(x1,y1,x2,y2)

    x1=390
    y1=50
    x2=440
    y2=70
    drawline(x1,y1,x2,y2)

    #journalist house
    x1=460
    y1=-40
    x2=460
    y2=-110
    drawline(x1,y1,x2,y2)

    x1=460
    y1=-110
    x2=550
    y2=-110
    drawline(x1,y1,x2,y2)

    x1=550
    y1=-110
    x2=550
    y2=-40
    drawline(x1,y1,x2,y2)

    x1=550
    y1=-40
    x2=440
    y2=-40
    drawline(x1,y1,x2,y2)

    x1=440
    y1=-40
    x2=440
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=440
    y1=-20
    x2=570
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=570
    y1=-20
    x2=570
    y2=-40
    drawline(x1,y1,x2,y2)

    x1=570
    y1=-40
    x2=550
    y2=-40
    drawline(x1,y1,x2,y2)

    #Mrs Price house
    x1=400
    y1=-300
    x2=550
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=550
    y1=-300
    x2=550
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=550
    y1=-200
    x2=400
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=400
    y1=-200
    x2=400
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=400
    y1=-300
    x2=410
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=410
    y1=-300
    x2=410
    y2=-280
    drawline(x1,y1,x2,y2)

    x1=410
    y1=-280
    x2=420
    y2=-280
    drawline(x1,y1,x2,y2)

    x1=420
    y1=-280
    x2=420
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=400
    y1=-200
    x2=390
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=390
    y1=-200
    x2=470
    y2=-180
    drawline(x1,y1,x2,y2)

    x1=470
    y1=-180
    x2=560
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=560
    y1=-200
    x2=550
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=440
    y1=-260
    x2=510
    y2=-260
    drawline(x1,y1,x2,y2)

    x1=510
    y1=-260
    x2=510
    y2=-220
    drawline(x1,y1,x2,y2)

    x1=510
    y1=-220
    x2=440
    y2=-220
    drawline(x1,y1,x2,y2)

    x1=440
    y1=-220
    x2=440
    y2=-260
    drawline(x1,y1,x2,y2)

    #ware house
    x1=150
    y1=-300
    x2=300
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=300
    y1=-300
    x2=300
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=300
    y1=-200
    x2=150
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=150
    y1=-200
    x2=150
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=160
    y1=-300
    x2=160
    y2=-280
    drawline(x1,y1,x2,y2)

    x1=160
    y1=-280
    x2=170
    y2=-280
    drawline(x1,y1,x2,y2)

    x1=170
    y1=-280
    x2=170
    y2=-300
    drawline(x1,y1,x2,y2)

    #janus cars
    x1=-150
    y1=-300
    x2=-30
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=-30
    y1=-300
    x2=-30
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=-30
    y1=-200
    x2=-150
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=-150
    y1=-200
    x2=-150
    y2=-300
    drawline(x1,y1,x2,y2)

    x1=-120
    y1=-300
    x2=-120
    y2=-280
    drawline(x1,y1,x2,y2)

    x1=-120
    y1=-280
    x2=-110
    y2=-280
    drawline(x1,y1,x2,y2)

    x1=-110
    y1=-280
    x2=-110
    y2=-300
    drawline(x1,y1,x2,y2)

    #swimming pool
    x1=100
    y1=-100
    x2=200
    y2=-100
    drawline(x1,y1,x2,y2)

    x1=200
    y1=-100
    x2=200
    y2=-50
    drawline(x1,y1,x2,y2)

    x1=200
    y1=-50
    x2=100
    y2=-50
    drawline(x1,y1,x2,y2)

    x1=100
    y1=-50
    x2=100
    y2=-100
    drawline(x1,y1,x2,y2)

    #high building for final fight
    x1=100
    y1=20
    x2=120
    y2=120
    drawline(x1,y1,x2,y2)

    x1=120
    y1=120
    x2=140
    y2=130
    drawline(x1,y1,x2,y2)

    x1=140
    y1=130
    x2=160
    y2=120
    drawline(x1,y1,x2,y2)

    x1=160
    y1=120
    x2=180
    y2=20
    drawline(x1,y1,x2,y2)

    x1=180
    y1=20
    x2=160
    y2=10
    drawline(x1,y1,x2,y2)

    x1=160
    y1=10
    x2=100
    y2=20
    drawline(x1,y1,x2,y2)

    x1=140
    y1=130
    x2=160
    y2=10
    drawline(x1,y1,x2,y2)

    x1=120
    y1=16
    x2=120
    y2=36
    drawline(x1,y1,x2,y2)

    x1=120
    y1=36
    x2=130
    y2=35
    drawline(x1,y1,x2,y2)

    x1=130
    y1=35
    x2=130
    y2=16
    drawline(x1,y1,x2,y2)

    #college building
    x1=-180
    y1=0
    x2=-80
    y2=0
    drawline(x1,y1,x2,y2)

    x1=-80
    y1=0
    x2=-80
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-80
    y1=80
    x2=-180
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-180
    y1=80
    x2=-180
    y2=0
    drawline(x1,y1,x2,y2)

    x1=-180
    y1=0
    x2=-160
    y2=0
    drawline(x1,y1,x2,y2)

    x1=-160
    y1=0
    x2=-160
    y2=20
    drawline(x1,y1,x2,y2)

    x1=-160
    y1=20
    x2=-150
    y2=20
    drawline(x1,y1,x2,y2)

    x1=-150
    y1=20
    x2=-150
    y2=0
    drawline(x1,y1,x2,y2)

    x1=-140
    y1=40
    x2=-120
    y2=40
    drawline(x1,y1,x2,y2)

    x1=-120
    y1=40
    x2=-120
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-120
    y1=60
    x2=-140
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-140
    y1=60
    x2=-140
    y2=40
    drawline(x1,y1,x2,y2)

    x1=-120
    y1=40
    x2=-70
    y2=50
    drawline(x1,y1,x2,y2)

    x1=-70
    y1=50
    x2=10
    y2=50
    drawline(x1,y1,x2,y2)

    x1=10
    y1=50
    x2=10
    y2=100
    drawline(x1,y1,x2,y2)

    x1=10
    y1=100
    x2=-70
    y2=100
    drawline(x1,y1,x2,y2)

    x1=-70
    y1=100
    x2=-70
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-70
    y1=60
    x2=-120
    y2=40
    drawline(x1,y1,x2,y2)

    #london tower
    x1=-350
    y1=-150
    x2=-250
    y2=-150
    drawline(x1,y1,x2,y2)

    x1=-250
    y1=-150
    x2=-250
    y2=-100
    drawline(x1,y1,x2,y2)

    x1=-250
    y1=-100
    x2=-350
    y2=-100
    drawline(x1,y1,x2,y2)

    x1=-350
    y1=-100
    x2=-350
    y2=-150
    drawline(x1,y1,x2,y2)

    x1=-330
    y1=-150
    x2=-330
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=-330
    y1=-130
    x2=-320
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=-320
    y1=-130
    x2=-320
    y2=-150
    drawline(x1,y1,x2,y2)

    #roads
    x1=-700
    y1=140
    x2=-590
    y2=140
    drawline(x1,y1,x2,y2)

    x1=-590
    y1=140
    x2=-590
    y2=145
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=145
    x2=-580
    y2=140
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=140
    x2=-430
    y2=140
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=200
    x2=-400
    y2=280
    drawline(x1,y1,x2,y2)

    x1=-370
    y1=280
    x2=-370
    y2=205
    drawline(x1,y1,x2,y2)

    x1=-370
    y1=205
    x2=-245
    y2=205
    drawline(x1,y1,x2,y2)

    x1=-245
    y1=205
    x2=-245
    y2=245
    drawline(x1,y1,x2,y2)

    x1=-235
    y1=245
    x2=-235
    y2=205
    drawline(x1,y1,x2,y2)

    x1=-235
    y1=205
    x2=90
    y2=205
    drawline(x1,y1,x2,y2)

    x1=90
    y1=205
    x2=90
    y2=245
    drawline(x1,y1,x2,y2)

    x1=110
    y1=245
    x2=110
    y2=205
    drawline(x1,y1,x2,y2)

    x1=110
    y1=205
    x2=450
    y2=205
    drawline(x1,y1,x2,y2)

    x1=450
    y1=205
    x2=450
    y2=245
    drawline(x1,y1,x2,y2)

    x1=490
    y1=245
    x2=490
    y2=205
    drawline(x1,y1,x2,y2)

    x1=490
    y1=205
    x2=700
    y2=205
    drawline(x1,y1,x2,y2)

    x1=700
    y1=160
    x2=350
    y2=160
    drawline(x1,y1,x2,y2)

    x1=350
    y1=160
    x2=350
    y2=60
    drawline(x1,y1,x2,y2)

    x1=390
    y1=20
    x2=440
    y2=20
    drawline(x1,y1,x2,y2)

    x1=440
    y1=20
    x2=440
    y2=25
    drawline(x1,y1,x2,y2)

    x1=460
    y1=25
    x2=460
    y2=20
    drawline(x1,y1,x2,y2)

    x1=460
    y1=20
    x2=520
    y2=20
    drawline(x1,y1,x2,y2)

    x1=520
    y1=20
    x2=520
    y2=25
    drawline(x1,y1,x2,y2)

    x1=560
    y1=25
    x2=560
    y2=20
    drawline(x1,y1,x2,y2)

    x1=560
    y1=20
    x2=700
    y2=20
    drawline(x1,y1,x2,y2)

    x1=-700
    y1=100
    x2=-400
    y2=100
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=100
    x2=-400
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=0
    x2=-400
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=-20
    x2=-570
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=-570
    y1=-20
    x2=-570
    y2=-5
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=-5
    x2=-580
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=-20
    x2=-700
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=-700
    y1=-50
    x2=-400
    y2=-50
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=-50
    x2=-400
    y2=-170
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=-170
    x2=-570
    y2=-170
    drawline(x1,y1,x2,y2)

    x1=-570
    y1=-170
    x2=-570
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=-160
    x2=-580
    y2=-170
    drawline(x1,y1,x2,y2)

    x1=-580
    y1=-170
    x2=-700
    y2=-170
    drawline(x1,y1,x2,y2)

    x1=-700
    y1=-200
    x2=-400
    y2=-200
    drawline(x1,y1,x2,y2)

    x1=-400
    y1=-200
    x2=-350
    y2=-340
    drawline(x1,y1,x2,y2)

    x1=-350
    y1=-340
    x2=650
    y2=-340
    drawline(x1,y1,x2,y2)

    x1=650
    y1=-340
    x2=650
    y2=-10
    drawline(x1,y1,x2,y2)

    x1=650
    y1=-10
    x2=700
    y2=-10
    drawline(x1,y1,x2,y2)

    x1=-300
    y1=170
    x2=20
    y2=170
    drawline(x1,y1,x2,y2)

    x1=20
    y1=170
    x2=20
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=20
    y1=-20
    x2=-150
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=-150
    y1=-20
    x2=-150
    y2=-15
    drawline(x1,y1,x2,y2)

    x1=-160
    y1=-15
    x2=-160
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=-160
    y1=-20
    x2=-370
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=-370
    y1=-20
    x2=-370
    y2=0
    drawline(x1,y1,x2,y2)

    x1=-370
    y1=80
    x2=-370
    y2=120
    drawline(x1,y1,x2,y2)

    x1=60
    y1=160
    x2=310
    y2=160
    drawline(x1,y1,x2,y2)

    x1=310
    y1=160
    x2=310
    y2=60
    drawline(x1,y1,x2,y2)

    x1=310
    y1=10
    x2=310
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=310
    y1=-20
    x2=130
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=130
    y1=-20
    x2=130
    y2=0
    drawline(x1,y1,x2,y2)

    x1=120
    y1=0
    x2=120
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=120
    y1=-20
    x2=60
    y2=-20
    drawline(x1,y1,x2,y2)

    x1=60
    y1=-20
    x2=60
    y2=160
    drawline(x1,y1,x2,y2)

    x1=-370
    y1=-50
    x2=20
    y2=-50
    drawline(x1,y1,x2,y2)

    x1=20
    y1=-50
    x2=20
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=20
    y1=-160
    x2=-320
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=-320
    y1=-160
    x2=-320
    y2=-155
    drawline(x1,y1,x2,y2)

    x1=-330
    y1=-155
    x2=-330
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=-330
    y1=-160
    x2=-365
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=-365
    y1=-160
    x2=-365
    y2=-50
    drawline(x1,y1,x2,y2)

    x1=60
    y1=-45
    x2=310
    y2=-45
    drawline(x1,y1,x2,y2)

    x1=310
    y1=-45
    x2=310
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=310
    y1=-160
    x2=60
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=60
    y1=-160
    x2=60
    y2=-45
    drawline(x1,y1,x2,y2)

    x1=350
    y1=-10
    x2=610
    y2=-10
    drawline(x1,y1,x2,y2)

    x1=610
    y1=-10
    x2=610
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=610
    y1=-130
    x2=520
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=520
    y1=-130
    x2=520
    y2=-120
    drawline(x1,y1,x2,y2)

    x1=510
    y1=-120
    x2=510
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=510
    y1=-130
    x2=350
    y2=-130
    drawline(x1,y1,x2,y2)

    x1=350
    y1=-130
    x2=350
    y2=-10
    drawline(x1,y1,x2,y2)

    x1=350
    y1=-160
    x2=610
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=610
    y1=-160
    x2=610
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=610
    y1=-310
    x2=425
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=425
    y1=-310
    x2=425
    y2=-305
    drawline(x1,y1,x2,y2)

    x1=415
    y1=-305
    x2=415
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=415
    y1=-310
    x2=350
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=350
    y1=-310
    x2=350
    y2=-160
    drawline(x1,y1,x2,y2)

    x1=310
    y1=-190
    x2=70
    y2=-190
    drawline(x1,y1,x2,y2)

    x1=70
    y1=-190
    x2=70
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=70
    y1=-310
    x2=160
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=160
    y1=-310
    x2=160
    y2=-305
    drawline(x1,y1,x2,y2)

    x1=170
    y1=-305
    x2=170
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=170
    y1=-310
    x2=310
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=310
    y1=-310
    x2=310
    y2=-190
    drawline(x1,y1,x2,y2)

    x1=20
    y1=-190
    x2=-360
    y2=-190
    drawline(x1,y1,x2,y2)

    x1=-360
    y1=-190
    x2=-320
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=-320
    y1=-310
    x2=-120
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=-120
    y1=-310
    x2=-120
    y2=-305
    drawline(x1,y1,x2,y2)

    x1=-110
    y1=-305
    x2=-110
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=-110
    y1=-310
    x2=20
    y2=-310
    drawline(x1,y1,x2,y2)

    x1=20
    y1=-310
    x2=20
    y2=-190
    drawline(x1,y1,x2,y2)

    #hostage car
    x1=-300
    y1=80
    x2=-250
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-250
    y1=80
    x2=-240
    y2=70
    drawline(x1,y1,x2,y2)

    x1=-240
    y1=70
    x2=-220
    y2=70
    drawline(x1,y1,x2,y2)

    x1=-220
    y1=70
    x2=-220
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-220
    y1=60
    x2=-330
    y2=60
    drawline(x1,y1,x2,y2)

    x1=-330
    y1=60
    x2=-330
    y2=70
    drawline(x1,y1,x2,y2)

    x1=-330
    y1=70
    x2=-310
    y2=70
    drawline(x1,y1,x2,y2)

    x1=-310
    y1=70
    x2=-300
    y2=80
    drawline(x1,y1,x2,y2)

    x1=-300
    y1=50
    x2=-300
    y2=50
    drawline(x1,y1,x2,y2)
    t.circle(5)

    x1=-250
    y1=50
    x2=-250
    y2=50
    drawline(x1,y1,x2,y2)
    t.circle(5)

    x1=-600
    y1=300
    x2=-600
    y2=300
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("221 Bakers Street")

    x1=-587
    y1=150
    x2=-587
    y2=150
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("A")

    x1=-587
    y1=200
    x2=-587
    y2=200
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("B")

    x1=-587
    y1=250
    x2=-587
    y2=250
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("C")

    x1=-400
    y1=300
    x2=-400
    y2=300
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("shoes")

    x1=-400
    y1=150
    x2=-400
    y2=150
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("sofa")

    x1=-360
    y1=150
    x2=-360
    y2=150
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("sofa")

    x1=-380
    y1=170
    x2=-380
    y2=170
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("chair")

    x1=-230
    y1=280
    x2=-230
    y2=280
    drawline(x1,y1,x2,y2)
    t.color("blue")
    t.write("Police Station")

    x1=-150
    y1=310
    x2=-150
    y2=310
    drawline(x1,y1,x2,y2)
    t.color("blue")
    t.write("Police Inspection")

    x1=80
    y1=310
    x2=80
    y2=310
    drawline(x1,y1,x2,y2)
    t.color("grey")
    t.write("Court")

    x1=450
    y1=330
    x2=450
    y2=330
    drawline(x1,y1,x2,y2)
    t.color("orange")
    t.write("Restaurant")

    x1=355
    y1=140
    x2=355
    y2=140
    drawline(x1,y1,x2,y2)
    t.color("purple")
    t.write("Lauriston's Garden")

    x1=550
    y1=140
    x2=550
    y2=140
    drawline(x1,y1,x2,y2)
    t.color("green")
    t.write("Plants")

    x1=600
    y1=110
    x2=600
    y2=110
    drawline(x1,y1,x2,y2)
    t.color("green")
    t.write("Garbage Bin")

    x1=500
    y1=90
    x2=500
    y2=90
    drawline(x1,y1,x2,y2)
    t.color("green")
    t.write("Gutter")

    x1=310
    y1=20
    x2=310
    y2=20
    drawline(x1,y1,x2,y2)
    t.color("maroon")
    t.write("Jennifer's body")

    x1=460
    y1=-40
    x2=460
    y2=-40
    drawline(x1,y1,x2,y2)
    t.color("pink")
    t.write("Journalist House")

    x1=430
    y1=-180
    x2=430
    y2=-180
    drawline(x1,y1,x2,y2)
    t.color("brown")
    t.write("Mrs. Prince House")

    x1=200
    y1=-220
    x2=200
    y2=-220
    drawline(x1,y1,x2,y2)
    t.color("yellow")
    t.write("Ware House")

    x1=120
    y1=-80
    x2=120
    y2=-80
    drawline(x1,y1,x2,y2)
    t.color("blue")
    t.write("Swimming pool")

    x1=120
    y1=140
    x2=120
    y2=140
    drawline(x1,y1,x2,y2)
    t.color("red")
    t.write("High Building for Final Fight")

    x1=-170
    y1=80
    x2=-170
    y2=80
    drawline(x1,y1,x2,y2)
    t.color("orange")
    t.write("College Building")

    x1=-60
    y1=70
    x2=-60
    y2=70
    drawline(x1,y1,x2,y2)
    t.color("green")
    t.write("Identical pills")

    x1=-300
    y1=80
    x2=-300
    y2=80
    drawline(x1,y1,x2,y2)
    t.color("brown")
    t.write("Hostage car")

    x1=-340
    y1=-120
    x2=-340
    y2=-120
    drawline(x1,y1,x2,y2)
    t.color("brown")
    t.write("London Tower")

    x1=-130
    y1=-240
    x2=-130
    y2=-240
    drawline(x1,y1,x2,y2)
    t.color("grey")
    t.write("Janus Cars")

    x1=-570
    y1=-300
    x2=-570
    y2=-300
    drawline(x1,y1,x2,y2)
    t.color("blue")
    t.write("Seashore")

    x1=-590
    y1=-100
    x2=-590
    y2=-100
    drawline(x1,y1,x2,y2)
    t.color("purple")
    t.write("Boarding School")

    x1=-590
    y1=40
    x2=-590
    y2=40
    drawline(x1,y1,x2,y2)
    t.color("blue")
    t.write("Hospital")

    x1=-450
    y1=50
    x2=-450
    y2=50
    drawline(x1,y1,x2,y2)
    t.color("green")
    t.write("Sherlock's lab")

    t.done()

def space(): #AHMED ASHRAF SP18-BSE-009
    print("\n")
def invalid(): #AHMED ASHRAF SP18-BSE-009
    print("TRY ANOTHER COMMAND ")

#AHMED ASHRAF SP18-BSE-009
def slowprint(message, speed):    #using for printing the string slowly
    for x in range(0, len(message)):     
        if x ==  len(message)-1:
            print(message[x])
        else:
            print(message[x], end="")
            sys.stdout.flush()
            time.sleep(speed)

def final1():
    while True:
        zx=open("ali\\final.txt","r")
        slowprint(zx.read(),0.04)
        zx.close()
        time.sleep(2)
        space()
        space()
        zz=open("ali\\final1.txt","r")
        slowprint(zz.read(),0.04)
        zz.close()
        time.sleep(2)
        space()
        space()
        za=open("ali\\final2.txt","r")
        slowprint(za.read(),0.04)
        za.close()
        time.sleep(2)
        space()
        space()
        zc=open("ali\\final3.txt","r")
        slowprint(zc.read(),0.04)
        zc.close()
        time.sleep(2)
        space()
        space()
        zv=open("ali\\final4.txt","r")
        slowprint(zv.read(),0.04)
        zv.close()
        time.sleep(2)
        space()
        space()
        zs=open("ali\\final5.txt","r")
        slowprint(zs.read(),0.04)
        zs.close()
        time.sleep(2)
        space()
        space()
        while True:
            j=input("Do you want to jump?")
            j=j.lower()
            if 'yes' in j:
                zl=open("ali\\final6.txt","r")
                slowprint(zl.read(),0.04)
                zl.close()
                time.sleep(2)
                space()
                space()
            elif 'no' in j:
                ze=open("ali\\final7.txt","r")
                slowprint(ze.read(),0.04)
                ze.close()
                time.sleep(2)
                space()
                space()
            elif "map" in j:
                map()
                space()
                continue
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue

def final():
    while True:
        f=input("Do you want to fight Jim...??")
        f=f.lower()
        if 'fight' in f or 'yes' in f:
            dd=open("ali\\fighta.txt","r")
            slowprint(dd.read(),0.04)
            dd.close()
            time.sleep(2)
            space()
            space()
            final1()
        elif 'dont' in f or 'no' in f or "don't" in f:
            dc=open("ali\\fighta1.txt","r")
            slowprint(dc.read(),0.04)
            dc.close()
            time.sleep(2)
            space()
            space()
            final1()
        elif "map" in f:
            map()
            space()
            continue
        else:
            invalid()
            time.sleep(2)
            space()
            space()
            continue
            

def kitty():
    while True:
        aa=open("ali\\kitty.txt","r")
        slowprint(aa.read(),0.04)
        aa.close()
        time.sleep(2)
        space()
        space()
        bb=open("ali\\kitty2.txt","r")
        slowprint(bb.read(),0.04)
        bb.close()
        time.sleep(2)
        space()
        space()
        while True:
            z=input("Do you want to talk to Jim??")
            z=z.lower()
            if 'yes' in z:
                gg=open("ali\\kitty3.txt","r")
                slowprint(gg.read(),0.04)
                gg.close()
                time.sleep(2)
                space()
                space()
                while True:
                    hb=open("ali\\kitty4.txt","r")
                    slowprint(hb.read(),0.04)
                    hb.close()
                    time.sleep(2)
                    space()
                    space()
                    ee=open("ali\\kitty5.txt","r")
                    slowprint(ee.read(),0.04)
                    ee.close()
                    time.sleep(2)
                    space()
                    space()
                    while True:
                        gd=open("ali\\dr.txt","r")
                        slowprint(gd.read(),0.04)
                        gd.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            w=input("Do you want to Talk with sherlock?")
                            w=w.lower()
                            if 'yes' in w:
                                qq=open("ali\\dr1.txt","r")
                                slowprint(qq.read(),0.04)
                                qq.close()
                                time.sleep(2)
                                space()
                                space()
                                while True:
                                    bc=open("ali\\dr3.txt","r")
                                    slowprint(bc.read(),0.04)
                                    bc.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    sl=open("ali\\dr4.txt","r")
                                    slowprint(sl.read(),0.04)
                                    sl.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    while True:
                                        vv=open("ali\\dr5.txt","r")
                                        slowprint(vv.read(),0.04)
                                        vv.close()
                                        time.sleep(2)
                                        space()
                                        space()
                                        t=input("What to do now:?")
                                        t=t.lower()
                                        if 'chat' in t or 'talk' in t:
                                            vz=open("ali\\jump.txt","r")
                                            slowprint(vz.read(),0.04)
                                            vz.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            final()
                                            
                                        
                                        
                                        elif 'walk' in t or 'around' in t:
                                            mq=open("ali\\jump1.txt","r")
                                            slowprint(mq.read(),0.04)
                                            mq.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            final()
                                    
                                            
                                        elif "map" in t:
                                            map()
                                            space()
                                            continue
                                        
                                        else:
                                            invalid()
                                            time.sleep(2)
                                            space()
                                            space()
                                    
                            elif 'no' in w :
                                wr=open("ali\\dr2.txt","r")
                                slowprint(wr.read(),0.04)
                                wr.close()
                                time.sleep(2)
                                space()
                                space()
                            elif "map" in w:
                                map()
                                space()
                                continue
                            else:
                                invalid()
                                timesleep(2)
                                space()
                                space()
                                continue
            elif 'no' in z:
                    ss=open("ali\\kitty8.txt","r")
                    slowprint(ss.read(),0.04)
                    ss.close()
                    time.sleep(2)
                    space()
                    space()
                    kitty()
                
            elif "map" in z:
                    map()
                    space()
                    continue
            else:
                    invalid()
                    time.sleep(2)
                    space()
                    space()
                    continue
            
def run():
    while True:
        az=open("ali\\run.txt","r")
        slowprint(az.read(),0.04)
        az.close()
        time.sleep(2)
        space()
        space()
        aa=open("ali\\run1.txt","r")
        slowprint(aa.read(),0.04)
        aa.close()
        time.sleep(2)
        space()
        space()
        while True:
            l=input("Do you want sherlock to run?")
            l=l.lower()
            if 'yes' in l or 'run' in l:
                hh=open("ali\\run2.txt","r")
                slowprint(hh.read(),0.04)
                hh.close()
                time.sleep(2)
                space()
                space()
                while True:
                    f=input("What to do Now")
                    f=f.lower()
                    if 'go' in f or 'walk' in  f or 'home' in f:
                        nb=open("ali\\home.txt","r")
                        slowprint(nb.read(),0.04)
                        nb.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            cc=open("ali\\sad.txt","r")
                            slowprint(cc.read(),0.04)
                            cc.close()
                            time.sleep(2)
                            space()
                            space()
                            c=input("Do you want to take the money")
                            c=c.lower()
                            if 'yes' in c:
                                az=open("ali\\home1.txt","r")
                                slowprint(az.read(),0.04)
                                az.close()
                                time.sleep(2)
                                space()
                                space()
                                while True:
                                    rr=open("ali\\hell.txt","r")
                                    slowprint(rr.close(),0.04)
                                    rr.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    pp=open("ali\\hell1.txt","r")
                                    slowprint(pp.close(),0.04)
                                    pp.close()
                                    time.sleep(2)
                                    space()
                                    space()
                                    while True:
                                        y=input("Break-in or ring the bell?")
                                        if 'break' in y:
                                            la=open("ali\\hell2.txt","r")
                                            slowprint(la.close(),0.04)
                                            la.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            kitty()
                                        elif 'ring' in y or 'bell' in y:
                                            vv=open("ali\\hell3.txt","r")
                                            slowprint(vv.read(),0.04)
                                            vv.close()
                                            time.sleep(2)
                                            space()
                                            space()
                                            kitty()
                                        elif "map" in y:
                                            map()
                                            space()
                                            continue
                                        else:
                                            invalid()
                                            time.sleep(2)
                                            space()
                                            space()
                                            continue
                                            
                                        
                            elif 'no' in c:
                                dd=open("ali\\home2.txt","r")
                                slowprint(dd.close(),0.04)
                                dd.close()
                                time.sleep(2)
                                space()
                                space()
                            elif "map" in c:
                                map()
                                space()
                                continue
                            else:
                                invalid()
                                time.sleep(2)
                                space()
                                space()
                                continue
                    
                    
                    
            elif 'no' in l or 'dont' in l or "don't" in l:
                mn=open("ali\\run3.txt","r")
                slowprint(mn.read(),0.04)
                mn.close()
                time.sleep(2)
                space()
                space()
                
            elif "map" in l:
                map()
                space()
                continue
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue
def arrest():
    while True:
        ff=open("ali\\arrest.txt","r")
        slowprint(ff.read(),0.04)
        ff.close()
        time.sleep(2)
        space()
        space()
        while True:
            w=input("What to do now?:")
            w=w.lower()
            if 'go' in w:
                dd=open("ali\\arrest1.txt","r")
                slowprint(dd.read(),0.04)
                dd.close()
                time.sleep(2)
                space()
                space()
            elif "map" in w:
                map()
                space()
                continue
            elif 'dont' in w or "don't" in w:
                ds=open("ali\\arrest2.txt","r")
                slowprint(ds.read(),0.04)
                ds.close()
                space()
                space()
                aa=open("ali\\arrest4.txt","r")
                slowprint(aa.read(),0.04)
                aa.close()
                time.sleep(2)
                space()
                space()
                while True:
                    po=open("ali\\arrest5.txt","r")
                    slowprint(po.read(),0.04)
                    po.close()
                    time.sleep(2)
                    space()
                    space()
                    ll=open("ali\\arrest6.txt","r")
                    slowprint(ll.read(),0.04)
                    ll.close()
                    time.sleep(2)
                    space()
                    space()
                    k=input("Fight the police man..??")
                    k=k.lower()
                    if 'yes' in k or 'fight' in k:
                        jj=open("ali\\fight.txt","r")
                        slowprint(jj.read(),0.04)
                        jj.close()
                        time.sleep(2)
                        space()
                        space()
                        nn=open("ali\\fight2.txt","r")
                        slowprint(nn.read(),0.04)
                        nn.close()
                        time.sleep(2)
                        space()
                        space()
                        run()
                    elif 'no' in k or 'not' in k or 'dont' in k or "dont't" in k:
                        mm=open("ali\\fight1.txt","r")
                        slowprint(mm.read(),0.04)
                        mm.close()
                        time.sleep(2)
                        space()
                        space()
                        run()
                    elif "map" in k:
                        map()
                        space()
                        continue
                    else:
                        invalid()
                        time.sleep(2)
                        space()
                        space()
                        continue    
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                
def kidnap2():
    while True:
        az=open("ali\\sally.txt","r")
        slowprint(az.read(),0.04)
        az.close()
        time.sleep(2)
        space()
        space()
        aq=open("ali\\sally2.txt","r")
        slowprint(aq.read(),0.04)
        aq.close()
        time.sleep(2)
        space()
        space()
        af=open("ali\\sally3.txt","r")
        slowprint(af.read(),0.04)
        af.close()
        time.sleep(2)
        space()
        space()
        while True:
            o=input("Do you want to open the door?:")
            if 'yes' in o:
                rr=open("ali\\sally4.txt","r")
                slowprint(rr.read(),0.04)
                rr.close()
                time.sleep(2)
                space()
                space()
                arrest()
            elif 'no' in o:
                ew=open("ali\\sally5.txt","r")
                slowprint(ew.read(),0.04)
                ew.close()
                time.sleep(2)
                space()
                space()
                rr=open("ali\\sally6.txt","r")
                slowprint(rr.read(),0.04)
                rr.close()
                time.sleep(2)
                space()
                space()
                arrest()
            elif "map" in o:
                map()
                space()
                continue
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue
      
def addlestone():
    while True:
        df=open("ali\\addle.txt","r")
        slowprint(df.read(),0.03)
        df.close()
        time.sleep(2)
        space()
        space()
        while True:
            gg=open("ali\\addle2.txt","r")
            slowprint(gg.read(),0.03)
            gg.close()
            time.sleep(2)
            space()
            space()
            gq=open("ali\\addle3.txt","r")
            slowprint(gq.read(),0.03)
            gq.close()
            time.sleep(2)
            space()
            space()
            dd=open("ali\\taxi1.txt","r")
            slowprint(dd.read(),0.03)
            dd.close()
            time.sleep(2)
            space()
            space()
            while True:
                v=input("Aren't you feeling Hungry...!!!??")
                v=v.lower()  
                if 'yes' in v or 'hungary' in v or 'starving' in v:
                    bb=open("ali\\rest.txt","r")
                    slowprint(bb.read(),0.03)
                    bb.close()
                    time.sleep(2)
                    space()
                    space()
                    while True:
                        zz=open("ali\\rest2.txt","r")
                        slowprint(zz.read(),0.04)
                        zz.close()
                        time.sleep(2)
                        space()
                        space()
                        kidnap2()
                elif 'no' in v or 'not' in v:
                    cc=open("ali\\rest1.txt","r")
                    slowprint(cc.read(),0.03)
                    cc.close()
                    time.sleep(2)
                    space()
                    space()
                    oo=open("ali\\rest3.txt","r")
                    slowprint(oo.read(),0.04)
                    oo.close()
                    time.sleep(2)
                    space()
                    space()
                    kidnap2()
                elif "map" in v:
                    map()
                    space()
                    continue
                else:
                    space()
                    invalid()
                    time.sleep(2)
                    space()
                    space()
                    continue
                    
def kidnapping():
    while True:
        qa=open("ali\\kidnap.txt","r")
        slowprint(qa.read(),0.03)
        qa.close()
        time.sleep(2)
        space()
        space()
        while True:
            q=input("Do you Want Dr. John to open it..??")
            if 'yes' in q or 'want' in q:
                sd=open("ali\\open.txt","r")
                slowprint(sd.read(),0.03)
                sd.close()
                time.sleep(2)
                space()
                space()
                while True:
                        qq=open("ali\\kid1.txt","r")
                        slowprint(qq.read(),0.03)
                        qq.close()
                        time.sleep(2)
                        space()
                        space()
                        er=open("ali\\asd.txt","r")
                        slowprint(er.read(),0.03)
                        er.close()
                        time.sleep(2)
                        space()
                        space()
                        az=open("ali\\kid2.txt","r")
                        slowprint(az.read(),0.03)
                        az.close()
                        time.sleep(2)
                        space()
                        space()
                        gg=open("ali\\kid3.txt","r")
                        slowprint(gg.read(),0.03)
                        gg.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            d=input("Do you Want to Sherlock to search the place?")
                            d=d.lower()
                            if 'yes' in d or 'sure' in d or 'why not' in d or 'search' in d or 'examine' in d:
                                we=open("ali\\search1.txt","r")
                                slowprint(we.read(),0.03)
                                we.close()
                                time.sleep(2)
                                space()
                                space()
                                ty=open("ali\\search2.txt","r")
                                slowprint(ty.read(),0.03)
                                ty.close()
                                time.sleep(2)
                                space()
                                space()
                                ee=open("ali\\search3.txt","r")
                                slowprint(ee.read(),0.03)
                                ee.close()
                                time.sleep(2)
                                space()
                                space()
                                pp=open("ali\\search4.txt","r")
                                slowprint(pp.read(),0.03)
                                pp.close()
                                time.sleep(2)
                                space()
                                space()
                                kk=open("ali\\search5.txt","r")
                                slowprint(kk.read(),0.03)
                                kk.close()
                                time.sleep(2)
                                space()
                                space()
                                mm=open("ali\\search6.txt","r")
                                slowprint(mm.read(),0.03)
                                mm.close()
                                time.sleep(2)
                                space()
                                space()
                                xx=open("ali\\search7.txt","r")
                                slowprint(xx.read(),0.03)
                                xx.close()
                                time.sleep(2)
                                space()
                                space()
                                cc=open("ali\\search8.txt","r")
                                slowprint(cc.read(),0.03)
                                cc.close()
                                time.sleep(2)
                                space()
                                space()
                                while True:
                                    h=input("Do you Want Sherlock To pick wooden pieces??")
                                    h=h.lower()
                                    if 'yes' in h or "pick" in h:
                                        hg=open("ali\\search9.txt","r")
                                        slowprint(hg.read(),0.03)
                                        hg.close()
                                        time.sleep(2)
                                        space()
                                        space()
                                        addlestone()
                                    elif 'no' in h:
                                        jn=open("ali\\search10.txt","r")
                                        slowprint(jn.read(),0.03)
                                        jn.close()
                                        time.sleep(2)
                                        space()
                                        space()
                                        addlestone()
                                    elif "map" in h:
                                        map()
                                        space()
                                        continue
                                    else:
                                        space()
                                        invalid()
                                        space()
                                        time.sleep(1)
                            elif 'no' in d or 'dont' in d or "don't" in d:
                                df=open("ali\\walks1.txt","r")
                                slowprint(df.read(),0.03)
                                df.close()
                                time.sleep(2)
                                space()
                                space()
                            elif "map" in d:
                                map()
                                space()
                                continue
                            else:
                                invalid()
                                time.sleep(2)
                                space()
                                space()
                                continue
def jim_mor():
    while True:
        ad=open("ali\\bribe.txt","r")
        slowprint(ad.read(),0.03)
        ad.close()
        time.sleep(2)
        space()
        space()
        while True:
            ff=open("ali\\2mon.txt","r")
            slowprint(ff.read(),0.03)
            ff.close()
            time.sleep(2)
            space()
            space()
            while True:
                aw=open("ali\\mycroft.txt","r")
                slowprint(aw.read(),0.03)
                aw.close()
                time.sleep(2)
                space()
                space()
                while True:
                    a=input("Do you want Dr. John to go??")
                    a=a.lower()
                    if 'yes' in a or 'sure' in a or 'want' in a:
                        fg=open("ali\\myc2.txt","r")
                        slowprint(fg.read(),0.03)
                        fg.close()
                        time.sleep(2)
                        space()
                        space()
                        kl=open("ali\\myc3.txt","r")
                        slowprint(kl.read(),0.03)
                        kl.close()
                        time.sleep(2)
                        space()
                        space()
                        kk=open("ali\\myc4.txt","r")
                        slowprint(kk.read(),0.03)
                        kk.close()
                        time.sleep(2)
                        space()
                        space()
                        bb=open("ali\\myc5.txt","r")
                        slowprint(bb.read(),0.03)
                        bb.close()
                        time.sleep(2)
                        space()
                        space()
                        kidnapping()
                
                    elif 'no' in a or 'stay' in a or 'dont' in a or "don't" in a:
                        qw=open("ali\\stay.txt","r")
                        slowprint(qw.read(),0.03)
                        qw.close()
                        time.sleep(2)
                        space()
                        space()
                        kidnapping()
                    elif "map" in a:
                        map()
                        space()
                        continue
                    else:
                        invalid()
                        space()
                        space()
                        time.sleep(2)
                        
def court_proceeding():
    az=open("ali\\court1.txt","r")
    slowprint(az.read(),0.03)
    az.close()
    time.sleep(2)
    space()
    space()
    while True:
        a=input("Would You like to Define Jim Moriarity?")
        a=a.lower()
        if 'yes' in a or 'sure' in a or 'why not' in a:
            aq=open("ali\\defjim.txt","r")
            slowprint(aq.read(),0.03)
            aq.close()
            time.sleep(2)
            space()
            space()
            while True:
                aa=open("ali\\judge.txt","r")
                slowprint(aa.read(),0.03)
                aa.close()
                time.sleep(2)
                space()
                space()
                while True:
                    ab=open("ali\\injail.txt","r")
                    slowprint(ab.read(),0.03)
                    ab.close()
                    time.sleep(2)
                    space()
                    space()
                    while True:
                        ag=open("ali\\iou.txt","r")
                        slowprint(ag.read(),0.03)
                        ag.close()
                        time.sleep(2)
                        space()
                        space()
                        while True:
                            c=input("Chat with Jim or first pour tea then chat?")
                            c=c.lower()
                            if 'yes' in c or 'chat' in c:
                                aw=open("ali\\chat.txt","r")
                                slowprint(aw.read(),0.03)
                                aw.close()
                                time.sleep(2)
                                space()
                                space()
                                jim_mor()
                            elif 'pour' in c or 'tea' in c or 'offer' in c:
                                af=open("ali\\chat1.txt","r")
                                slowprint(af.read(),0.03)
                                af.close()
                                time.sleep(2)
                                space()
                                space()
                                jim_mor()
                            elif "map" in c:
                                map()
                                space()
                                continue
                            else:
                                invalid()
                                time.sleep(2)
                                space()
                                space()
                                continue
def london_tower():
        aa=open("ali\\court.txt","r")
        slowprint(aa.read(),0.03)
        aa.close()
        time.sleep(2)
        space()
        space()
        while True:
            a=input("Do you want to search the place?")
            a=a.lower()
            if 'examine' in a or 'look around' in a or 'search' in a or 'yes' in a:
                ab=open("ali\\londontower.txt","r")
                slowprint(ab.read(),0.03)
                ab.close()
                time.sleep(2)
                space()
                space()
                while True:
                    cc=open("ali\\londontower1.txt","r")
                    slowprint(cc.read(),0.03)
                    cc.close()
                    time.sleep(2)
                    space()
                    space()
                    court_proceeding()
            elif "map" in a:
                map()
                space()
                continue
            else:
                space()
                invalid()
                space()
                time.sleep(1)
def reichenbach_fall():
    while True:
        ab=open("ali\\abc.txt","r")
        slowprint(ab.read(),0.03)
        ab.close()
        time.sleep(2)
        space()
        space()
        while True:
            a=input("Do you want to reply back? : ")
            a=a.lower()
            if "ignore" in a or "dont reply" in a or "don't" in a or 'no' in a:
                bc=open("ali\\abc1.txt","r")
                slowprint(bc.read(),0.03)
                bc.close()
                time.sleep(2)
                space()
                space()
                london_tower()
            elif "message" in a or "reply" in a or "text" in a or 'yes' in a:
                cd=open("ali\\abc2.txt","r")
                slowprint(cd.read(),0.03)
                cd.close()
                time.sleep(2)
                space()
                space()
                london_tower()
            elif "map" in a:
                map()
                space()
                continue
            else:
                invalid()
                time.sleep(2)
                space()
                space()
                continue


def last():
    print("The pink phone rings again ")
    space()
    while True:
        a=input("what do you want to do ?")
        a=a.lower()
        if "pick" in a or "recieve" in a or "attend" in a:
            space()
            b = open("4rth\\last.txt","r")
            slowprint(b.read(),0.04)
            b.close()
            while True:
                c=input("Go to the complex")
                if "go" in c or "sure" in c or "yes" in c:
                    space()
                    d= open("4rth\\complex.txt","r")
                    slowprint(d.read(),0.04)
                    d.close()
                    space()
                    e=input("Press any key to continue....")
                    space()
                    f=open("4rth\\complex2.txt","r")
                    slowprint(f.read(),0.04)
                    f.close()
                    l=open("4rth\\complex3.txt","r")
                    slowprint(l.read(),0.04)
                    l.close()
                    space()
                    time.sleep(2)
                    print("After few days")
                    reichenbach_fall()
                elif "no" in c or "later" in c or "leave" in c:
                    space()
                    print("You have to go to the pool to reveal who the bomber is ")
                    space()
                    time.sleep(1)
                    continue
                elif "where" in c:
                    space()
                    print("You are at your house and planing to go to the pool.")
                    space()
                    time.sleep(1)
                    continue
                elif "map" in c:
                    map()
                    space()
                    continue
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue
        elif "no" in a or "ignore" in a or "no" in a:
            space()
            print("you have to pick the call its from the bomber")
            space()
            time.sleep()
            continue
        elif "map" in a:
            map()
            space()
            continue
        elif "where" in a:
            space()
            print("you are at the police station.")
            space()
            time.sleep()
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue
def connie2():
    a=open("4rth\\done.txt","r")
    slowprint(a.read(),0.04)
    a.close()
    space()
    time.sleep(1)
    while True:
        b=input("would you like to tell him your deductions")
        b=b.lower()
        if "yes" in b or "sure" in b or "tell" in b or "why not" in b:
            c=open("4rth\\tell.txt","r")
            slowprint(c.read(),0.04)
            c.close()
            space()
            e=input("press any key to continue....")
            space()
            d=open("4rth\\tell2.txt","r")
            slowprint(d.read(),0.04)
            d.close()
            space()
            while True:
                print("You have to go to the police station to tell Lestrade")
                space()
                g=input("what do you want to do ? ")
                g=g.lower()
                if "police" in g or "lestrade" in g or "go" in g or "yes" in g or "sure" in g:
                    f=open("4rth\\police3.txt","r")
                    slowprint(f.read(),0.04)
                    f.close()
                    space()
                    i=input("press any key to continue.....")
                    space()
                    h=open("4rth\\police4.txt","r")
                    slowprint(h.read(),0.04)
                    h.close()
                    last()
                elif "no" in g or "later" in g:
                    space()
                    time.sleep(1)
                    continue
                elif "map" in g:
                    map()
                    space()
                    continue
                else:
                    invalid
                    space()
                    time.sleep(1)
                    continue
        elif "no" in b or "later" in b:
            space()
            print("JOHN : Sherlock you can tell me your deduction I want to hear how close I was.")
            space()
            time.sleep(1)
            continue
        elif "where" in b:
            space()
            print("At Connie Prince house")
            space()
            time.sleep(1)
            continue
        elif "map" in b:
            map()
            space()
            continue
        else:
            space()
            invalid()
            space()
            time.sleep(1)

def answer():
    while True:
        a = input('''What do you reply Lestrade
1) Missing what missing ?
2) You should get more information
3) Join John and find those things''')
        a=a.lower()
        if '1' in a or "missing what missing ?" in a:
            space()
            b=open("4rth\\missing.txt","r")
            slowprint(b.read(),0.04)
            b.close()
            space()
            time.sleep(1)
            while True:
                f = open("4rth\\deliver.txt","r")
                slowprint(f.read(),0.04)
                f.close()
                space()
                time.sleep(1)
                g=input("What do you want to do ? ")
                if "go" in g or "sure" in g or "ok" in g or "go" in g or "home" in g:
                    space()
                    time.sleep(1)
                    h = open("4rth\\221b.txt","r")
                    slowprint(h.read(),0.04)
                    h.close()
                    space()
                    i=input("press any key to continue....")
                    space()
                    j=open("4rth\\221b2.txt","r")
                    slowprint(j.read(),0.04)
                    j.close()
                    time.sleep(1)
                    while True:
                        l = input("What to do now ? ")
                        l=l.lower()
                        time.sleep(1)
                        if "recieve" in l or "attend" in l or "pick it" in l or "listen" in l:
                            space()
                            m=open("4rth\\call4.txt","r")
                            slowprint(m.read(),0.04)
                            m.close()
                            connie2()
                        elif "ignore" in l or "no" in l or "cannot" in l or "leave" in l or "later" in l:
                            space()
                            print("you cannot ignore this call its from bomber")
                            space()
                            time.sleep(1)
                            continue
                        elif "map" in l:
                            map()
                            space()
                            continue
                        elif "where" in l:
                            space()
                            print("you are at your house 221b inspecting things with lestrade")
                            space()
                            time.sleep(1)
                            continue
                        else:
                            space()
                            invalid()
                            space()
                            time.sleep(1)
                            continue
                elif "no" in g or "later" in g or "sorry" in g:
                    space()
                    print("You have to go for further investigation.")
                    space()
                    time.sleep(1)
                    continue
                elif "where" in g:
                    space()
                    k=open("4rth\\w3.txt","r")
                    slowprint(k.read(),0.04)
                    k.close()
                    space()
                    time.sleep(1)
                    continue
                elif "map" in g:
                    map()
                    space()
                    continue
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue
                             
        elif '2' in a or "you should get more information" in a:
            space()
            c=open("4rth\\find.txt","r")
            slowprint(c.read(),0.04)
            c.close()
            space()
            time.sleep(1)
            print("So you may ask another question.")
            space()
            continue
        elif '3' in a or "join John and find those things" in a:
            space()
            d=open("4rth\\join.txt","r")
            slowprint(d.read(),0.04)
            d.close()
            space()
            time.sleep(1)
            continue
        elif "map" in a:
            map()
            space()
            continue
        elif "where" in a:
            space()
            e=open("4rth\\w2.txt","r")
            slowprint(e.read(),0.04)
            e.close()
            space()
            time.sleep(1)
            continue
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue


def connie():
    a=open("4rth\\police1.txt","r")
    slowprint(a.read(),0.04)
    a.close()
    space()
    b=input("press any key to continue....")
    space()
    c=open("4rth\\police2.txt","r")
    slowprint(c.read(),0.04)
    c.close()
    space()
    time.sleep(1)
    while True:
        d=open("4rth\\lestrade.txt","r")
        slowprint(d.read(),0.04)
        d.close()
        space()
        time.sleep(1)
        while True:
            e=input("Continue the examining ?")
            e=e.lower()
            if "yes" in e or "sure" in e or "continue" in e or "examine" in e:
                space()
                f=open("4rth\\further.txt","r")
                slowprint(f.read(),0.04)
                f.close()
                space()
                i=input("press any key to continue....")
                space()
                j=open("4rth\\further2.txt","r")
                slowprint(j.read(),0.04)
                j.close()
                space()
                time.sleep(1)
                answer()
            elif "no" in e or "not" in e or "ignore" in e:
                space()
                g=open("4rth\\ignore2.txt","r")
                slowprint(g.read(),0.04)
                g.close()
                space()
                time.sleep(1)
                continue
            elif "where" in e:
                space()
                h=open("4rth\\w2.txt","r")
                slowprint(h.read(),0.04)
                h.close()
                space()
                time.sleep(1)
                continue
            
            elif "map" in e:
                map()
                space()
                continue
            else:
                space()
                invalid()
                space()
                time.sleep()
                continue



def greatgame3():
    space()
    a = input("press any key to continue....")
    time.sleep(2)
    b=open("4rth\\1.txt","r")
    slowprint(b.read(),0.04)
    b.close()
    c=input("press any key to continue....")
    d=open("4rth\\2.txt","r")
    slowprint(d.read(),0.04)
    space()
    time.sleep(1)
    e=open("4rth\\connie.txt","r")
    slowprint(e.read(),0.04)
    e.close()
    space()
    while True:
        f=input("what do you want to do ?")
        f=f.lower()
        if "recieve" in f or "attend" in f or "pick it" in f or "listen" in f:
            space()
            g=open("4rth\\call.txt","r")
            slowprint(g.read(),0.04)
            g.close()
            time.sleep(1)
            space()
            h=open("4rth\\call2.txt","r")
            slowprint(h.read(),0.04)
            h.close()
            space()
            time.sleep(1)
            while True:
                print("Phone ringing and this time it's from Lestrade")
                space()
                k=input("what do you want to do ?")
                k=k.lower()
                if "recieve" in k or "attend" in k or "pick it" in k or "listen" in k:
                    space()
                    l=open("4rth\\call3.txt","r")
                    slowprint(l.read(),0.04)
                    l.close()
                    time.sleep(1)
                    while True:
                        space()
                        o=input('''What do you want to do:
1) Go to police station
2) eat lunch first ''')
                        o=o.lower()
                        if "eat" in o or "lunch" in o:
                            space()
                            p=open("4rth\\eat.txt","r")
                            slowprint(p.read(),0.04)
                            p.close()
                            space()
                            time.sleep(1)
                            connie()
                        elif "go" in o or "lestrade" in o or "police" in o:
                            space()
                            q=open("4rth\\police.txt","r")
                            slowprint(q.read(),0.04)
                            q.close()
                            space()
                            time.sleep(1)
                            connie()
                        elif "map" in o:
                            map()
                            space()
                            continue
                        elif "where" in o:
                            space()
                            r=open("4rth\\w1.txt","r")
                            slowprint(r.read(),0.04)
                            r.close()
                            space()
                            time.sleep(1)
                            continue
                        else:
                            space()
                            invalid()
                            space()
                            time.sleep(1)
                            continue
                        
                elif "ignore" in k or "no" in k or "cannot" in k or "leave" in k or "later" in k:
                    space()
                    m=open("4rth\\ignore1.txt","r")
                    slowprint(m.read(),0.04)
                    m.close()
                    space()
                    time.sleep(1)
                    continue
                elif "where" in k:
                    space()
                    n=open("4rth\\w1.txt","r")
                    slowprint(n.read(),0.04)
                    n.close()
                    space()
                    time.sleep(1)
                    continue
                elif "map" in k:
                    map()
                    space()
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue

        elif "ignore" in f or "no" in f or "cannot" in f or "leave" in f or "later" in f:
            space()
            i=open("4rth\\ignore.txt","r")
            slowprint(i.read(),0.04)
            i.close()
            space()
            time.sleep(1)
            continue
        elif "where" in f:
            space()
            j=open("4rth\\w1.txt","r")
            slowprint(j.read(),0.04)
            j.close()
            space()
            time.sleep(1)
            continue
        elif "map" in f:
            map()
            space()
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue
            


def police():
    a = open("3rd\\police.txt","r")
    slowprint(a.read(),0.004)
    a.close()
    space()
    b=input("press any key to continue....")
    space()
    c=open("3rd\\police2.txt","r")
    slowprint(c.read(),0.004)
    c.close()
    space()
    time.sleep(1)
    while True:
        d=input("Tell them the further assumption ?")
        d=d.lower()
        if "yes" in d or "sure" in d or "why not" in d or "tell" in d:
            space()
            e = open("3rd\\further.txt","r")
            slowprint(e.read(),0.004)
            e.close()
            space()
            time.sleep(1)
            f = input("press any key to continue....")
            space()
            g=open("3rd\\further2.txt","r")
            slowprint(g.read(),0.004)
            g.close()
            greatgame3()
        elif "no" in d or "no" in d or "cannot" in d or "ignore" in d:
            space()
            e = open("3rd\\ignore3.txt","r")
            slowprint(e.read(),0.004)
            e.close()
            space()
            time.sleep(1)
            continue
        elif "where" in d:
            space()
            print("you are at the police car pund with watson and Lestrade to inspect the car.")
            space()
            time.sleep(1)
            continue
        elif "quit" in d or "exit" in d:
            sys.exit()
        elif "map" in d:
            map()
            space()
            continue
        else:
            space()
            invalid()
            space()
            time.sleep(1)
            continue
 
def lab2():
    while True:
        print("JOHN : So what you deduced ? ")
        a=input("tell John or not ? ")
        if "tell" in a or "ok" in a or "sure" in a or "talk" in a:
            space()
            b=open("3rd\\john.txt","r")
            slowprint(b.read(),0.004)
            b.close()
            space()
            time.sleep(1)
            while True:
                d=open("3rd\\lab.txt","r")
                slowprint(d.read(),0.004)
                space()
                time.sleep(1)
                while True:
                    e=input("what to do ? ")
                    e=e.lower()
                    if "examine" in e or "investigate" in e or "check" in e or "look" in e:
                        space()
                        f = open("3rd\\blood.txt","r")
                        slowprint(f.read(),0.004)
                        f.close()
                        space()
                        time.sleep(1)
                        while True:
                            i=input("attend the call ? ")
                            i=i.lower()
                            if "yes" in i or "sure" in i or "ok" in i or "attend" in i or "recieve" in i:
                                space()
                                j=open("3rd\\blood2.txt","r")
                                slowprint(j.read(),0.004)
                                j.close()
                                space()
                                time.sleep(1)
                                police()
                            elif "no" in i or "donot" in i or "cannot" in i or "later" in i:
                                space()
                                k=open("3rd\\ignore2.txt","r")
                                slowprint(k.read(),0.004)
                                k.close()
                                space()
                                time.sleep(1)
                                continue
                            elif "where" in i:
                                space()
                                l=open("3rd\\w3.txt","r")
                                slowprint(l.read(),0.004)
                                l.close()
                                space()
                                time.sleep(1)
                                continue
                            elif "quit" in i or "exit" in i:
                                sys.exit()
                            elif "map" in i:
                                map()
                                space()
                                continue
                            else:
                                space()
                                invalid()
                                space()
                                time.sleep(1)
                                continue
                            
                    elif "donot" in e or "no" in e or "cannot" in e or "ignore" in e:
                        space()
                        g=open("3rd\\ignore1.txt","r")
                        slowprint(g.read(),0.004)
                        g.close()
                        space()
                        time.sleep(1)
                        continue
                    elif "where" in e:
                        space()
                        h=open("3rd\\w2.txt","r")
                        slowprint(h.read(),0.004)
                        h.close()
                        space()
                        time.sleep(1)
                        continue
                    elif "quit" in e or "exit" in e:
                        sys.exit()
                    elif "map" in e:
                        map()
                        space()
                        continue
                    else:
                        space()
                        invalid()
                        space()
                        time.sleep(1)
                        continue
                    
        elif "no" in a or "donot" in a or "cannot" in a or "later" in a:
            space()
            c=open("3rd\\john1.txt","r")
            slowprint(c.read(),0.004)
            c.close()
            space()
            time.sleep(1)
            continue
        elif "quit" in a or "exit" in a:
            sys.exit()
        elif "map" in a:
            map()
            space()
            continue
        else:
            space()
            invalid()
            space()
            time.sleep(1)
    
def scene():
    a=open("3rd\\scene.txt","r")
    slowprint(a.read(),0.004)
    a.close()
    while True:    
        b=input("what to do now ?")
        b=b.lower()
        if "examine" in b or "investigate" in b or "check" in b or "ok" in b:
            c=open("3rd\\check.txt","r")
            slowprint(c.read(),0.004)
            c.close()
            time.sleep(1)
            space()
            while True:
                q=input("talk to Mrs. Monkford or not ?")
                q=q.lower()
                if "talk" in q or "yes" in q or "sure" in q:
                    w=open("3rd\\mrs.txt","r")
                    slowprint(w.read(),0.004)
                    w.close()
                    space()
                    t=open("3rd\\mrs2.txt","r")
                    slowprint(t.read(),0.004)
                    t.close()
                    space()
                    time.sleep(1)
                    while True:
                        print("you have to go the JANUS cars for further investigation")
                        f=input("what to do now ?")
                        f=f.lower()
                        if "janus" in f or "go" in f or "ok" in f or "cab" in f:
                            print("you arrive at JANUS cars and goes to the manager's office.")
                            while True:
                                g=input("what to do now ?")
                                g=g.lower()
                                if "investigate" in g or "ask" in g or "examine" in g:
                                    A=open("3rd\\janus.txt","r")
                                    slowprint(A.read(),0.004)
                                    A.close()
                                    space()
                                    time.sleep(1)
                                    Z=input("press any key to continue ....")
                                    space()
                                    time.sleep(1)
                                    B=open("3rd\\janus2.txt","r")
                                    slowprint(B.read(),0.004)
                                    B.close()
                                    space()
                                    time.sleep(1)
                                    lab2()
                                elif "no" in g or "donot" in g or "cannot" in g or "later" in g:
                                    space()
                                    print("you have to investigate him.")
                                    space()
                                    time.sleep(1)
                                    continue
                                elif "where" in g:
                                    space()
                                    ii=open("3rd\\w.txt","r")
                                    slowprint(ii.read(),0.004)
                                    ii.close()
                                    space()
                                    ttime.sleep(1)
                                    continue
                                elif "quit" in g or "exit" in g:
                                    sys.exit()
                                elif "map" in g:
                                    map()
                                    space()
                                    continue
                                else:
                                    space()
                                    print("You have to in vestigate him.")
                                    space()
                                    invalid()
                                    space()
                                    time.sleep(0.004)
                                    continue
                        elif "donot" in f or "no" in f or "cannot" in f or "later" in f:
                            pp=open("3rd\\no2.txt","r")
                            slowprint(pp.read(),0.004)
                            pp.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "where" in f:
                            yy=open("3rd\\sea.txt","r")
                            slowprint(yy.read(),0.004)
                            s.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "quit" in f or "exit" in f:
                            sys.exit()
                        elif "map" in f:
                            map()
                            space()
                            continue
                        else:
                            invalid()
                            space()
                            time.sleep(1)
                            continue

                elif "no" in q or "cannot" in q or "leave" in q or "not" in q:
                    r=open("3rd\\no.txt","r")
                    slowprint(r.read(),0.004)
                    r.close()
                    space()
                    time.sleep(1)
                    continue
                elif "where" in q:
                    s=open("3rd\\sea.txt","r")
                    slowprint(s.read(),0.004)
                    s.close()
                    space()
                    time.sleep(1)
                    continue
                elif "quit" in q or "exit" in q:
                    sys.exit()
                elif "map" in q:
                    map()
                    space()
                    continue
                else:
                    space()
                    invalid()
                    space()
                    time.sleep(1)
                    continue
        elif "lestrade" in b: 
            space()
            c=open("3rd\\lestrade3.txt","r")
            slowprint(c.read(),0.004)
            c.close()
            space()
            time.sleep(1)
            continue
        elif "watson" in b:
            d=open("3rd\\watson.txt","r")
            slowprint(d.read(),0.004)
            d.close()
            space()
            time.sleep(1)
            continue
        elif "where" in b:
            e=open("3rd\\sea.txt","r")
            slowprint(e.read(),0.004)
            e.close()
            space()
            time.sleep(1)
            continue
        elif "quit" in b or "exit" in b:
            sys.exit()
        elif "map" in b:
            map()
            space()
            continue
        else:
            invalid()
            space()
            time.sleep(1)
            continue
        
def call2():
    a=open("3rd\\call4.txt","r")
    slowprint(a.read(),0.004)
    a.close()
    space()
    time.sleep(1)
    b=open("3rd\\call5.txt","r")
    slowprint(b.read(),0.004)
    b.close()
    space()
    while True:
        c=input("Ask lestrade about the missing car ? ")
        c=c.lower()
        if "yes" in c or "ask him" in c or "talk to him" in c:
            d=open("3rd\\lestrade.txt","r")
            slowprint(d.read(),0.004)
            d.close()
            space()
            time.sleep(1)
            scene()
        elif "no" in c or "donot" in c or "ignore" in c or "cannot" in c:
            e = open("3rd\\lestrade2.txt","r")
            slowprint(e.read(),0.004)
            e.close()
            space()
            time.sleep(1)
        elif "quit" in c or "exit" in c:
            sys.exit()
        elif "where" in c:
            print("you are at the police station with Watson and Lestrade")
            space()
            time.sleep(1)
            continue
        elif "map" in c:
            map()
            space()
            continue
        else:
            invalid()
            space()
            time.sleep(1)
            continue
    
def message2():
    a=open("3rd\\car.txt","r")
    slowprint(a.read(),0.004)
    a.close()
    while True:
        b=input("you want to pick the phone ? ")
        b=b.lower()
        if "pick the call" in b or "attend" in b or "recieve" in b or "pick it" in b or "pick call" in b:
            c=open("3rd\\call1.txt","r")
            slowprint(c.read(),0.004)
            c.close()
            space()
            time.sleep(1)
            call2()
        elif "no" in b or "ask lestrade" in b or "ask watson" in b or "donot" in b or "cannot" in b:
            d=open("3rd\\call2.txt","r")
            slowprint(d.read(),0.004)
            d.close()
            space()
            time.sleep(1)
            call2()
        elif "watson" in b or "ask watson" in b:
            e=open("3rd\\call3.txt","r")
            slowprint(e.read(),0.004)
            e.close()
            space()
            time.sleep(1)
            call2()
        elif "quit" in b or "exit" in b :
            sys.exit()
        elif "map" in b:
            map()
            space()
            continue
        else:
            invalid()
            space()
            time.sleep(1)
            

#Ahmed ashraf
def greatgame2(): #3rd case
    a=open("3rd\\1.txt","r")
    slowprint(a.read(),0.004)
    a.close()
    e=open("3rd\\2.txt","r")
    slowprint(e.read(),0.004)
    e.close()
    space()
    time.sleep(1)
    while True:
        b=input("LESTRADE : lets have a cup of tea ")
        b=b.lower()
        if "drink" in b or "ok" in b or "sure" in b or "why not" in b or "yes" in b:
            c=open("3rd\\tea.txt","r")
            slowprint(c.read(),0.004)
            c.close()
            space()
            time.sleep(1)
            message2()
        elif "no" in b or "not now" in b or "never" in b or "cannot" in b or "later" in b:
            d=open("\\ignore.txt","r")
            slowprint(d.read(),0.004)
            d.close()
            space()
            time.sleep(1)
            message2()
        elif "quit" in b or "exit" in b:
            sys.exit()
        elif "map" in b:
            map()
            space()
            continue
        else:
            invalid()
            space()
            time.sleep(1)
    
def call(): #AHMED ASHRAF SP18-BSE-009
    while True:
        q=input("you want to examine shoes for clues or leave them ? ")
        q=q.lower()
        if "leave" in q or "ignore" in q or "donot examine" in q:
            ww=open("2nd\\ignore2.txt","r")
            slowprint(ww.read(),0.04)
            ww.close()
            space()
            time.sleep(1)
            continue
        elif "examine" in q or "investigate" in q or "inspect" in q or "check" in q:
            qq=open("2nd\\examine2.txt","r")
            slowprint(qq.read(),0.04)
            qq.close()
            space()
            time.sleep(1)
            while True:
                p=input('''where you want to Search for information about carl power's
1) Locker
2) Swiming pool''')
                p=p.lower()
                if "swiming pool" in p or "2" in p:
                    o=open("2nd\\swiming.txt","r")
                    slowprint(o.read(),0.04)
                    o.close()
                    space()
                    time.sleep(1)
                    continue
                elif "locker" in p or '1' in p:
                    pp=open("2nd\\locker.txt","r")
                    slowprint(pp.read(),0.04)
                    pp.close()
                    while True:
                        i=input('''what do you think the reason could be of his death :
1) Murder
2) sucide
3) natural ''')
                        i=i.lower()
                        if "murder" in i or "killed" in i or "1" in i:
                            k=open("2nd\\killed.txt","r")
                            slowprint(k.read(),0.04)
                            k.close()
                            space()
                            time.sleep(1)
                            l=open("2nd\\1solve.txt","r")
                            slowprint(l.read(),0.04)
                            l.close()
                            greatgame2()
                            
                        elif "sucide" in i or '2' in i:
                            ss=open("2nd\\sucide.txt","r")
                            slowprint(ss.read(),0.04)
                            ss.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "natural" in i or "3" in i:
                            n=open("2nd\\natural.txt","r")
                            slowprint(n.read(),0.04)
                            n.close()
                            space()
                            time.sleep(1)
                            continue
                        elif "quit" or "exit" in i:
                            sys.exit()
                        else:
                            invalid()
                            space()
                            time.sleep(1)
                            
                elif "quit" in p or "exit" in p:
                    sys.exit()
                elif "map" in p:
                    map()
                    space()
                    continue
                else:
                    invalid()
                    space()
                    time.sleep(1)
        elif "where" in q:
            print("still in the rooom")
            space()
            time.sleep(1)
            continue
        elif "map" in q:
            map()
            space()
            continue
        else:
            invalid()
            space()
            time.sleep(1)
            
a=['Pink Iphone','gun','microscope','gloves']

def envelope(): #AHMED ASHRAF SP18-BSE-009
    space()
    time.sleep(1)
    q=open("2nd\\envelop1.txt","r")
    slowprint(q.read(),0.04)
    q.close()
    while True:
        w = input("what to do now ? ")
        w = w.lower()
        if "go there" in w or "lets go" in w or "move" in w:
            space()
            time.sleep(1)
            e=open("2nd\\221c.txt","r") #opening the file
            slowprint(e.read(),0.04)
            e.close()#closing the file
            space()
            time.sleep(1)
            while True:
                r=input("What to do now ? ")
                r=r.lower()
                space()
                time.sleep(1)

                if "examine" in r or "inspect" in r:
                    t=open("2nd\\examine1.txt","r")
                    slowprint(t.read(),0.04)
                    t.close()
                    space()
                    time.sleep(1)
                    while True:
                        qq = input("Want to pick the call or not ? ")
                        qq = qq.lower()
                        if "pick it" in qq or "pick" in qq and not "donot pick" in qq or "recieve" in qq or "attend" in qq:
                            ww=open("2nd\\call.txt","r")
                            slowprint(ww.read(),0.04)
                            ww.close()
                            space()
                            time.sleep(1)
                            call()
                        elif "ignore" in qq or "donot pick" in qq:
                            ee=open("2nd\\ignore1.txt","r")
                            slowprint(ee.read(),0.04)
                            ee.close()
                            space()
                            time.sleep(1)
                        elif "lestrade" in qq or "watson" in qq:
                            print("Its better you pick the call ")
                            space()
                            time.sleep(1)
                        elif "quit" in qq or "exit" in qq:
                            sys.exit()
                        elif "map" in qq:
                            map()
                            space()
                            continue
                        else:
                            invalid()
                            space()
                            time.sleep(1)
                elif "leave" in r or "donot check" in r or "ignore" in r or "cannot" in r:
                    y=open("2nd\\donot1.txt","r")
                    slowprint(y.read(),0.04)
                    y.close()
                    space()
                    time.sleep(1)

                elif "where" in r:
                    print("You are in 221C in the basment of Mrs. Hudesn house.")
                    space()
                    time.sleep(1)

                elif "quit" in r or "exit" in r:
                    sys.exit()
                elif "map" in r:
                    map()
                    space()
                    continue
                else:
                    invalid()
                    space()
                    time.sleep(1)

        elif "donot go" in w or " we cannot go" in w or "donot" in w:
            space()
            time.sleep(1)
            r=open("2nd\\donot.txt","r") #opening the file
            slowprint(r.read(),0.04)
            r.close() #closing the file
            space()
            time.sleep(1)

        elif "where" in w:
            
            print("you are standing in the police station")
            space()
            time.sleep(1)

        elif "quit" in w or "exit" in w:
            sys.exit()
        elif "map" in w:
            map()
            space()
            continue
        
        else:
            invalid()
            space()
            time.sleep(1)



def thegreatgame(): #AHMED ASHRAF SP18-BSE-009
    while True:
        q=open("2nd\\great.txt","r") #reading from great in 2nd folder
        slowprint(q.read(),0.04) #calling to print character by character
        q.close()
        time.sleep(1)
        w=open("2nd\\bomb.txt","r") #getting the text
        slowprint(w.read(),0.04)
        w.close()
        while True:
            call = input("what do you want to do ? ") #input from the user
            call = call.lower()
            space()
            time.sleep(1)
            if "attend" in call or "recieve" in call or "pick call" in call:
                a=open("2nd\\attend.txt","r")
                slowprint(a.read(),0.04)
                a.close()
                space()
                time.sleep(1)
                while True:
                    d=open("2nd\\cab.txt","r")
                    slowprint(d.read(),0.04)
                    d.close()
                    space()
                    time.sleep(1)
                    while True:
                        f=input("what to do now ? ")
                        f=f.lower()
                        if "examine" in f or "inspect" in f or "open" in f:
                            g=open("2nd\\envelope.txt","r")
                            slowprint(g.read(),0.04)
                            g.close()
                            envelope()
                        elif "ignore" in f or "walk" in f or "talk" in f:
                            print("Lestrade : Sherlock inspect the envelope ")
                            space()
                            time.sleep(1)
                        elif "where" in f:
                            print("you are in the police stattion with John")
                            space()
                            time.sleep(1)
                        elif "quit" in f or "exit" in f:
                            sys.exit()
                        elif "map" in f:
                            map()
                            space()
                            continue
                        else:
                            invalid()
                            space()
                            time.sleep(1)
                            
            elif "ignore" in call or "donot attend" in call or "donot recieve" in call or "donot pick" in call:
                s=open("2nd\\ignore.txt","r")
                slowprint(s.read(),0.04)
                s.close()
                space()
                time.sleep(1)
            elif "quit" in call or "exit" in call:
                sys.exit()
            elif "map" in call:
                map()
                space()
                continue
            else:
                invalid()
                space()
                time.sleep(1)

def chellenge(): #the final chellenge with the cabbie
    dd=open("files\\chellenge1.txt","r")
    slowprint(dd.read(),0.04)
    dd.close()
    time.sleep(1)
    space()
    while True:
        tt=input("YOU WANT TO PLAY THE GAME ? ")
        tt = tt.lower()
        if "yes" in tt or "sure" in tt or "yea" in tt:
            time.sleep(1)
            space()
            while True:
                yy=input("cabbie offers you the same what will you choose pills or the gun ? ")
                yy=yy.lower()
                if "pill" in yy :
                    print("You die because you choose the wrong pill try again ")
                    time.sleep(1)
                    space()
                    continue
                elif "gun" in yy:
                    ss=open("files\\gun.txt","r")
                    slowprint(ss.read(),0.04)
                    ss.close()
                    time.sleep(1)
                    space()
                    print("MYSTERY SOLVED") #1st mystery solved
                    time.sleep(2)
                    space()
                    thegreatgame() # calling the next function of next level
                elif "quit" or "exit" in yy:
                    sys.exit()
                elif "map" in yy:
                    map()
                    space()
                    continue
                else:
                    invalid()
                    continue
        elif "no" in tt or "cannot" in tt:
            print("YOU HAVE TO PLAY THE GAME ")
            space()
            invalid()
            time.sleep(1)
            space()
        elif "quit" in tt or "exit" in tt:
            sys.exit()
        elif "map" in tt:
            map()
            space()
            continue
        else:
            invalid()
            time.sleep(1)
            space()
            continue
                                
def taxi1(): 
    while True:
        rr=input("what do you want to ask the cabbie now ? ") #asking the cabbie questions
        rr=rr.lower()
        if "who are you" in rr:
            time.sleep(1)
            space()
            print("Cabbie : I'm the person who killed that lady. ")
            space()
            time.sleep(1)
            
        elif "who am i" in rr:
            print("you are detective Sherlock holmes ")
            time.sleep(1)
            space()
            continue
        elif "why are you doing this" in rr:
            time.sleep(1)
            space()
            print("Cabbie : I'm doing this for my childern everytime I take a life $100 are gifted to them.")
            print("Cabbie : I don't killed her i just gave her an offer and she killed herself. I just play a game ")
            time.sleep(1)
            space()
            chellenge()
        elif "how you killed her" in rr:
            space()
            time.sleep(1)
            print("Cabbie : I don't killed her i just gave her an offer and she killed herself ")
            space()
            time.sleep(1)
            chellenge()
        elif "quit" in rr or "exit" in rr:
            sys.exit()
        elif "map" in rr:
            map()
            space()
            continue
        else:
            invalid()
            space()
            time.sleep(1)
def flat1(): #AHMED ASHRAF SP18-BSE-009
    while True:
        qq=open("files\\flat1.txt","r") #going to flat after finding the bag
        slowprint(qq.read(),0.04)
        qq.close()
        space()
        time.sleep(1)
        while True:
            ww=input("what to do now ? ") #cabie arrives
            ww=ww.lower()
            if "outside" in ww or "go in taxi" in ww or "go" in ww or "go in cab" in ww or "leave flat" in ww:
                ee=open("files\\taxi1.txt","r") #the taxi journy loading
                slowprint(ee.read(),0.04)
                ee.close()
                space()
                time.sleep(1)
                taxi1()
            elif "dont" in ww or "stay" in ww or "don't" in ww or "no" in ww or "cant" in ww or "can't" in ww or "cannot" in ww: #have to go
                print("You have to go with cabbie to solve the mystery ")
                continue
            elif "ask mrs hudson" in ww or "who" in ww or "did not" in ww: #have to go with cabbie to continue the game
                print("Mrs. Hudson : Sorry dear you have to ask him about this ")
                continue
            elif "quit" in ww or "exit" in ww:
                sys.exit()
            elif "map" in ww:
                map()
                space()
                continue
            else:
                invalid()
def trash(): 
    while True:
        time.sleep(1.5)
        space()
        ww=open("files\\bin.txt","r")
        slowprint(ww.read(),0.04)
        ww.close()
        space()
        time.sleep(2)
        qq=open("files\\watson1.txt","r")
        slowprint(qq.read(),0.04)
        qq.close()
        ww=input("what do you want to do now ? ")
        ww=ww.lower()
        if "dont" in ww or "don't" in ww or "no" in ww or "cant" in ww or "can't" in ww or "not" in ww:
            space()
            time.sleep(1)
            ss=open("files\\eatn1.txt","r")
            slowprint(ss.read(),0.04)
            ss.close()
            space()
            time.sleep(1)
            flat1()
        elif "yes" in ww or "sure" in ww or  "why not" in ww or "ok" in ww or "okay" in ww:
            space()
            time.sleep(1)
            ee=open("files\\eat1.txt","r")
            slowprint(ee.read(),0.04)
            ee.close()
            space()
            time.sleep(1)
            flat1()
        elif 'quit' in ww:
            sys.exit()
        elif "map" in ww:
            map()
            space()
            continue
        
        else:
            invalid()
            continue

def pink():
    while True:
        time.sleep(1)
        space()
        a=open("files\\pink1.txt","r")
        slowprint(a.read(),0.04)
        a.close()
        space()
        while True:
            do=input("what do you want to do ? ")
            do=do.lower()
            if 'look' in do:
                time.sleep(1)
                b=open("files\\looka1.txt","r")
                slowprint(b.read(),0.04)
                b.close()
                space()
                continue
                time.sleep(1)
            elif "map" in do:
                map()
                space()
                continue
            elif 'examine' in do or "inspect" in do or "detect" in do:
                time.sleep(1)
                c=open("files\\examine1.txt","r")
                slowprint(c.read(),0.04)
                c.close()
                space()
                while True:
                    space()
                    time.sleep(1.5)
                    r=open('files\\search1.txt','r')
                    slowprint(r.read(),0.04)
                    r.close()
                    space()
                    time.sleep(1.5)
                    w=input("where you want to search ? (search in street go left or right)")
                    w=w.lower()
                    if 'right' in w:
                        time.sleep(1.5)
                        space()
                        q=open("files\\right1.txt","r")
                        slowprint(q.read(),0.04)
                        q.close()
                        space()
                        print("Going back to the building and standing infront of it again  ")
                        time.sleep(1.5)
                    elif "map" in w:
                        map()
                        space()
                        continue
                    elif 'left' in w:
                        space()
                        time.sleep(1.5)
                        p=open("files\\left1.txt","r")
                        slowprint(p.read(),0.04)
                        p.close()
                        time.sleep(1.5)
                        space()
                        while True:
                            z=input("Where you want to search now ?")
                            z=z.lower()
                            if "gutter" in z:
                                space()
                                time.sleep(1.5)
                                qq=open("files\\guter.txt","r")
                                slowprint(qq.read(),0.04)
                                qq.close()
                                space()
                                time.sleep(1.5)
                                continue
                            elif "trash" in z or "bin" in z or "garbage" in z:
                                trash()
                            elif "plant" in z or "green" in z or "small plants" in z:
                                time.sleep(1.5)
                                space()
                                ee=open("files\\plant.txt","r")
                                slowprint(ee.read(),0.04)
                                ee.close()
                                continue
                            elif "all" in z or "every" in z or "them" in z:
                                time.sleep(1.5)
                                space()
                                qq=open("files\\guter.txt","r")
                                slowprint(qq.read(),0.04)
                                qq.close()
                                space()
                                time.sleep(1.5)
                                ee=open("files\\plant.txt","r")
                                slowprint(ee.read(),0.04)
                                ee.close()
                                space()
                                trash()
                            elif 'quit' in z:
                                sys.exit()
                            elif "map" in z:
                                map()
                                space()
                                continue
                            else:
                               invalid()
                               continue
                    else:
                        space()
                        invalid()
                        space()
            elif 'walk' in do:
                time.sleep(1)
                d=open("files\\walk1.txt","r")
                slowprint(d.read(),0.04)
                d.close()
                space()
                time.sleep(1)
                continue
            elif 'where' in do:
                g=open("files\\where1.txt","r")
                slowprint(g.read(),0.04)
                g.close()
            elif 'lestrade' in do:
                i=open("files\\lestrade1.txt","r")
                slowprint(i.read(),0.04)
                i.close()
            elif "map" in do:
                map()
                space()
                continue
            elif 'quit' in do:
                sys.exit()
            else:
                invalid()
                space()
                continue
                time.sleep(1)
        
def credits(): #AHMED ASHRAF SP18-BSE-009
    c=open("files\\credits.txt","r")
    slowprint(c.read(),0.04)
    c.close()
    space()
def help(): #AHMED ASHRAF SP18-BSE-009
    h=open("files\\help.txt","r")
    slowprint(h.read(),0.04)
    h.close()
    space()
    
def play(): #AHMED ASHRAF SP18-BSE-009
    while True:
        f=open("files\\1.txt","r")
        slowprint(f.read(),0.04)
        f.close()
        space()
        while True:
            ride = input('''want to go with
1) Lestrade in police car
2) cab/Taxi ''')
            ride = ride.lower()
            if 'cab' in ride or 'taxi' in ride or '2' in ride:
                c=open("files\\cab.txt","r")
                slowprint(c.read(),0.04)
                c.close()
                pink()
            elif 'lestrade' in ride or '1' in ride:
                d=open("files\\lestrade.txt","r")
                slowprint(d.read(),0.04)
                d.close()
                space()
                pink()
            elif 'quit' in ride or 'exit' in ride :
                sys.exit()
            elif "map" in ride:
                map()
                space()
                continue
            else:
                space()
                invalid()
                space()
                time.sleep(1)
                continue
            
def menue(): #AHMED ASHRAF SP18-BSE-009
    while True:
        m='''PRESS 1 TO PLAY
PRESS 2 FOR HELP/INSTRUCTIONS
PRESS 3 FOR CREDITS
PRESS 4 FOR CHARACTERS
PRESS 5 FOR MAP
PRESS 6 FOR EXIT : '''
        menu_1 = input(m)
        menu_1= menu_1.lower()
        if '1' in menu_1 or 'play' in menu_1:
            
            space()
            play()
        elif '2' in menu_1 or 'help' in menu_1 or 'instructions' in menu_1:
            space()
            help()
        elif '3' in menu_1 or 'credits' in menu_1:
            space()
            credits()
        elif '4' in menu_1 or 'characters' in menu_1:
            space()
            time.sleep(1)
            aa=open('files\\characters.txt','r')
            slowprint(aa.read(),0.04)
            aa.close()
            space()
        elif '6' in menu_1 or 'quit' in menu_1 or 'exit' in menu_1:
            space()
            break
        elif "map" in menu_1 or '5' in menu_1:
            map()
            space()
            continue
        else:
            invalid()
            space()
            continue
            
def start(): #AHMED ASHRAF SP18-BSE-009
    a=open("files\\intro1.txt","r")
    slowprint(a.read(),0.04)
    a.close()
    time.sleep(0.5)
    b=open('files\\intro2.txt','r')
    slowprint(b.read(),0.04)
    b.close()
    space()
    menue()
start()
