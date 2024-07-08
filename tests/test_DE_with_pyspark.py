import unittest
import nbimporter
import sys,os
sys.path.insert(0,os.getcwd())

from src import DE_with_pyspark as qn
from tests import solution as sol
from tests.TestUtils import TestUtils

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("appName").config("spark.driver.extraClassPath", "C:\\mysql-connector-j-8.0.33.jar").getOrCreate()

def are_two_spark_dataframes_equal(df_sol, df_test):
    try:
        match_column_names = set(df_sol.columns) == set(df_test.columns)

        if match_column_names:
            # Sort the columns to ensure consistent order
            df_sol = df_sol.select(sorted(df_sol.columns))
            df_test = df_test.select(sorted(df_test.columns))
            
            # Compare values
            mismatched_rows = df_sol.subtract(df_test)
            
            if mismatched_rows.count() == 0:
                return True
            else:
                return False
        else:
            return False
    except:
        return False


class TestLoadDataFromMysql(unittest.TestCase):
     
    def test_load_data_from_mysql(self):
        try:
            test_obj = TestUtils()
            sol_df = sol.load_data_from_mysql(spark, "classicmodels", 'orderdetails')
            test_df = qn.load_data_from_mysql(spark, "classicmodels", 'orderdetails')
            if are_two_spark_dataframes_equal(sol_df, test_df):
                passed = True
                test_obj.yakshaAssert("TestLoadDataFromMysql", True, "functional")
                print("TestLoadDataFromMysql = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestLoadDataFromMysql", False, "functional")
                print("TestLoadDataFromMysql = Falied")
        except:
            passed = False
            test_obj.yakshaAssert("TestLoadDataFromMysql", False, "functional")
            print("TestLoadDataFromMysql = Falied")
        
        assert passed

class TestLoadDataFromCSV(unittest.TestCase):
     
    def test_load_data_from_csv(self):
        try:
            test_obj = TestUtils()
            sol_df = sol.load_data_from_csv(spark, 'employees.csv')
            test_df = qn.load_data_from_csv(spark, 'employees.csv')
            if are_two_spark_dataframes_equal(sol_df, test_df):
                passed = True
                test_obj.yakshaAssert("TestLoadDataFromMyCSV", True, "functional")
                print("TestLoadDataFromMyCSV = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestLoadDataFromMyCSV", False, "functional")
                print("TestLoadDataFromMyCSV = Falied")
        except:
            passed = False
            test_obj.yakshaAssert("TestLoadDataFromMyCSV", False, "functional")
            print("TestLoadDataFromMyCSV = Falied")
        assert passed

class TestLoadDataFromFlatfile(unittest.TestCase):
     
    def test_load_data_from_flatfile(self):
        try:
            test_obj = TestUtils()
            sol_df = sol.load_data_from_flatfile(spark, 'payments.txt')
            test_df = qn.load_data_from_flatfile(spark, 'payments.txt')
            if are_two_spark_dataframes_equal(sol_df, test_df):
                passed = True
                test_obj.yakshaAssert("TestLoadDataFromFlatfile", True, "functional")
                print("TestLoadDataFromFlatfile = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestLoadDataFromFlatfile", False, "functional")
                print("TestLoadDataFromFlatfile = Falied")
        except:
            passed = False
            test_obj.yakshaAssert("TestLoadDataFromFlatfile", False, "functional")
            print("TestLoadDataFromFlatfile = Falied")
        assert passed

class TestGetCustomerInfo(unittest.TestCase):
     
    def test_get_customer_info(self):
        try:
            test_obj = TestUtils()
            sol_df = sol.get_customer_info(spark)
            test_df = qn.get_customer_info(spark)
            if are_two_spark_dataframes_equal(sol_df, test_df):
                passed = True
                test_obj.yakshaAssert("TestGetCustomerInfo", True, "functional")
                print("TestGetCustomerInfo = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestGetCustomerInfo", False, "functional")
                print("TestGetCustomerInfo = Falied")
        except:
            passed = False
            test_obj.yakshaAssert("TestGetCustomerInfo", False, "functional")
            print("TestGetCustomerInfo = Falied")
        assert passed

class TestCleanProductMSRPColumn(unittest.TestCase):
     
    def test_clean_product_MSRP_column(self):
        test_obj = TestUtils()
        sol_df = sol.clean_product_MSRP_column(spark)
        test_df = qn.clean_product_MSRP_column(spark)
        if are_two_spark_dataframes_equal(sol_df, test_df):
            passed = True
            test_obj.yakshaAssert("TestCleanProductMSRPColumn", True, "functional")
            print("TestCleanProductMSRPColumn = Passed")
        else:
            passed = False
            test_obj.yakshaAssert("TestCleanProductMSRPColumn", False, "functional")
            print("TestCleanProductMSRPColumn = Falied")
        
            passed = False
            test_obj.yakshaAssert("TestCleanProductMSRPColumn", False, "functional")
            print("TestCleanProductMSRPColumn = Falied")
        assert passed
class TestReturnTop5BigSpendCountries(unittest.TestCase):
     
    def test_return_top_5_big_spend_countries(self):
        try:
            test_obj = TestUtils()
            sol_df = sol.return_top_5_big_spend_countries(spark)
            test_df = qn.return_top_5_big_spend_countries(spark)
            if are_two_spark_dataframes_equal(sol_df, test_df):
                passed = True
                test_obj.yakshaAssert("TestReturnTop5BigSpendCountries", True, "functional")
                print("TestReturnTop5BigSpendCountries = Passed")
            else:
                passed = False
                test_obj.yakshaAssert("TestReturnTop5BigSpendCountries", False, "functional")
                print("TestReturnTop5BigSpendCountries = Falied")
        except:
            passed = False
            test_obj.yakshaAssert("TestReturnTop5BigSpendCountries", False, "functional")
            print("TestReturnTop5BigSpendCountries = Falied")
        assert passed
