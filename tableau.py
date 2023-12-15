from data import google_data, amazon_data
import pandas as pd

google_revenue = google_data["Close"] * google_data["Volume"]
amazon_revenue = amazon_data["Close"] * amazon_data["Volume"]

google_revenue_growth = google_revenue.pct_change()
amazon_revenue_growth = amazon_revenue.pct_change()

class TableauWorksheet:
    def __init__(self, name):
        self.name = name
        self.data = None

    def setData(self, data):
        self.data = data

    def mark_line(self, x, y):
        pass

    def mark_scatter(self, x, y):
        pass

class TableauDashboard:
    def __init__(self, title):
        self.title = title
        self.worksheets = []

    def addWorksheet(self, worksheet):
        self.worksheets.append(worksheet)

    def setTitle(self, title):
        self.title = title

# Define data source connections
google_data_source = pd.DataFrame({"Date": google_data.index, "Revenue": google_revenue})
amazon_data_source = pd.DataFrame({"Date": amazon_data.index, "Revenue": amazon_revenue})

# Create worksheets and charts
google_revenue_chart = TableauWorksheet("Google Revenue Over Time")
google_revenue_chart.setData(google_data_source)
google_revenue_chart.mark_line(x="Date", y="Revenue")

amazon_revenue_chart = TableauWorksheet("Amazon Revenue Over Time")
amazon_revenue_chart.setData(amazon_data_source)
amazon_revenue_chart.mark_line(x="Date", y="Revenue")

correlation_chart = TableauWorksheet("Correlation between Google and Amazon Revenue")
correlation_chart.setData(pd.DataFrame({"Google": google_revenue_growth, "Amazon": amazon_revenue_growth}))
correlation_chart.mark_scatter(x="Google", y="Amazon")

# Combine worksheets and customize dashboard
dashboard = TableauDashboard("Tech Titans")
dashboard.addWorksheet(google_revenue_chart)
dashboard.addWorksheet(amazon_revenue_chart)
dashboard.addWorksheet(correlation_chart)
dashboard.setTitle("Unraveling Google & Amazon's 2024 Potential")

# Publish or embed dashboard as needed
