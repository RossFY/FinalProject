# This is the Main File



class Main(object):
    from Functions import Functions
    from getResult import getResult
    if __name__ == "__main__":
        f = Functions()
        filename = 'players_stats.csv'
        test_data, training_data = f.loadDataset(filename)

        print("The program will show different results due to different k values: ")
        print()

        # test when k = 5
        k = 5
        print('1. When k is', k)

        gr1 = getResult(k, test_data, training_data)
        gr1.printResult()

        # test when k = 10
        k = 10
        print('2. When k is', k)

        gr2 = getResult(k, test_data, training_data)
        gr2.printResult()

        # test when k = 15
        k = 15
        print('3. When k is', k)

        gr3 = getResult(k, test_data, training_data)
        gr3.printResult()

        # test when k = 20
        k = 20
        print('4. When k is', k)

        gr4 = getResult(k, test_data, training_data)
        gr4.printResult()