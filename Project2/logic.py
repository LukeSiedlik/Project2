import csv

class GradingModel:
    def __init__(self):
        self.filename = "grading_data.csv"

    def save_data(self, name: str, scores: list, final_score: float):
        """Saves the student data (name, scores, final average) to a CSV file."""
        data = [name] + scores + [final_score]
        self.ensure_csv_exists()

        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
        except Exception as e:
            print(f"Error writing to CSV file: {e}")

    def ensure_csv_exists(self):
        """Ensures the CSV file is created if it does not exist."""
        try:
            with open(self.filename, mode='r') as file:
                pass
        except FileNotFoundError:
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score 1", "Score 2", "Score 3", "Score 4", "Final"])

    def calculate_final_score(self, scores: list) -> float:
        """Calculates the average score."""
        if scores:
            return round(sum(scores) / len(scores), 2)
        return 0.0
