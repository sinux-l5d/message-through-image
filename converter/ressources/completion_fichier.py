vals_RGB = [(0,0,0),
(5,0,5),
(25,30,14),
(61,24,12),
(25,15,35),
(48,25,14),
(90,64,10),
(70,80,56),
(78,87,97),
(99,99,99),
(102,50,30),
(103,1,20),
(10,25,103),
(14,26,105),
(102,15,35),
(218,248,77),
(73,1,185),
(8,170,214),
(219,170,56),
(169,22,216),
(151,79,83),
(160,100,115),
(135,238,195),
(219,78,93),
(76,48,253),
(169,21,58),
(235,48,226),
(109,152,140),
(135,134,49),
(13,185,43),
(247,182,45),
(241,245,80),
(125,214,238),
(246,232,183),
(138,184,218),
(139,241,27),
(247,71,229),
(234,31,164),
(141,247,118),
(58,155,165),
(90,241,112),
(155,68,175),
(81,43,246),
(98,1,193),
(246,10,129),
(30,180,182),
(198,194,210),
(241,175,104),
(34,42,3),
(185,33,203),
(24,139,81),
(57,151,142),
(59,218,147),
(195,240,173),
(177,38,240),
(169,95,240),
(63,15,253),
(175,64,48),
(89,86,81),
(236,254,253),
(247,183,4),
(51,48,186),
(160,162,89),
(57,132,149),
(101,95,151),
(158,244,47),
(22,52,196),
(144,153,201),
(133,75,179),
(172,160,17),
(81,119,153),
(241,46,162),
(73,151,187),
(137,179,212),
(232,154,78),
(88,63,217),
(12,135,98),
(127,210,64),
(186,78,170),
(5,103,204),
(213,54,148),
(230,200,210),
(240,255,240),
(255,255,255)
]
with open("valeurs_RGB.csv","w") as file:
    for i in range (0,84):
        varToWrite = str(i) + "," + str(vals_RGB[i]) + '\n'
        file.write(varToWrite)
