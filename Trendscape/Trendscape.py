from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def setup_pytrends():
    """Set up pytrends object and return it."""
    return TrendReq(hl='en-US', tz=360)

def get_keywords_from_user():
    """Prompt user for keywords and return the list."""
    num_keywords = min(25, int(input("Enter the number of keywords (up to 25): ")))
    return [input(f"Enter keyword {i+1}: ") for i in range(num_keywords)]

def plot_interest_over_time(interest_data, keywords):
    """Generate a plot for interest over time."""
    plt.figure(figsize=(10, 6))
    interest_data.plot()
    plt.title('Google Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Interest')
    plt.legend(keywords, loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()

def on_click(event):
    """Handle click events on the plot."""
    # TODO: Implement this function
    pass

def save_plot():
    """Save the visualization and return the filename."""
    save_filename = input("Enter the filename to save the visualization (without extension): ")
    plt.savefig(f"{save_filename}.png")
    return save_filename

def save_analysis_to_file(interest_data, filename):
    """Save basic analysis to a text file."""
    # Basic analysis
    highest_interest = interest_data.max().dropna()
    highest_interest_keywords = highest_interest.idxmax() if not highest_interest.empty else "No data available"
    analysis_result = f"The keyword with the highest interest is '{highest_interest_keywords}'."
    
    # Calculate percentage change
    time_intervals = ['1w', '1m', '3m', '6m', '12m']
    analysis_text = [analysis_result, "\n\nPercentage change in interest:"]
    for interval in time_intervals:
        interval_data = interest_data.last(interval).iloc[0]
        percent_change = (interval_data - interval_data.iloc[0]) / interval_data.iloc[0] * 100
        analysis_text.append(f"{interval}: {percent_change:.2f}%")

    # Write results to a text file
    with open(f"{filename}_analysis.txt", "w") as analysis_file:
        analysis_file.write("\n".join(analysis_text))

def main():
    pytrends = setup_pytrends()
    keywords = get_keywords_from_user()

    # Build the payload for Google Trends query and fetch data
    pytrends.build_payload(keywords, timeframe='today 5-y', geo='', gprop='')
    interest_over_time = pytrends.interest_over_time()

    plot_interest_over_time(interest_over_time, keywords)

    # Initialize click event on plot
    plt.gcf().canvas.mpl_connect("button_press_event", on_click)

    filename = save_plot()
    save_analysis_to_file(interest_over_time, filename)
    
    plt.show()

if __name__ == "__main__":
    main()
