from logic import GradingModel

class GradingController:
    def __init__(self, view):
        self.view = view
        self.model = GradingModel()

    def submit_scores(self):
        """Handles the submission of scores from the view."""
        name = self.view.name_input.text().strip()
        attempts = self.view.attempts_input.text().strip()

        if not name or not name.replace(" ", "").isalpha():
            self.view.show_error("Enter a valid name (letters only)")
            return

        if not attempts.isdigit() or not (1 <= int(attempts) <= 4):
            self.view.show_error("Enter an attempt from 1-4")
            return

        attempts = int(attempts)
        scores = []

        for i in range(attempts):
            score_text = self.view.score_inputs[i].text().strip()
            if not score_text.isdigit():
                self.view.show_error(f"Enter a valid Score {i + 1} (0-100)")
                return

            score = int(score_text)
            if not (0 <= score <= 100):
                self.view.show_error(f"Score {i + 1} must be between 0 and 100")
                return

            scores.append(score)

        while len(scores) < 4:
            scores.append("")

        final_score = self.model.calculate_final_score([int(s) for s in scores if s != ""])

        self.model.save_data(name, scores, final_score)
        self.view.show_success("Submitted")
