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
