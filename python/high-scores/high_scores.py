class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        sort_scores = sorted(self.scores , reverse = True)
        return sort_scores[:3]
