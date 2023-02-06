import math
import pandas as pd
import sqlite3


class Solution:
    def __init__(self):
        # connecting to the DB
        self.connection = sqlite3.connect('test_11.db')
        self.cursor = self.connection.cursor()
        # variables
        self.managers = None
        self.stores = None
        self.sales_data = None
        self.feature_data = None
        self.dates = None

    # creation of the tables
    def createTable(self):

        # sql schema to create store table
        create_store_table = ''' CREATE TABLE IF NOT EXISTS 'store' (
            "store" INT NOT NULL,
            "size" INT NOT NULL,
            "type" VARCHAR(45) NOT NULL,
            "manager_id" INT NOT NULL,
            FOREIGN KEY ('manager_id') REFERENCES manager_id('manager')
            PRIMARY KEY ("store"))
        '''

        # sql schema to create manager table
        create_manager_table = ''' CREATE TABLE IF NOT EXISTS 'manager' (
            "manager_id" INT NOT NULL,
            "store" INT NOT NULL,
            "manager_name" VARCHAR(45) NOT NULL,
            "year_as_manager" INT NOT NULL,
            "email" VARCHAR(45) NOT NULL,
            "street_address" VARCHAR(45) NOT NULL,
            "city" VARCHAR(45) NOT NULL,
            "state" VARCHAR(45) NOT NULL,
            "zipcode" INT NOT NULL,
            FOREIGN KEY ('store') REFERENCES store ('store')
            PRIMARY KEY ("manager_id"))
        '''

        # sql schema to create date table
        create_date_table = ''' CREATE TABLE IF NOT EXISTS 'date' (
            "date" DATE NOT NULL,
            "isholiday" BOOLEAN NOT NULL,
            PRIMARY KEY ("date"))
        '''

        # sql schema to create sales table
        create_sales_table = '''  CREATE TABLE 'sales' (
            "sales_id" INT NOT NULL,
            "store" INT NOT NULL,
            "dept" INT NOT NULL,
            "weekly_sales" REAL NOT NULL,
            "date" DATE NOT NULL,
            FOREIGN KEY ('store') REFERENCES store ('store')
            FOREIGN KEY ('date') REFERENCES date ('date')
            PRIMARY KEY ("sales_id"))
        '''

        # sql schema to create feature table
        create_features_table = ''' CREATE TABLE IF NOT EXISTS 'features' (
            "features_id" INT NOT NULL,
            "store" INT NOT NULL,
            "temperature" REAL NOT NULL,
            "fuel_Price" REAL NOT NULL,
            "markdown_1" REAL NOT NULL,
            "markdown_2" REAL NOT NULL,
            "markdown_3" REAL NOT NULL,
            "markdown_4" REAL NOT NULL,
            "markdown_5" REAL NOT NULL,
            "cpi" REAL NOT NULL,
            "unemployment" REAL NOT NULL,
            "date" DATE NOT NULL,
            FOREIGN KEY ('store') REFERENCES store ('store')
            FOREIGN KEY ('date') REFERENCES date ('date')
            PRIMARY KEY ("features_id")) 
        '''

        # this excute the sql schema for each table.
        self.cursor.execute(create_store_table)
        self.cursor.execute(create_manager_table)
        self.cursor.execute(create_sales_table)
        self.cursor.execute(create_date_table)
        self.cursor.execute(create_features_table)

    # function to read from csv, cleaning data and inserting to the table.
    def readFileAndInsert(self, file, tableName):
        # insert into the table
        if tableName == 'managers':
            self.managers = pd.read_csv(file, dtype={'store': int})
            # data cleaning
            self.managers.index = [x for x in range(
                1, len(self.managers.values)+1)]
            self.managers['manager_id'] = self.managers.index
            self.managers.isnull().sum()
            self.managers.loc[6, 'Manager'] = "George" + " " + "Parker"
            self.managers.dropna(inplace=True)
            self.managers[["street_address", "city", "state", "zipcode"]
                          ] = self.managers.Address.str.split(";", expand=True)
            self.managers = self.managers.drop(columns=(["Address"]), axis=1)
            self.managers = self.managers.iloc[:, [4, 0, 1, 2, 3, 5, 6, 7, 8]]
            self.managers.to_sql(tableName, self.connection,
                                 if_exists='append', index=False)

        elif tableName == 'stores':
            self.stores = pd.read_csv(file)

            # Data Cleaning Part
            self.stores.index = [x for x in range(
                1, len(self.stores.values)+1)]
            self.stores['manager_id'] = self.stores.index
            mean = self.stores['Size'].mean()
            self.stores['Size'].fillna(mean, inplace=True)
            self.stores.isnull().sum()

            print(self.stores)
            # populating the table
            self.stores.to_sql(tableName, self.connection,
                               if_exists='append', index=False)

        elif tableName == 'sales':
            headers = ['Store', 'Dept', 'Weekly_Sales', 'Date']
            self.sales_data = pd.read_csv(file, usecols=headers)
            self.sales_data.index = [x for x in range(
                1, len(self.sales_data.values)+1)]
            self.sales_data['sales_id'] = self.sales_data.index
            self.sales_data.isnull().sum()  # to check for empty column
            self.sales_data = self.sales_data.drop(
                columns=(["IsHoliday"]), axis=1)  # REMOVE IsHoliday
            self.sales_data.fillna(0, inplace=True)
            self.sales_data = self.sales_data.iloc[:, [4, 0, 1, 3, 2]]
            print(self.sales_data)
            self.sales_data.to_sql(
                tableName, self.connection, if_exists='append', index=False)

        elif tableName == 'dates':
            self.dates = pd.concat([self.feature_data[['Date', 'IsHoliday']], self.self.sales_data[[
                                   'Date', 'IsHoliday']]], axis=0)
            self.dates = self.dates.drop_duplicates(subset='Date')
            self.dates = self.dates.groupby('Date').agg(
                {'IsHoliday': 'first'}).reset_index()
            print(self.dates)
            self.dates.to_sql(tableName, self.connection,
                              if_exists='append', index=False)

        elif tableName == 'features':
            self.feature_data = pd.read_csv(file)
            self.feature_data.index = [x for x in range(
                1, len(self.feature_data.values)+1)]
            self.feature_data['features_id'] = self.feature_data.index
            self.feature_data.isnull().sum()
            self.feature_data = self.feature_data.drop(
                columns=(["IsHoliday"]), axis=1)
            self.feature_data["MarkDown1"].fillna("NA", inplace=True)
            self.feature_data["MarkDown2"].fillna("NA", inplace=True)
            self.feature_data["MarkDown3"].fillna("NA", inplace=True)
            self.feature_data["MarkDown4"].fillna("NA", inplace=True)
            self.feature_data["MarkDown5"].fillna("NA", inplace=True)
            self.feature_data["CPI"].fillna("NA", inplace=True)
            self.feature_data["Unemployment"].fillna("NA", inplace=True)
            self.feature_data = self.feature_data.iloc[:, [
                11, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]]
            self.feature_data.isnull().sum()
            self.feature_data.to_sql(
                tableName, self.connection, if_exists='append', index=False)

    # to read from the table
    def readFromTable(self, tableName):
        select_all = "SELECT * FROM "+tableName
        rows = self.cursor.execute(select_all).fetchall()

        for r in rows:
            print(r)

    # to update store info
    def updateStoreInfo(self,store, manager, years, email, street_address, city, state, zipcode):
        my_data = (manager, years, email, street_address,
                   city, state, zipcode, store)
        print(my_data)
        update = '''UPDATE manager SET manager=?, years_as_manager=?, email=?, street_address=?,city=?,state=?,zipcode=? WHERE store=?'''
        print(update)
        try:
            self.cursor.execute(update, (manager, int(years), email,
                        street_address, city, state, zipcode, int(store)))
            self.readFromTable('manager')
        except Exception as my_error:
            print(my_error)

    # select store numbers from store info table
    def returnStoreNumbers(self):
        storeNumbers = []
        select_all = "SELECT store FROM stores"
        rows = self.cursor.execute(select_all).fetchall()

        for r in rows:
            storeNumbers.append(int(r[0]))

        return sorted(storeNumbers)

    def commit(self):
        self.connection.commit()

    # function to calculate mean size for a particular store.
    def meanStoreSize(self, storeType):
        if storeType not in self.storeTypes:
            return "Invalid Store Type selected"

        select_store_size = "SELECT size FROM stores WHERE type='{}' and stores.size <> 'None'".format(
            storeType)
        print(select_store_size)
        rows = self.cursor.execute(select_store_size).fetchall()
        mean = 0
        print(len(rows))
        for r in rows:
            print(r[0])
            mean += r[0]

        print("the mean for this type is =", mean/len(rows))
        return math.ceil(mean/len(rows))

    # function to return distinct type of store in store data table.
    def returnStoreTypes(self):
        storeTypes = []
        print("function to return store types")
        select_storeTypes = "SELECT DISTINCT type FROM stores"
        rows = self.cursor.execute(select_storeTypes).fetchall()
        for r in rows:
            if(r[0] is not storeTypes):
                storeTypes.append(r[0])

        print(storeTypes)
        return storeTypes


# res = Solution()
# res.createTable()
# done
# res.readFileAndInsert('store_info.csv', "managers")
# res.readFromTable('managers')

# print(res.returnStoreNumbers())

# done
# res.readFileAndInsert('stores_data-set.csv', "stores")
# res.readFromTable('stores')

# done
# res.readFileAndInsert('self.sales_data-set.csv', "sales")
# res.readFromTable('sales')

# done
# res.readFileAndInsert(' self.feature_data_set.csv', "features")
# res.readFromTable('features')

# done
# res.readFileAndInsert(' self.feature_data_set.csv', "dates")
# res.readFromTable('dates')

# res.updateStoreInfo("10", "tobey1 doe","1", "tobey1.doe@Walmart.org", "lagos")
