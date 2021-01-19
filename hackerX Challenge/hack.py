def defend(missiles):
    arr = []
    holder = []
    mini = 0

    for i in range(len(missiles)):
        holder = []

        for j in range(len(arr)):
            print("arr: ", arr)
            print("MISS: ", missiles[i])
            print("ARR INDEX: ", arr[j])
            current_t, current_f = arr[j][0], arr[j][1]
            print("CURRENT T & F: ", current_t, current_f)
            desired_t, desired_f = missiles[i][0], missiles[i][1]
            print("DESIRED T & F: ", desired_t, desired_f)
            diff_t, diff_f = abs(desired_t - current_t), abs(desired_f - current_f)
            print("DIFF's T & F: ", diff_t, "|", diff_f)

            if len(arr) == 0:
                holder = []
                break

            elif arr[j] == missiles[i]:
                print("INITIAL SUCCESS: ", arr[j], "AND", missiles[i])
                holder = arr[j]
                break

            elif (desired_t >= current_t) and ((current_f + diff_f == desired_f) or (current_f - diff_f == desired_f)) and (current_t + diff_f <= desired_t):
                if desired_f > current_f:
                    arr[j][0], arr[j][1] = current_t + diff_f + (diff_t - diff_f), current_f + diff_f
                    print("DESIRED > CURRENT: ", desired_f, desired_t)
                    print("MISSILE:", arr[j])
                    holder = arr[j]
                    break
                elif desired_f < current_f:
                    arr[j][0], arr[j][1] = current_t + diff_f + (diff_t - diff_f), current_f - diff_f
                    print("DESIRED < CURRENT: ", desired_f, desired_t)
                    print("MISSILE:", arr[j])
                    holder = arr[j]
                    break
                elif diff_f == 0:
                    if diff_f == 0 and (current_t + diff_t) <= desired_t:
                        arr[j][0], arr[j][1] = desired_t, desired_f
                        print("WHEN DIFF F == 0: ", arr[j])
                        holder = arr[j]
                        break
        if len(holder) == 0:
            mini += 1
            make_another = missiles[i]
            print("Created HIT: ", make_another)
            print("arr: ", arr)
            arr.append(make_another)
        print("IN FINISH: /", arr)
        print(mini)
    minimum_missiles = len(arr)
    print("FINALLY: ", minimum_missiles)
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

"""defend([[65, 844],[70, 993],[201, 427],[348, 899],[388, 268],[440, 416],[459, 421],[459, 796],[744, 291],[870, 121]])
"""
