## CHALLENGE QUESTION
"""
Update: A slight modification in the problem statement (see below)

Evil Nation A is angry and plans to launch N guided-missiles at the peaceful Nation B in an attempt to wipe out all of Nation B's people.
 Nation A's missile i will arrive in nation B at time ti.
  Missile i communicates with its headquarters by unique radio signals with a frequency equal to fi.
  Can you help the peaceful Nation B survive by building a defensive system that will stop the missiles dead in the sky?

Defensive system:

The only way to defend Nation B from the attacking missile is by counter attacking them with a hackerX missile.
 You have a lot of hackerX missiles and each one of them has its own radio frequency.
  An individual hackerX missile can destroy Evil Nation A’s attacking missile if the radio frequency of both of the missiles match.
   Each hackerX missile can be used an indefinite number of times. Its invincible and doesn't get destroyed in the collision.

The good news is you can adjust the frequency of the hackerX missile to match the evil missiles' frequency.
When changing the hackerX missile's initial frequency fA to the new defending frequency fB, you will need \|fB - fA\| units of time to do.


If two evil missles with same frequency arrive at the same time, we can destroy them both with one hackerX missile.
 You can set the frequency of a hackerX missile to any value when its fired.

What is the minimum number of hackerX missiles you must launch to keep Nation B safe?

Input Format:
The first line contains a single integer N denoting the number of missiles.
This is followed by N lines each containing two integers ti and fi denoting the time & frequency of the ith missile.

Output Format:
A single integer denoting the minimum number of hackerX missiles you need to defend the nation.

Constraints:
1 <= N <= 100000
0 <= ti <= 100000
0 <= fi <= 100000
t1 <= t2 <= ... <= tN

Sample Input #00

4
1 1
2 2
3 1
5 1
Sample Output #00

1
Explanation #00

A HackerX missile is launched at t = 1 with a frequency f = 1,
and destroys the first missile. It re-tunes its frequency to f = 2 in 1 unit of time,
and destroys the missile that is going to hit Nation B at t = 2.
It re-tunes its frequency back to 1 in 1 unit of time and destroys the missile that is going to hit the nation at t = 3.
 It is relaunched at t = 5 with f = 1 and destroys the missile that is going to hit nation B at t = 5. Hence,
 you need only 1 HackerX to protect nation B.

Sample Input #01

4
1 1
2 3
3 1
5 1
Sample Output #01

2
Explanation #01

Destroy 1 missile at t = 1, f = 1. now at t = 2, there is a missile with frequency 3.
The launched missile takes 2 units of time to destroy this, hence we need a new hackerX missile to destroy this one.
The first hackerX missile can destroy the 3rd missile which has the same frequency as itself.
The same hackerX missile destroys the missile that is hitting its city at t = 5. Thus, we need atleast 2 hackerX missiles.
"""

    ######### SOLUTION CODE #########


def defend(missiles):
    mini = 1
    initial_missile = missiles[0]
    arr = []
    initial = [0, 0]
    chalk = 0
    for i in missiles:

        if i == initial_missile:
            print("INITIAL SUCCESS:", i, "AND", initial_missile)
            chalk += 1
            arr.append(initial_missile)

        else:
            print("i VALUE", i)
            current_t, current_f = initial_missile[0], initial_missile[1]
            desired_t, desired_f = i[0], i[1]
            print("CURRENT: ", current_t, current_f)
            print("DESIRED: ", desired_t, desired_f)

            diff_t, diff_f = abs(desired_t - current_t), abs(desired_f - current_f)
            print("DIFF T&F: ", diff_t, diff_f)


            if (desired_t >= current_t) and ((current_f + diff_f == desired_f) or (current_f - diff_f == desired_f)) and (current_t + diff_f <= desired_t):
                if desired_f > current_f:
                    initial[0], initial[1] = current_t + diff_f + (diff_t - diff_f), current_f + diff_f
                    initial_missile[0], initial_missile[1] = initial[0], initial[1]
                    print("DESIRED > CURRENT: ", desired_f, desired_t)
                    print("MISSILE:", initial)
                    mini += 1
                    print("MINI, ", mini)
                elif desired_f < current_f:
                    initial[0], initial[1] = current_t + diff_f + (diff_t - diff_f), current_f - diff_f
                    initial_missile[0], initial_missile[1] = initial[0], initial[1]
                    print("DESIRED < CURRENT: ", desired_f, desired_t)
                    print("MISSILE:", initial)
                    mini += 1
                    print("MINI, ", mini)
                elif diff_f == 0:
                    if diff_f == 0 and (current_t + diff_t <= desired_t):
                        initial[1] = desired_f
                        initial[0] = desired_t
                        initial_missile[0], initial_missile[1] = initial[0], initial[1]
                        mini += 1
                    elif diff_t == 0:
                        print("NO, SAME TIMING. MISSED")
                    elif diff_t == 0 and diff_f == 0:
                        print("BOTH DIFF's ZEROS")
            else:
                for k in range(len(arr)):
                    print("KKKK: ", arr[k])
                    sec_current_t, sec_current_f = arr[k][0], arr[k][1]
                    print("CHECK ARR: ", arr)
                    print("SEC CURRENT T: ", sec_current_t, "SEC CURRENT F: ", sec_current_f)
                    print("DIFF F: ", diff_f)
                    sec_diff_t, sec_diff_f = abs(sec_current_t - desired_t), abs(sec_current_f - desired_f)
                    print("SEC DIFF F: ", sec_diff_f, "SEC DIFF T: ", sec_diff_t)

                    holder = []

                    if (desired_t >= sec_current_t) and ((sec_current_f + sec_diff_f == desired_f) or (sec_current_f - sec_diff_f == desired_f)) and (sec_current_t + sec_diff_f <= desired_t):
                        if desired_f > sec_current_f:
                            arr[k][0] = sec_current_t + sec_diff_f + (sec_diff_t - sec_diff_f)
                            arr[k][1] = sec_current_f + sec_diff_f
                            print("AFTER ELSE --- DESIRED > CURRENT: ", desired_f, desired_t)
                            print("MISSILE:", arr[k])
                            holder = arr[k]
                            break
                        elif desired_f < sec_current_f:
                            arr[k][0] = sec_current_t + sec_diff_f + (sec_diff_t - sec_diff_f)
                            arr[k][1] = sec_current_f - sec_diff_f
                            print("AFTER ELSE --- DESIRED < CURRENT: ", desired_f, desired_t)
                            print("MISSILE:", arr[k])
                            holder = arr[k]
                            break
                        elif sec_diff_f == 0:
                            if sec_diff_f == 0 and (sec_current_t + sec_diff_t) <= desired_t:
                                arr[k][0] = desired_t
                                arr[k][1] = desired_f
                                print("WHEN DIFF F == 0: ", arr[k])
                                holder = arr[k]
                                break
                            else:
                                holder = []
                                break
                    else:
                        pass

                if len(holder) == 0:
                    make_another = i
                    print("Created HIT: ", make_another)
                    print("arr: ", arr)
                    arr.append(make_another)
                    chalk += 1
                print("FINISH ???: ", arr, " \ ")

    minimum_missiles = len(arr)
    print("Last ANSWER: ", minimum_missiles)
    print("LAST chalk: ", chalk)
    return minimum_missiles

    print("Mini: ",mini)
    print("ARR LENGTH: ", len(arr))
    print("FINAL ARR: ", arr)
## Test Case 1 , 10 inputs , ## Expected Output:
defend([[65, 844],[70, 993],[201, 427],[348, 899],[388, 268],[440, 416],[459, 421],[459, 796],[744, 291],[870, 121]])

## Test Case 2   19 inputs   ## Expected Output: 6
"""defend([
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
[880, 276]])"""

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


"""
Created HIT:  [5, 687]
arr:  []
IN FINISH: / [[5, 687]]
arr:  [[5, 687]]
MISS:  [49, 338]
ARR INDEX:  [5, 687]
CURRENT T & F:  5 687
DESIRED T & F:  49 338
DIFF's T & F:  44 | 349
Created HIT:  [49, 338]
arr:  [[5, 687]]
IN FINISH: / [[5, 687], [49, 338]]
arr:  [[5, 687], [49, 338]]
MISS:  [63, 853]
ARR INDEX:  [5, 687]
CURRENT T & F:  5 687
DESIRED T & F:  63 853
DIFF's T & F:  58 | 166
arr:  [[5, 687], [49, 338]]
MISS:  [63, 853]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  63 853
DIFF's T & F:  14 | 515
Created HIT:  [63, 853]
arr:  [[5, 687], [49, 338]]
IN FINISH: / [[5, 687], [49, 338], [63, 853]]
arr:  [[5, 687], [49, 338], [63, 853]]
MISS:  [93, 150]
ARR INDEX:  [5, 687]
CURRENT T & F:  5 687
DESIRED T & F:  93 150
DIFF's T & F:  88 | 537
arr:  [[5, 687], [49, 338], [63, 853]]
MISS:  [93, 150]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  93 150
DIFF's T & F:  44 | 188
arr:  [[5, 687], [49, 338], [63, 853]]
MISS:  [93, 150]
ARR INDEX:  [63, 853]
CURRENT T & F:  63 853
DESIRED T & F:  93 150
DIFF's T & F:  30 | 703
Created HIT:  [93, 150]
arr:  [[5, 687], [49, 338], [63, 853]]
IN FINISH: / [[5, 687], [49, 338], [63, 853], [93, 150]]
arr:  [[5, 687], [49, 338], [63, 853], [93, 150]]
MISS:  [129, 535]
ARR INDEX:  [5, 687]
CURRENT T & F:  5 687
DESIRED T & F:  129 535
DIFF's T & F:  124 | 152
arr:  [[5, 687], [49, 338], [63, 853], [93, 150]]
MISS:  [129, 535]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  129 535
DIFF's T & F:  80 | 197
arr:  [[5, 687], [49, 338], [63, 853], [93, 150]]
MISS:  [129, 535]
ARR INDEX:  [63, 853]
CURRENT T & F:  63 853
DESIRED T & F:  129 535
DIFF's T & F:  66 | 318
arr:  [[5, 687], [49, 338], [63, 853], [93, 150]]
MISS:  [129, 535]
ARR INDEX:  [93, 150]
CURRENT T & F:  93 150
DESIRED T & F:  129 535
DIFF's T & F:  36 | 385
Created HIT:  [129, 535]
arr:  [[5, 687], [49, 338], [63, 853], [93, 150]]
IN FINISH: / [[5, 687], [49, 338], [63, 853], [93, 150], [129, 535]]
arr:  [[5, 687], [49, 338], [63, 853], [93, 150], [129, 535]]
MISS:  [130, 831]
ARR INDEX:  [5, 687]
CURRENT T & F:  5 687
DESIRED T & F:  130 831
DIFF's T & F:  125 | 144
arr:  [[5, 687], [49, 338], [63, 853], [93, 150], [129, 535]]
MISS:  [130, 831]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  130 831
DIFF's T & F:  81 | 493
arr:  [[5, 687], [49, 338], [63, 853], [93, 150], [129, 535]]
MISS:  [130, 831]
ARR INDEX:  [63, 853]
CURRENT T & F:  63 853
DESIRED T & F:  130 831
DIFF's T & F:  67 | 22
DESIRED < CURRENT:  831 130
MISSILE: [130, 831]
IN FINISH: / [[5, 687], [49, 338], [130, 831], [93, 150], [129, 535]]
arr:  [[5, 687], [49, 338], [130, 831], [93, 150], [129, 535]]
MISS:  [140, 841]
ARR INDEX:  [5, 687]
CURRENT T & F:  5 687
DESIRED T & F:  140 841
DIFF's T & F:  135 | 154
arr:  [[5, 687], [49, 338], [130, 831], [93, 150], [129, 535]]
MISS:  [140, 841]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  140 841
DIFF's T & F:  91 | 503
arr:  [[5, 687], [49, 338], [130, 831], [93, 150], [129, 535]]
MISS:  [140, 841]
ARR INDEX:  [130, 831]
CURRENT T & F:  130 831
DESIRED T & F:  140 841
DIFF's T & F:  10 | 10
DESIRED > CURRENT:  841 140
MISSILE: [140, 841]
IN FINISH: / [[5, 687], [49, 338], [140, 841], [93, 150], [129, 535]]
arr:  [[5, 687], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [142, 591]
ARR INDEX:  [5, 687]
CURRENT T & F:  5 687
DESIRED T & F:  142 591
DIFF's T & F:  137 | 96
DESIRED < CURRENT:  591 142
MISSILE: [142, 591]
IN FINISH: / [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
arr:  [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [144, 581]
ARR INDEX:  [142, 591]
CURRENT T & F:  142 591
DESIRED T & F:  144 581
DIFF's T & F:  2 | 10
arr:  [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [144, 581]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  144 581
DIFF's T & F:  95 | 243
arr:  [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [144, 581]
ARR INDEX:  [140, 841]
CURRENT T & F:  140 841
DESIRED T & F:  144 581
DIFF's T & F:  4 | 260
arr:  [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [144, 581]
ARR INDEX:  [93, 150]
CURRENT T & F:  93 150
DESIRED T & F:  144 581
DIFF's T & F:  51 | 431
arr:  [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [144, 581]
ARR INDEX:  [129, 535]
CURRENT T & F:  129 535
DESIRED T & F:  144 581
DIFF's T & F:  15 | 46
IN FINISH: / [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
arr:  [[142, 591], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [271, 594]
ARR INDEX:  [142, 591]
CURRENT T & F:  142 591
DESIRED T & F:  271 594
DIFF's T & F:  129 | 3
DESIRED > CURRENT:  594 271
MISSILE: [271, 594]
IN FINISH: / [[271, 594], [49, 338], [140, 841], [93, 150], [129, 535]]
arr:  [[271, 594], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [271, 970]
ARR INDEX:  [271, 594]
CURRENT T & F:  271 594
DESIRED T & F:  271 970
DIFF's T & F:  0 | 376
arr:  [[271, 594], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [271, 970]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  271 970
DIFF's T & F:  222 | 632
arr:  [[271, 594], [49, 338], [140, 841], [93, 150], [129, 535]]
MISS:  [271, 970]
ARR INDEX:  [140, 841]
CURRENT T & F:  140 841
DESIRED T & F:  271 970
DIFF's T & F:  131 | 129
DESIRED > CURRENT:  970 271
MISSILE: [271, 970]
IN FINISH: / [[271, 594], [49, 338], [271, 970], [93, 150], [129, 535]]
arr:  [[271, 594], [49, 338], [271, 970], [93, 150], [129, 535]]
MISS:  [287, 495]
ARR INDEX:  [271, 594]
CURRENT T & F:  271 594
DESIRED T & F:  287 495
DIFF's T & F:  16 | 99
arr:  [[271, 594], [49, 338], [271, 970], [93, 150], [129, 535]]
MISS:  [287, 495]
ARR INDEX:  [49, 338]
CURRENT T & F:  49 338
DESIRED T & F:  287 495
DIFF's T & F:  238 | 157
DESIRED > CURRENT:  495 287
MISSILE: [287, 495]
IN FINISH: / [[271, 594], [287, 495], [271, 970], [93, 150], [129, 535]]
arr:  [[271, 594], [287, 495], [271, 970], [93, 150], [129, 535]]
MISS:  [294, 191]
ARR INDEX:  [271, 594]
CURRENT T & F:  271 594
DESIRED T & F:  294 191
DIFF's T & F:  23 | 403
arr:  [[271, 594], [287, 495], [271, 970], [93, 150], [129, 535]]
MISS:  [294, 191]
ARR INDEX:  [287, 495]
CURRENT T & F:  287 495
DESIRED T & F:  294 191
DIFF's T & F:  7 | 304
arr:  [[271, 594], [287, 495], [271, 970], [93, 150], [129, 535]]
MISS:  [294, 191]
ARR INDEX:  [271, 970]
CURRENT T & F:  271 970
DESIRED T & F:  294 191
DIFF's T & F:  23 | 779
arr:  [[271, 594], [287, 495], [271, 970], [93, 150], [129, 535]]
MISS:  [294, 191]
ARR INDEX:  [93, 150]
CURRENT T & F:  93 150
DESIRED T & F:  294 191
DIFF's T & F:  201 | 41
DESIRED > CURRENT:  191 294
MISSILE: [294, 191]
IN FINISH: / [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
arr:  [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [333, 150]
ARR INDEX:  [271, 594]
CURRENT T & F:  271 594
DESIRED T & F:  333 150
DIFF's T & F:  62 | 444
arr:  [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [333, 150]
ARR INDEX:  [287, 495]
CURRENT T & F:  287 495
DESIRED T & F:  333 150
DIFF's T & F:  46 | 345
arr:  [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [333, 150]
ARR INDEX:  [271, 970]
CURRENT T & F:  271 970
DESIRED T & F:  333 150
DIFF's T & F:  62 | 820
arr:  [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [333, 150]
ARR INDEX:  [294, 191]
CURRENT T & F:  294 191
DESIRED T & F:  333 150
DIFF's T & F:  39 | 41
arr:  [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [333, 150]
ARR INDEX:  [129, 535]
CURRENT T & F:  129 535
DESIRED T & F:  333 150
DIFF's T & F:  204 | 385
IN FINISH: / [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
arr:  [[271, 594], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [488, 643]
ARR INDEX:  [271, 594]
CURRENT T & F:  271 594
DESIRED T & F:  488 643
DIFF's T & F:  217 | 49
DESIRED > CURRENT:  643 488
MISSILE: [488, 643]
IN FINISH: / [[488, 643], [287, 495], [271, 970], [294, 191], [129, 535]]
arr:  [[488, 643], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [755, 816]
ARR INDEX:  [488, 643]
CURRENT T & F:  488 643
DESIRED T & F:  755 816
DIFF's T & F:  267 | 173
DESIRED > CURRENT:  816 755
MISSILE: [755, 816]
IN FINISH: / [[755, 816], [287, 495], [271, 970], [294, 191], [129, 535]]
arr:  [[755, 816], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [816, 341]
ARR INDEX:  [755, 816]
CURRENT T & F:  755 816
DESIRED T & F:  816 341
DIFF's T & F:  61 | 475
arr:  [[755, 816], [287, 495], [271, 970], [294, 191], [129, 535]]
MISS:  [816, 341]
ARR INDEX:  [287, 495]
CURRENT T & F:  287 495
DESIRED T & F:  816 341
DIFF's T & F:  529 | 154
DESIRED < CURRENT:  341 816
MISSILE: [816, 341]
IN FINISH: / [[755, 816], [816, 341], [271, 970], [294, 191], [129, 535]]
arr:  [[755, 816], [816, 341], [271, 970], [294, 191], [129, 535]]
MISS:  [848, 779]
ARR INDEX:  [755, 816]
CURRENT T & F:  755 816
DESIRED T & F:  848 779
DIFF's T & F:  93 | 37
DESIRED < CURRENT:  779 848
MISSILE: [848, 779]
IN FINISH: / [[848, 779], [816, 341], [271, 970], [294, 191], [129, 535]]
arr:  [[848, 779], [816, 341], [271, 970], [294, 191], [129, 535]]
MISS:  [880, 276]
ARR INDEX:  [848, 779]
CURRENT T & F:  848 779
DESIRED T & F:  880 276
DIFF's T & F:  32 | 503
arr:  [[848, 779], [816, 341], [271, 970], [294, 191], [129, 535]]
MISS:  [880, 276]
ARR INDEX:  [816, 341]
CURRENT T & F:  816 341
DESIRED T & F:  880 276
DIFF's T & F:  64 | 65
arr:  [[848, 779], [816, 341], [271, 970], [294, 191], [129, 535]]
MISS:  [880, 276]
ARR INDEX:  [271, 970]
CURRENT T & F:  271 970
DESIRED T & F:  880 276
DIFF's T & F:  609 | 694
arr:  [[848, 779], [816, 341], [271, 970], [294, 191], [129, 535]]
MISS:  [880, 276]
ARR INDEX:  [294, 191]
CURRENT T & F:  294 191
DESIRED T & F:  880 276
DIFF's T & F:  586 | 85
DESIRED > CURRENT:  276 880
MISSILE: [880, 276]
IN FINISH: / [[848, 779], [816, 341], [271, 970], [880, 276], [129, 535]]
FINALLY:  5
"""
