# This is the Main File

import Functions

if __name__ == "__main__":
    filename = 'players_stats.csv'
    test_data, training_data = Functions.loadDataset(filename)

    print("The program will show different results due to different k values: ")
    print()

    k = 5
    print('1. When k is', k)
    predictions1 = []
    matched = 0
    unmatched = 0

    PG_PG = 0
    PG_SG = 0
    PG_SF = 0
    PG_PF = 0
    PG_C = 0

    SG_PG = 0
    SG_SG = 0
    SG_SF = 0
    SG_PF = 0
    SG_C = 0

    SF_PG = 0
    SF_SG = 0
    SF_SF = 0
    SF_PF = 0
    SF_C = 0

    PF_PG = 0
    PF_SG = 0
    PF_SF = 0
    PF_PF = 0
    PF_C = 0

    C_PG = 0
    C_SG = 0
    C_SF = 0
    C_PF = 0
    C_C = 0

    for x in range(len(test_data)):
        neighbors = Functions.getNeighbors(training_data, test_data[x], k)
        result = Functions.getResponse(neighbors)
        predictions1.append(result)

        if repr(result) == repr('PG'):
            if repr(test_data[x][-1]) == repr('PG'):
                PG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PG_C += 1
        elif repr(result) == repr('SG'):
            if repr(test_data[x][-1]) == repr('PG'):
                SG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SG_C += 1
        elif repr(result) == repr('SF'):
            if repr(test_data[x][-1]) == repr('PG'):
                SF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SF_C += 1
        elif repr(result) == repr('PF'):
            if repr(test_data[x][-1]) == repr('PG'):
                PF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PF_C += 1
        elif repr(result) == repr('C'):
            if repr(test_data[x][-1]) == repr('PG'):
                C_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                C_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                C_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                C_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                C_C += 1

        if repr(result) != repr(test_data[x][-1]):
            unmatched += 1
        else:
            matched += 1
        # print('predicted = ' + repr(result) + ', actual = ' + repr(test_data[x][-1]))

    accuracy = Functions.getAccuracy(test_data, predictions1)

    # draw the table
    print("Table: (first row is the predicted values, first column is actual values)")
    print("\tPG\tSG\tSF\tPF\tC")
    print("PG\t%d\t%d\t%d\t%d\t%d" % (PG_PG, SG_PG, SF_PG, PF_PG, C_PG))
    print("SG\t%d\t%d\t%d\t%d\t%d" % (PG_SG, SG_SG, SF_SG, PF_SG, C_SG))
    print("SF\t%d\t%d\t%d\t%d\t%d" % (PG_SF, SG_SF, SF_SF, PF_SF, C_SF))
    print("PF\t%d\t%d\t%d\t%d\t%d" % (PG_PF, SG_PF, SF_PF, PF_PF, C_PF))
    print("C\t%d\t%d\t%d\t%d\t%d" % (PG_C, SG_C, SF_C, PF_C, C_C))
    print()
    print('Total test data:', (matched + unmatched))
    print('Matched:', matched, 'Unmatched:', unmatched)
    print('Accuracy: ' + repr(accuracy) + '%')
    print()

    k = 10
    print('2. When k is', k)
    predictions2 = []
    matched = 0
    unmatched = 0

    PG_PG = 0
    PG_SG = 0
    PG_SF = 0
    PG_PF = 0
    PG_C = 0

    SG_PG = 0
    SG_SG = 0
    SG_SF = 0
    SG_PF = 0
    SG_C = 0

    SF_PG = 0
    SF_SG = 0
    SF_SF = 0
    SF_PF = 0
    SF_C = 0

    PF_PG = 0
    PF_SG = 0
    PF_SF = 0
    PF_PF = 0
    PF_C = 0

    C_PG = 0
    C_SG = 0
    C_SF = 0
    C_PF = 0
    C_C = 0

    for x in range(len(test_data)):
        neighbors = Functions.getNeighbors(training_data, test_data[x], k)
        result = Functions.getResponse(neighbors)
        predictions2.append(result)

        if repr(result) == repr('PG'):
            if repr(test_data[x][-1]) == repr('PG'):
                PG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PG_C += 1
        elif repr(result) == repr('SG'):
            if repr(test_data[x][-1]) == repr('PG'):
                SG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SG_C += 1
        elif repr(result) == repr('SF'):
            if repr(test_data[x][-1]) == repr('PG'):
                SF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SF_C += 1
        elif repr(result) == repr('PF'):
            if repr(test_data[x][-1]) == repr('PG'):
                PF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PF_C += 1
        elif repr(result) == repr('C'):
            if repr(test_data[x][-1]) == repr('PG'):
                C_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                C_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                C_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                C_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                C_C += 1

        if repr(result) != repr(test_data[x][-1]):
            unmatched += 1
        else:
            matched += 1
        # print('predicted = ' + repr(result) + ', actual = ' + repr(test_data[x][-1]))
    accuracy = Functions.getAccuracy(test_data, predictions2)

    # draw the table
    print("Table: (first row is the predicted values, first column is actual values)")
    print("\tPG\tSG\tSF\tPF\tC")
    print("PG\t%d\t%d\t%d\t%d\t%d" % (PG_PG, SG_PG, SF_PG, PF_PG, C_PG))
    print("SG\t%d\t%d\t%d\t%d\t%d" % (PG_SG, SG_SG, SF_SG, PF_SG, C_SG))
    print("SF\t%d\t%d\t%d\t%d\t%d" % (PG_SF, SG_SF, SF_SF, PF_SF, C_SF))
    print("PF\t%d\t%d\t%d\t%d\t%d" % (PG_PF, SG_PF, SF_PF, PF_PF, C_PF))
    print("C\t%d\t%d\t%d\t%d\t%d" % (PG_C, SG_C, SF_C, PF_C, C_C))
    print()
    print('Total test data:', (matched + unmatched))
    print('Matched:', matched, 'Unmatched:', unmatched)
    print('Accuracy: ' + repr(accuracy) + '%')
    print()

    k = 15
    print('3. When k is', k)
    predictions3 = []
    matched = 0
    unmatched = 0

    PG_PG = 0
    PG_SG = 0
    PG_SF = 0
    PG_PF = 0
    PG_C = 0

    SG_PG = 0
    SG_SG = 0
    SG_SF = 0
    SG_PF = 0
    SG_C = 0

    SF_PG = 0
    SF_SG = 0
    SF_SF = 0
    SF_PF = 0
    SF_C = 0

    PF_PG = 0
    PF_SG = 0
    PF_SF = 0
    PF_PF = 0
    PF_C = 0

    C_PG = 0
    C_SG = 0
    C_SF = 0
    C_PF = 0
    C_C = 0

    for x in range(len(test_data)):
        neighbors = Functions.getNeighbors(training_data, test_data[x], k)
        result = Functions.getResponse(neighbors)
        predictions3.append(result)

        if repr(result) == repr('PG'):
            if repr(test_data[x][-1]) == repr('PG'):
                PG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PG_C += 1
        elif repr(result) == repr('SG'):
            if repr(test_data[x][-1]) == repr('PG'):
                SG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SG_C += 1
        elif repr(result) == repr('SF'):
            if repr(test_data[x][-1]) == repr('PG'):
                SF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SF_C += 1
        elif repr(result) == repr('PF'):
            if repr(test_data[x][-1]) == repr('PG'):
                PF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PF_C += 1
        elif repr(result) == repr('C'):
            if repr(test_data[x][-1]) == repr('PG'):
                C_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                C_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                C_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                C_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                C_C += 1

        if repr(result) != repr(test_data[x][-1]):
            unmatched += 1
        else:
            matched += 1
        # print('predicted = ' + repr(result) + ', actual = ' + repr(test_data[x][-1]))
    accuracy = Functions.getAccuracy(test_data, predictions3)

    # draw the table
    print("Table: (first row is the predicted values, first column is actual values)")
    print("\tPG\tSG\tSF\tPF\tC")
    print("PG\t%d\t%d\t%d\t%d\t%d" % (PG_PG, SG_PG, SF_PG, PF_PG, C_PG))
    print("SG\t%d\t%d\t%d\t%d\t%d" % (PG_SG, SG_SG, SF_SG, PF_SG, C_SG))
    print("SF\t%d\t%d\t%d\t%d\t%d" % (PG_SF, SG_SF, SF_SF, PF_SF, C_SF))
    print("PF\t%d\t%d\t%d\t%d\t%d" % (PG_PF, SG_PF, SF_PF, PF_PF, C_PF))
    print("C\t%d\t%d\t%d\t%d\t%d" % (PG_C, SG_C, SF_C, PF_C, C_C))
    print()
    print('Total test data:', (matched + unmatched))
    print('Matched:', matched, 'Unmatched:', unmatched)
    print('Accuracy: ' + repr(accuracy) + '%')
    print()


    k = 20
    print('4. When k is', k)
    predictions4 = []
    matched = 0
    unmatched = 0

    PG_PG = 0
    PG_SG = 0
    PG_SF = 0
    PG_PF = 0
    PG_C = 0

    SG_PG = 0
    SG_SG = 0
    SG_SF = 0
    SG_PF = 0
    SG_C = 0

    SF_PG = 0
    SF_SG = 0
    SF_SF = 0
    SF_PF = 0
    SF_C = 0

    PF_PG = 0
    PF_SG = 0
    PF_SF = 0
    PF_PF = 0
    PF_C = 0

    C_PG = 0
    C_SG = 0
    C_SF = 0
    C_PF = 0
    C_C = 0

    for x in range(len(test_data)):
        neighbors = Functions.getNeighbors(training_data, test_data[x], k)
        result = Functions.getResponse(neighbors)
        predictions4.append(result)

        if repr(result) == repr('PG'):
            if repr(test_data[x][-1]) == repr('PG'):
                PG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PG_C += 1
        elif repr(result) == repr('SG'):
            if repr(test_data[x][-1]) == repr('PG'):
                SG_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SG_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SG_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SG_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SG_C += 1
        elif repr(result) == repr('SF'):
            if repr(test_data[x][-1]) == repr('PG'):
                SF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                SF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                SF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                SF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                SF_C += 1
        elif repr(result) == repr('PF'):
            if repr(test_data[x][-1]) == repr('PG'):
                PF_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                PF_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                PF_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                PF_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                PF_C += 1
        elif repr(result) == repr('C'):
            if repr(test_data[x][-1]) == repr('PG'):
                C_PG += 1
            elif repr(test_data[x][-1]) == repr('SG'):
                C_SG += 1
            elif repr(test_data[x][-1]) == repr('SF'):
                C_SF += 1
            elif repr(test_data[x][-1]) == repr('PF'):
                C_PF += 1
            elif repr(test_data[x][-1]) == repr('C'):
                C_C += 1

        if repr(result) != repr(test_data[x][-1]):
            unmatched += 1
        else:
            matched += 1
        # print('predicted = ' + repr(result) + ', actual = ' + repr(test_data[x][-1]))
    accuracy = Functions.getAccuracy(test_data, predictions4)

    # draw the table
    print("Table: (first row is the predicted values, first column is actual values)")
    print("\tPG\tSG\tSF\tPF\tC")
    print("PG\t%d\t%d\t%d\t%d\t%d" % (PG_PG, SG_PG, SF_PG, PF_PG, C_PG))
    print("SG\t%d\t%d\t%d\t%d\t%d" % (PG_SG, SG_SG, SF_SG, PF_SG, C_SG))
    print("SF\t%d\t%d\t%d\t%d\t%d" % (PG_SF, SG_SF, SF_SF, PF_SF, C_SF))
    print("PF\t%d\t%d\t%d\t%d\t%d" % (PG_PF, SG_PF, SF_PF, PF_PF, C_PF))
    print("C\t%d\t%d\t%d\t%d\t%d" % (PG_C, SG_C, SF_C, PF_C, C_C))
    print()
    print('Total test data:', (matched + unmatched))
    print('Matched:', matched, 'Unmatched:', unmatched)
    print('Accuracy: ' + repr(accuracy) + '%')
