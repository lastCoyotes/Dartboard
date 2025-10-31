import math

doublesdict = {
    50: "DB",
    40: "D20",
    38: "D19",
    36: "D18",
    34: "D17",
    32: "D16",
    30: "D15",
    28: "D14",
    26: "D13",
    24: "D12",
    22: "D11",
    20: "D10",
    18: "D9",
    16: "D8",
    14: "D7",
    12: "D6",
    10: "D5",
    8: "D4",
    6: "D3",
    4: "D2",
    2: "D1"
}

treblesdict = {
    60: "T20",
    57: "T19",
    54: "T18",
    51: "T17",
    48: "T16",
    45: "T15",
    42: "T14",
    39: "T13",
    36: "T12",
    33: "T11",
    30: "T10",
    27: "T9",
    24: "T8",
    21: "T7",
    18: "T6",
    15: "T5",
    12: "T4",
    9: "T3",
    6: "T2",
    3: "T1"
}

alldict = {
    60: ["T20"],
    57: ["T19"],
    54: ["T18"],
    51: ["T17"],
    50: ["DB"],
    48: ["T16"],
    45: ["T15"],
    42: ["T14"],
    40: ["D20"],
    39: ["T13"],
    38: ["D19"],
    36: ["D18", "T12"],
    34: ["D17"],
    33: ["T11"],
    32: ["D16"],
    30: ["D15", "T10"],
    28: ["D14"],
    27: ["T9"],
    26: ["D13"],
    25: ["B"],
    24: ["D12", "T8"],
    22: ["D11"],
    21: ["T7"],
    20: ["20", "D10"],
    19: ["19"],
    18: ["18", "D9", "T6"],
    17: ["17"],
    16: ["16", "D8"],
    15: ["15", "T5"],
    14: ["14", "D7"],
    13: ["13"],
    12: ["12", "D6", "T4"],
    11: ["11"],
    10: ["10", "D5"],
    9: ["9", "T3"],
    8: ["8", "D4"],
    7: ["7"],
    6: ["6", "D3", "T2"],
    5: ["5"],
    4: ["4", "D2"],
    3: ["3", "T1"],
    2: ["2", "D1"],
    1: ["1"]
}


def union(list1, list2, list3):
    final_list = list1 + list2 + list3
    return final_list


def first_sum(target, first_dart):
    # check again for posterity
    if target <= 170:
        if first_dart.is_knock_out or first_dart.is_bounce_out or first_dart.is_foul:
            first_score = 0
        else:
            first_score = first_dart.score
        target = target - first_score
        # we already have the first hit, so only find the largest double to checkout
        for i in doublesdict:
            new_target = target - i
            # if we can check out with only one double, do it
            if new_target == 0:
                if first_dart.is_double:
                    # print(doublesdict[first_dart.score], doublesdict[i], "")
                    return doublesdict[first_score], doublesdict[i], ""
                elif first_dart.is_triple:
                    # print(treblesdict[first_dart.score], doublesdict[i], "")
                    return treblesdict[first_score], doublesdict[i], ""
                else:
                    # print(first_dart.score, doublesdict[i], "")
                    return first_score, doublesdict[i], ""
            for j in alldict:
                if new_target >= 0:
                    second_target = new_target - j
                    # if k is too small to reach 0, then stop iterating and return to j loop
                    if second_target > 0:
                        break
                    # print(third_target)
                    # if i + j is the target, we've found our checkout
                    if second_target == 0:
                        if first_dart.is_double:
                            # print(doublesdict[first_dart.score], alldict[j][0], doublesdict[i])
                            return doublesdict[first_score], alldict[j][0], doublesdict[i]
                        elif first_dart.is_triple:
                            # print(treblesdict[first_dart.score], alldict[j][0], doublesdict[i])
                            return treblesdict[first_score], alldict[j][0], doublesdict[i]
                        else:
                            # print(first_dart.score, alldict[j][0], doublesdict[i])
                            return first_score, alldict[j][0], doublesdict[i]
        # print("First sum did not find a number.")
        return "", "", ""
    return "", "", ""


def second_sum(target, first_dart, second_dart):
    # again, check for posterity
    if target <= 170:
        if first_dart.is_knock_out or first_dart.is_bounce_out or first_dart.is_foul:
            first_score = 0
        else:
            first_score = first_dart.score
        if second_dart.is_knock_out or second_dart.is_bounce_out or second_dart.is_foul:
            second_score = 0
        else:
            second_score = second_dart.score
        # calculate the value remaining after the first and second hits
        target = target - first_score - second_score
        # iterate through all possible doubles to see if we can check out
        for i in doublesdict:
            new_target = target - i
            if new_target == 0:
                if first_dart.is_double:
                    if second_dart.is_double:
                        # print(doublesdict[first_dart.score], doublesdict[second_dart.score], doublesdict[i])
                        return doublesdict[first_score], doublesdict[second_score], doublesdict[i]
                    elif second_dart.is_triple:
                        # print(doublesdict[first_dart.score], treblesdict[second_dart.score], doublesdict[i])
                        return doublesdict[first_score], treblesdict[second_score], doublesdict[i]
                    else:
                        # print(doublesdict[first_dart.score], second_dart.score, doublesdict[i])
                        return doublesdict[first_score], second_score, doublesdict[i]
                elif first_dart.is_triple:
                    if second_dart.is_double:
                        # print(treblesdict[first_dart.score], doublesdict[second_dart.score], doublesdict[i])
                        return treblesdict[first_score], doublesdict[second_score], doublesdict[i]
                    elif second_dart.is_triple:
                        # print(treblesdict[first_dart.score], treblesdict[second_dart.score], doublesdict[i])
                        return treblesdict[first_score], treblesdict[second_score], doublesdict[i]
                    else:
                        # print(treblesdict[first_dart.score], second_dart.score, doublesdict[i])
                        return treblesdict[first_score], second_score, doublesdict[i]
                else:
                    if second_dart.is_double:
                        # print(first_dart.score, doublesdict[second_dart.score], doublesdict[i])
                        return first_score, doublesdict[second_score], doublesdict[i]
                    elif second_dart.is_triple:
                        # print(first_dart.score, treblesdict[second_dart.score], doublesdict[i])
                        return first_score, treblesdict[second_score], doublesdict[i]
                    else:
                        # print(first_dart.score, second_dart.score, doublesdict[i])
                        return first_score, second_score, doublesdict[i]
        # print("Second sum did not find a number.")
        return "", "", ""
    # print("Score is not <= 170")
    return "", "", ""


def initial_sum(target):
    # check to see if the starting score is below 170 to checkout
    if target <= 170:
        # find the largest double that will allow the checkout
        for i in doublesdict:
            new_target = target - i
            # if the largest double checks out, allow it
            if new_target == 0:
                # print(doublesdict[i], "", "")
                return doublesdict[i], "", ""
            # find the next largest number that will allow the checkout
            for j in alldict:
                if new_target >= 0:
                    second_target = new_target - j
                    if second_target == 0:
                        # if we can check out in two, do that
                        # print(alldict[j][0], doublesdict[i], "")
                        return alldict[j][0], doublesdict[i], ""
                    # same as above, but the second iteration
                    for k in alldict:
                        # make sure that we're not doing work for numbers that are already below 0
                        if second_target >= 0:
                            third_target = second_target - k
                            # if k is too small to reach 0, then stop iterating and return to j loop
                            if third_target > 0:
                                break
                            # # print(third_target)
                            # if i + j + k is the target, we've found our checkout
                            if third_target == 0:
                                # print(alldict[k][0], alldict[j][0], doublesdict[i])
                                return alldict[k][0], alldict[j][0], doublesdict[i]
        # print("Initial sum did not find a number.")
        return "", "", ""