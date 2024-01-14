import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_name):
    """
    Loads data from a CSV file.
    :param file_name: str, name of the file to load.
    :return: DataFrame, loaded data.
    """
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return pd.DataFrame()

def analyze_income(data):
    """
    Analyzes the income data.
    :param data: DataFrame, the data containing income information.
    :return: dict, basic statistics of income.
    """
    stats = {
        'mean': data['Income'].mean(),
        'median': data['Income'].median(),
        'max': data['Income'].max(),
        'min': data['Income'].min()
    }
    return stats

def filter_income(data, lower_bound, upper_bound):
    """
    Filters the data for incomes within the specified range.
    :param data: DataFrame, the data to filter.
    :param lower_bound: int, the lower bound of the income range.
    :param upper_bound: int, the upper bound of the income range.
    :return: DataFrame, filtered data.
    """
    filtered_data = data[(data['Income'] >= lower_bound) & (data['Income'] <= upper_bound)]
    return filtered_data

def visualize_income_distribution(data):
    """
    Visualizes the distribution of income.
    :param data: DataFrame, the data to visualize.
    """
    plt.figure()
    plt.hist(data['Income'], bins=20, color='blue', alpha=0.7)
    plt.title('Income Distribution')
    plt.xlabel('Income')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def main():
    file_name = 'C:/Users/matth/Documents/Test Python/income_data.csv'
    data = load_data(file_name)
    
    if not data.empty:
        # Interactive part: User specifies income range
        lower_bound = int(input("Enter the lower bound of income: "))
        upper_bound = int(input("Enter the upper bound of income: "))

        filtered_data = filter_income(data, lower_bound, upper_bound)
        stats = analyze_income(filtered_data)
        print(f"Income Statistics for the specified range:\n{stats}")
        visualize_income_distribution(filtered_data)
    else:
        print("No data available.")

if __name__ == "__main__":
    main()
