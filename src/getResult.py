from Functions import Functions

class getResult(object):
    def __init__(self, k, test_data, training_data):
        self.predictions = []
        self.matched = 0
        self.unmatched = 0

        self.PG_PG = 0
        self.PG_SG = 0
        self.PG_SF = 0
        self.PG_PF = 0
        self.PG_C = 0

        self.SG_PG = 0
        self.SG_SG = 0
        self.SG_SF = 0
        self.SG_PF = 0
        self.SG_C = 0

        self.SF_PG = 0
        self.SF_SG = 0
        self.SF_SF = 0
        self.SF_PF = 0
        self.SF_C = 0

        self.PF_PG = 0
        self.PF_SG = 0
        self.PF_SF = 0
        self.PF_PF = 0
        self.PF_C = 0

        self.C_PG = 0
        self.C_SG = 0
        self.C_SF = 0
        self.C_PF = 0
        self.C_C = 0

        self.k = k
        self.test_data = test_data
        self.training_data = training_data

    def printResult(self):
        f = Functions()
        for x in range(len(self.test_data)):
            neighbors = f.getNeighbors(self.training_data, self.test_data[x], self.k)
            result = f.getResponse(neighbors)
            self.predictions.append(result)

            if repr(result) == repr('PG'):
                if repr(self.test_data[x][-1]) == repr('PG'):
                    self.PG_PG += 1
                elif repr(self.test_data[x][-1]) == repr('SG'):
                    self.PG_SG += 1
                elif repr(self.test_data[x][-1]) == repr('SF'):
                    self.PG_SF += 1
                elif repr(self.test_data[x][-1]) == repr('PF'):
                    self.PG_PF += 1
                elif repr(self.test_data[x][-1]) == repr('C'):
                    self.PG_C += 1
            elif repr(result) == repr('SG'):
                if repr(self.test_data[x][-1]) == repr('PG'):
                    self.SG_PG += 1
                elif repr(self.test_data[x][-1]) == repr('SG'):
                    self.SG_SG += 1
                elif repr(self.test_data[x][-1]) == repr('SF'):
                    self.SG_SF += 1
                elif repr(self.test_data[x][-1]) == repr('PF'):
                    self.SG_PF += 1
                elif repr(self.test_data[x][-1]) == repr('C'):
                    self.SG_C += 1
            elif repr(result) == repr('SF'):
                if repr(self.test_data[x][-1]) == repr('PG'):
                    self.SF_PG += 1
                elif repr(self.test_data[x][-1]) == repr('SG'):
                    self.SF_SG += 1
                elif repr(self.test_data[x][-1]) == repr('SF'):
                    self.SF_SF += 1
                elif repr(self.test_data[x][-1]) == repr('PF'):
                    self.SF_PF += 1
                elif repr(self.test_data[x][-1]) == repr('C'):
                    self.SF_C += 1
            elif repr(result) == repr('PF'):
                if repr(self.test_data[x][-1]) == repr('PG'):
                    self.PF_PG += 1
                elif repr(self.test_data[x][-1]) == repr('SG'):
                    self.PF_SG += 1
                elif repr(self.test_data[x][-1]) == repr('SF'):
                    self.PF_SF += 1
                elif repr(self.test_data[x][-1]) == repr('PF'):
                    self.PF_PF += 1
                elif repr(self.test_data[x][-1]) == repr('C'):
                    self.PF_C += 1
            elif repr(result) == repr('C'):
                if repr(self.test_data[x][-1]) == repr('PG'):
                    self.C_PG += 1
                elif repr(self.test_data[x][-1]) == repr('SG'):
                    self.C_SG += 1
                elif repr(self.test_data[x][-1]) == repr('SF'):
                    self.C_SF += 1
                elif repr(self.test_data[x][-1]) == repr('PF'):
                    self.C_PF += 1
                elif repr(self.test_data[x][-1]) == repr('C'):
                    self.C_C += 1

            if repr(result) != repr(self.test_data[x][-1]):
                self.unmatched += 1
            else:
                self.matched += 1
            # print('predicted = ' + repr(result) + ', actual = ' + repr(test_data[x][-1]))

        accuracy = f.getAccuracy(self.test_data, self.predictions)

        # draw the table
        print("Table: (first row is the predicted values, first column is actual values)")
        print("\tPG\tSG\tSF\tPF\tC")
        print("PG\t%d\t%d\t%d\t%d\t%d" % (self.PG_PG, self.SG_PG, self.SF_PG, self.PF_PG, self.C_PG))
        print("SG\t%d\t%d\t%d\t%d\t%d" % (self.PG_SG, self.SG_SG, self.SF_SG, self.PF_SG, self.C_SG))
        print("SF\t%d\t%d\t%d\t%d\t%d" % (self.PG_SF, self.SG_SF, self.SF_SF, self.PF_SF, self.C_SF))
        print("PF\t%d\t%d\t%d\t%d\t%d" % (self.PG_PF, self.SG_PF, self.SF_PF, self.PF_PF, self.C_PF))
        print("C\t%d\t%d\t%d\t%d\t%d" % (self.PG_C, self.SG_C, self.SF_C, self.PF_C, self.C_C))
        print()
        print('Total test data:', (self.matched + self.unmatched))
        print('Matched:', self.matched, 'Unmatched:', self.unmatched)
        print('Accuracy: ' + repr(accuracy) + '%')
        print()