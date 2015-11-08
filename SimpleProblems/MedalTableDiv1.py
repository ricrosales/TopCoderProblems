'''
Problem Statement

The Olympic Games in Athens end tomorrow. Given the results
of the olympic disciplines, generate and return the medal table.

The results of the disciplines are given as a String[] results,
where each element is in the format "GGG SSS BBB". GGG, SSS and
BBB are the 3-letter country codes (three capital letters from 'A'
to 'Z') of the countries winning the gold, silver and bronze medal,
respectively.

The medal table is a String[] with an element for each country
appearing in results. Each element has to be in the format "CCO G
S B" (quotes for clarity), where G, S and B are the number of gold,
silver and bronze medals won by country CCO, e.g. "AUT 1 4 1". The
numbers should not have any extra leading zeros.

Sort the elements by the number of gold medals won in decreasing order.
If several countries are tied, sort the tied countries by the number
of silver medals won in decreasing order. If some countries are still
tied, sort the tied countries by the number of bronze medals won in
decreasing order. If a tie still remains, sort the tied countries by
their 3-letter code in ascending alphabetical order.


Definition

Class:	MedalTable
Method:	generate
Parameters:	String[]
Returns:	String[]
Method signature:	String[] generate(String[] results)
(be sure your method is public)


Constraints

-	results contains between 1 and 50 elements, inclusive.
-	Each element of results is formatted as described in the problem statement.
-	No more than 50 different countries appear in results.

Examples

0)

{"ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"}
Returns:
{ "KOR 3 1 0",
 "ITA 1 0 0",
 "TPE 0 1 1",
 "CHN 0 1 0",
 "JPN 0 1 0",
 "AUS 0 0 1",
 "GBR 0 0 1",
 "UKR 0 0 1" }
These are the results of the archery competitions.

1)

{"USA AUT ROM"}
Returns: { "USA 1 0 0",  "AUT 0 1 0",  "ROM 0 0 1" }

2)

{"GER AUT SUI", "AUT SUI GER", "SUI GER AUT"}
Returns: { "AUT 1 1 1",  "GER 1 1 1",  "SUI 1 1 1" }

'''


class MedalTable:

    @staticmethod
    def generate(results):
        d = {}

        for i in results:
            if i[:3] in d:
                if 'g' in d[i[:3]]:
                    d[i[:3]]['g'] += 1
                else:
                    d[i[:3]]['g'] = 1
            else:
                d[i[:3]] = {'g': 0, 's': 0, 'b': 0}
                d[i[:3]]['g'] = 1

            if i[4:7] in d:
                if 's' in d[i[:3]]:
                    d[i[4:7]]['s'] += 1
                else:
                    d[i[4:7]]['s'] = 1
            else:
                d[i[4:7]] = {'g': 0, 's': 0, 'b': 0}
                d[i[4:7]]['s'] = 1

            if i[8:] in d:
                if 'b' in d[i[:3]]:
                    d[i[8:]]['b'] += 1
                else:
                    d[i[8:]]['b'] = 1
            else:
                d[i[8:]] = {'g': 0, 's': 0, 'b': 0}
                d[i[8:]]['b'] = 1

        k = list(d.keys())
        MedalTable.mergesort(k, d)
        # print(d)

        output = []
        for i in k:
            output.append(i + ' ' + str(d[i]['g']) +
                          ' ' + str(d[i]['s']) +
                          ' ' + str(d[i]['b']))
        return output


    @staticmethod
    def greater_than(a, b, d):
        if d[a]['g'] > d[b]['g']:
            return True
        elif d[a]['g'] == d[b]['g']:
            if d[a]['s'] > d[b]['s']:
                return True
            elif d[a]['s'] == d[b]['s']:
                if d[a]['b'] > d[b]['b']:
                    return True
                elif d[a]['b'] == d[b]['b']:
                    if ord(a[0]) < ord(b[0]):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    @staticmethod
    def mergesort(alist, d):
        if len(alist) > 1:
            mid = len(alist) // 2
            left_list = alist[:mid]
            right_list = alist[mid:]
            MedalTable.mergesort(left_list, d)
            MedalTable.mergesort(right_list, d)
            i = 0
            j = 0
            k = 0
            while i < len(left_list) and j < len(right_list):
                if MedalTable.greater_than(left_list[i], right_list[j], d):
                    alist[k] = left_list[i]
                    i += 1
                else:
                    alist[k] = right_list[j]
                    j += 1
                k += 1

            while i < len(left_list):
                alist[k] = left_list[i]
                i += 1
                k += 1

            while j < len(right_list):
                alist[k] = right_list[j]
                j += 1
                k += 1


if __name__ == '__main__':

    # l = ["GER AUT SUI", "AUT SUI GER", "SUI GER AUT"]
    # l = ["USA AUT ROM"]
    l = ["ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"]
    mt = MedalTable()
    print(mt.generate(l))