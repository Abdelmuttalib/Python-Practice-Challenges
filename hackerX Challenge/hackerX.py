
    ######### SOLUTION CODE #########
def defend(missiles):
    arr = []
    holder = []
    drop = 0
    mini = 0

    for i in missiles:
        holder = []

        for j in arr:
            print("arr: ", arr)
            print("MISS: ", i)
            print("ARR INDEX: ", j)
            current_time, current_frequency = j[0], j[1]
            print("CURRENT T & F: ", current_time, current_frequency)
            desired_time, desired_frequency = i[0], i[1]
            print("DESIRED T & F: ", desired_time, desired_frequency)
            diff_in_time, diff_in_frequency = abs(desired_time - current_time), abs(desired_frequency - current_frequency)
            print("DIFF's T & F: ", diff_in_time, "|", diff_in_frequency)

            if len(arr) == 0:
                holder = []
                break

            elif j == i:
                print("INITIAL SUCCESS: ", j, "AND", i)
                holder = j
                break

            elif (desired_time >= current_time) and ((current_frequency + diff_in_frequency == desired_frequency) or (current_frequency - diff_in_frequency == desired_frequency)) and (current_time + diff_in_frequency <= desired_time):
                if desired_frequency > current_frequency:
                    j[0], j[1] = current_time + diff_in_frequency + (diff_in_time - diff_in_frequency), current_frequency + diff_in_frequency
                    print("DESIRED > CURRENT: ", desired_frequency, desired_time)
                    print("MISSILE:", j)
                    mini += 1
                    print("MINI HERE", mini)
                    holder = j
                    break
                elif desired_frequency < current_frequency:
                    j[0], j[1] = current_time + diff_in_frequency + (diff_in_time - diff_in_frequency), current_frequency - diff_in_frequency
                    print("DESIRED < CURRENT: ", desired_frequency, desired_time)
                    print("MISSILE:", j)
                    mini += 1
                    print("MINI HERE", mini)
                    holder = j
                    break
                elif diff_in_frequency == 0:
                    if diff_in_frequency == 0 and (current_time + diff_in_time) <= desired_time:
                        j[0], j[1] = desired_time, desired_frequency
                        print("WHEN DIFF F == 0: ", j)
                        mini += 1
                        print("MINI IN ZERO", mini)
                        holder = j
                        break
        if len(holder) == 0:
            drop += 1
            make_another = i
            print("Created HIT: ", make_another)
            print("arr: ", arr)
            arr.append(make_another)
        print("IN FINISH: /", arr)
        print(mini)
    minimum_missiles = len(arr)
    print("FINALLY: ", minimum_missiles, "DROPPED: ", drop, "MINI: ", mini)

    return minimum_missiles




## Test Case 1 , 10 inputs , ## Expected Output:
"""defend([[65, 844],[70, 993],[201, 427],[348, 899],[388, 268],[440, 416],[459, 421],[459, 796],[744, 291],[870, 121]])
"""
## Test Case 2   19 inputs   ## Expected Output: 6
defend([
[5, 687],
[49, 338],
[63, 853],
[93, 150],
[129, 535],
[130, 831],
[140, 841],
[142, 591],
[144, 581],
[271, 594],
[271, 970],
[287, 495],
[294, 191],
[333, 150],
[488, 643],
[755, 816],
[816, 341],
[848, 779],
[880, 276]])

##Test Case 3    50 inputs   ##Expected Output: 9
"""defend([[29, 569],
[56, 667],
[73, 131],
[189, 550],
[208, 689],
[210, 76],
[223, 454],
[247, 329],
[251, 451],
[275, 660],
[283, 453],
[283, 89],
[289, 829],
[339, 197],
[343, 106],
[347, 715],
[350, 57],
[358, 299],
[362, 512],
[385, 405],
[401, 898],
[428, 862],
[439, 310],
[450, 83],
[464, 264],
[489, 770],
[546, 790],
[586, 325],
[664, 333],
[672, 210],
[678, 126],
[687, 496],
[707, 123],
[707, 813],
[711, 710],
[725, 758],
[735, 536],
[741, 820],
[799, 507],
[826, 865],
[837, 819],
[847, 53],
[860, 694],
[860, 909],
[893, 433],
[906, 446],
[958, 926],
[985, 127],
[991, 677],
[999, 261]])"""




##Test Case 4   100 inputs   ##Expected Output: 16
"""defend([[27, 490],
[31, 686],
[39, 614],
[47, 452],
[58, 730],
[73, 504],
[73, 260],
[77, 657],
[79, 901],
[109, 319],
[114, 905],
[125, 530],
[129, 657],
[136, 746],
[139, 211],
[155, 429],
[172, 113],
[177, 597],
[189, 376],
[194, 809],
[206, 795],
[215, 76],
[251, 972],
[253, 165],
[264, 880],
[269, 892],
[325, 932],
[328, 649],
[343, 18],
[344, 419],
[351, 251],
[374, 344],
[378, 598],
[386, 978],
[386, 772],
[400, 515],
[414, 424],
[414, 639],
[435, 366],
[438, 82],
[440, 637],
[445, 105],
[446, 387],
[450, 817],
[465, 865],
[477, 891],
[482, 204],
[495, 253],
[495, 353],
[499, 874],
[502, 939],
[506, 802],
[574, 922],
[645, 760],
[652, 698],
[680, 223],
[694, 918],
[700, 453],
[709, 314],
[714, 790],
[716, 232],
[735, 274],
[736, 511],
[769, 120],
[770, 144],
[772, 446],
[773, 205],
[775, 515],
[782, 143],
[797, 753],
[809, 636],
[812, 643],
[823, 121],
[825, 669],
[826, 545],
[827, 689],
[834, 608],
[847, 187],
[855, 946],
[856, 841],
[863, 192],
[871, 61],
[878, 171],
[903, 343],
[915, 874],
[919, 465],
[919, 449],
[928, 709],
[931, 490],
[940, 586],
[942, 586],
[951, 730],
[954, 914],
[970, 271],
[975, 359],
[978, 451],
[982, 94],
[984, 639],
[991, 340],
[995, 147]])"""
