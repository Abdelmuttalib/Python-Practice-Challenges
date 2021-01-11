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
    arr.append(initial_missile)
    initial = [0, 0]
    for i in missiles:
        place_h = initial_missile


        if i == initial_missile:
            print("INITIAL SUCCESS:", i, "AND", initial_missile)

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
                    holder = []

                    if (desired_t >= sec_current_t) and ((sec_current_f + sec_diff_f == desired_f) or (sec_current_f - sec_diff_f == desired_f)) and (sec_current_t + sec_diff_f <= desired_t):
                        if desired_f > sec_current_f:
                            arr[k][0] = sec_current_t + sec_diff_f + (sec_diff_t - sec_diff_f)
                            arr[k][1] = sec_current_f + sec_diff_f
                            print("AFTER ELSE --- DESIRED > CURRENT: ", desired_f, desired_t)
                            print("MISSILE:", arr[k])
                            holder = arr[k]
                            mini += 1
                            break
                        elif desired_f < sec_current_f:
                            arr[k][0] = sec_current_t + sec_diff_f + (sec_diff_t - sec_diff_f)
                            arr[k][1] = sec_current_f - sec_diff_f
                            print("AFTER ELSE --- DESIRED < CURRENT: ", desired_f, desired_t)
                            print("MISSILE:", arr[k])
                            holder = arr[k]
                            mini += 1
                            break
                        elif sec_diff_f == 0:
                            if sec_diff_f == 0 and (sec_current_t + sec_diff_t) <= desired_t:
                                arr[k][0] = desired_t
                                arr[k][1] = desired_f
                                print("WHEN DIFF F == 0: ", arr[k])
                                holder = arr[k]
                                mini += 1
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
                print("FINISH ???: ", arr, " \ ")

    minimum_missiles = len(arr)
    print("Last ANSWER: ", minimum_missiles)
    return minimum_missiles

    print("Mini: ",mini)
    print("ARR LENGTH: ", len(arr))
    print("FINAL ARR: ", arr)
## Test Case 1
#defend([[65, 844],[70, 993],[201, 427],[348, 899],[388, 268],[440, 416],[459, 421],[459, 796],[744, 291],[870, 121]])

## Test Case 2    ## Expected Output: 6
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

##Test Case 3    ##Expected Output: 16
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
