from backend.models import *


def sixtylistinit(n):
    listofsixties = [60] * (n - 1)
    listofsixties.append(50)
    return listofsixties


def fewestdartschecker(hits, first, second, third, leg, score):
    darts_sum = 0
    checkout_sum = 0
    prev_darts_sum = 0

    if leg == 801:
        max_darts = 14
    elif leg == 501:
        max_darts = 9
    elif leg == 301:
        max_darts = 6
    else:
        print("Invalid leg value.")
        return

    fewestdartslist = sixtylistinit(max_darts)
    # now we have a list of max_darts size, all valued at 60, minus the last which is the highest double - 50

    if len(hits) <= max_darts:
        for i in range(len(hits)):
            if hits[i].is_knock_out or hits[i].is_bounce_out or hits[i].is_foul:
                fewestdartslist[i] = 0
            else:
                fewestdartslist[i] = hits[i].score
    else:
        return False

    print(fewestdartslist)
    print(len(hits))

    for i in fewestdartslist:
        darts_sum += i

    # if len(fewestdartslist) == 6:

    # print(leg - darts_sum)

    if leg == 501 or leg == 301:
        print(score)
        if leg - darts_sum <= 0 and score >= 0:
            if len(hits) >= max_darts - 3:
                print(second)
                if second == "":
                    return False
                elif second != "" and len(hits) >= max_darts:
                    return False

                """
                for i in hits:
                    checkout_sum += i
                if leg - checkout_sum == 169 or leg - checkout_sum == 168 or leg - checkout_sum == 166 or\
                        leg - checkout_sum == 165 or leg - checkout_sum == 163 or leg - checkout_sum == 162 or\
                        leg - checkout_sum == 159:
                    return False
                """
            return True
        else:
            return False
    else:  # leg is == 801
        if leg - darts_sum <= 0 and score >= 0:
            if len(hits) == max_darts - 2:
                if third != "":
                    return False

                """
                for i in hits:
                    checkout_sum += i
                if leg - checkout_sum == 109 or leg - checkout_sum == 108 or leg - checkout_sum == 106 or \
                        leg - checkout_sum == 105 or leg - checkout_sum == 103 or leg - checkout_sum == 102 or \
                        leg - checkout_sum == 99:
                    return False
            elif 14 - 2 <= len(hits) <= 14:
                for i in range(12, len(hits)):
                    prev_darts_sum += i
                if darts_sum - prev_darts_sum == 109 or darts_sum - prev_darts_sum == 108 or \
                        darts_sum - prev_darts_sum == 106 or darts_sum - prev_darts_sum == 105 or \
                        darts_sum - prev_darts_sum == 103 or darts_sum - prev_darts_sum == 102 or \
                        darts_sum - prev_darts_sum == 99:
                    return False
                """

            return True
    return False
