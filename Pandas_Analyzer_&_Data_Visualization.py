import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

class Data_Analyzer():
    def __init__(self,data):
        self.data = data

    def display(self):
        print(f"Data:{self.data}")

    def explore_data(self):
        while True:
            print("== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Exit")
            opt = int(input("Choose an option:"))
    
            if opt == 1:
                print(self.data.head())
            elif opt == 2:
                print(self.data.tail())
            elif opt == 3:
                print(self.data.columns)
            elif opt == 4:
                print(self.data.dtypes)
            elif opt == 5:
                print(self.data.info())
            elif opt == 6:
                print("Exiting the Choice....")
                break
            else:
                print("Invalid Choice.Please try again....")

    def Dataframe_operation(self):
        while True:
            print("=== DataFrame Operations ===")
            print("1. Create a DataFrame")
            print("2. Indexing")
            print("3. Slicing")
            print("4. Selecting columns from DataFrame")
            print("5. Selecting rows from DataFrame")
            print("6. Exit" )
            option = int(input("Enter your choice: "))

            if option == 1:
                print("\nEnter data to create a DataFrame:")
                products_count = int(input("How many products?: "))
                products = []
                sales = []
                profits = []
                        
                for i in range(products_count):
                    product = input("Enter product name: ")
                    sale = float(input(f"Enter sales for {product}: "))
                    profit = float(input(f"Enter profit for {product}: "))
                    products.append(product)
                    sales.append(sale)
                    profits.append(profit)
                    new_data = {'Product': products, 'Sales': sales, 'Profit': profits}
                    df = pd.DataFrame(new_data)
                    print("\nCreated DataFrame:")
                    print(df)
                        
            elif option == 2:
                row = int(input("Enter row index: "))
                col = input("Enter column name: ")
                print(f"Value at row {row}, column '{col}': {self.data.at[row, col]}")
                    
            elif option == 3:
                print("\nSlicing Example: Select rows")
                start_row = int(input("Enter start row index: "))
                end_row = int(input("Enter end row index: "))
                print(f"Rows from {start_row} to {end_row}:")
                print(self.data.iloc[start_row:end_row])
                    
            elif option == 4:
                column_name = input("Enter column name to select: ")
                if column_name in self.data.columns:
                    print(f"Selected column '{column_name}':")
                    print(self.data[column_name])
                else:
                    print("Column not found.")
            elif choice == 5:
                row_name = input("Enter row name to select: ")
                if row_name in self.data.columns:
                    print(f"Selected row '{row_name}':")
                    print(self.data[row])
                else:
                    print("Row not found.")
            elif choice == 6:
                print("Exiting the program.....")
                break
            else:
                print("Invalid choice!please try again")

    def Handle_data(self):
        while True:
            print("== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Exit")
            option = int(input("Enter your choice: "))
            
            if option == 1:
                print(self.data.isnull().sum())
            elif option == 2:
                self.data.fillna(self.data.mean(), inplace=True)
                print("Missing values filled with mean.")
            elif option == 3:
                self.data.dropna(inplace=True)
                print("Rows with missing values dropped.")
            elif option == 4:
                value = input("Enter value to replace missing data with: ")
                self.data.fillna(value, inplace=True)
                print(f"Missing values replaced with {value}.")
            elif option == 5:
                print("Exiting the program.....")
                break
            else:
                print("Invalid Choice!Please try again....")

    def visualize_data(self):
        while True:
            print("== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Box Plot")
            print("6. Histogram")
            print("7. Violin Plot")
            print("8. Stack Plot")
            print("9. Step Chart")
            print("10.Exit")
            option = int(input("Enter your choice: "))
            
            x_col = input("Enter x-axis column name: ")
            y_col = input("Enter y-axis column name: ")
            if option == 1:
                plt.bar(self.data[x_col], self.data[y_col])
                plt.show()
            elif option == 2:
                plt.plot(self.data[x_col], self.data[y_col])
                plt.show()
            elif option == 3:
                plt.scatter(self.data[x_col], self.data[y_col])
                plt.show()
            elif option == 4:
                plt.pie(self.data[y_col].value_counts(), labels=self.data[x_col].unique())
                plt.show()
            elif option == 5:
                plt.boxplot(self.data[y_col])
                plt.show()
            elif option == 6:
                plt.hist(self.data[y_col])
                plt.show()
            elif option == 7:
                sns.violinplot(x=self.data[x_col], y=self.data[y_col])
                plt.show()
            elif option == 8:
                plt.stackplot(self.data[x_col], self.data[y_col])
                plt.show()
            elif option == 9:
                plt.step(self.data[x_col], self.data[y_col])
                plt.show()
            elif option == 10:
                print("Exiting the program...")
                break
            else:
                print("Invalid option! please try agian...")
                return
            plt.title(f"{x_col} vs {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.grid()
    
    
    def save_visualization(self, filename):
        plt.savefig(filename)
        print(f"Visualization saved as {filename} successfully!")


while True:

    print("=========== Data Analysis & Visualization Program ===========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. save Visualization")
    print("8. Exit")
    print("==============================================================")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        print("== Load Dataset ==\n")
        df_sale = pd.read_csv("Online Sales Data.csv", encoding = 'utf-8')
        obj = Data_Analyzer(df_sale)
        print(df_sale)
        print("\nDataset loaded successfully!")

    elif choice == 2:
        obj.explore_data()

    elif choice == 3:
        obj.Dataframe_operation()

    elif choice == 4:
        obj.Handle_data()
        
    elif choice == 5:
        obj.data.describe()

    elif choice == 6:
        obj.visualize_data()

    elif choice == 7:
        print("== Save Visualization ==\n")
        filename = input("Enter file name to save the plot (e.g., 'scatter_plot.png'): ")
        obj.save_visualization(filename)

    elif choice == 8:
        print("Exiting the program. Goodbye!......")
        break
    else:
        print("Invalid Choice!Please Try Again.......")
