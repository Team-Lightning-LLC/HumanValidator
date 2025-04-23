# validator.py

import random
import difflib
import re
from submission import Submission

class Validator:
    def __init__(self):
        self.history = {}  # Maps student_id to list of previous submissions

    def score_submission(self, submission: Submission) -> dict:
        emotional_variance = self.analyze_emotion(submission.text)
        logical_fluctuation = self.analyze_logic(submission.text)
        pattern_consistency = self.analyze_pattern(submission)
        error_typing = self.analyze_typing_errors(submission.text)
        originality = self.analyze_originality(submission)
        time_anomaly = self.analyze_time(submission)

        overall_score = self.weighted_score(
            emotional_variance,
            logical_fluctuation,
            pattern_consistency,
            error_typing,
            originality,
            time_anomaly
        )

        return {
            "submission_id": str(submission.id),
            "student_id": submission.student_id,
            "emotional_variance": emotional_variance,
            "logical_fluctuation": logical_fluctuation,
            "pattern_consistency": pattern_consistency,
            "error_typing": error_typing,
            "originality": originality,
            "time_anomaly": time_anomaly,
            "overall_humanity_score": round(overall_score, 2)
        }

    def record_submission(self, submission: Submission):
        if submission.student_id not in self.history:
            self.history[submission.student_id] = []
        self.history[submission.student_id].append(submission)

    def analyze_emotion(self, text: str) -> float:
        emotional_words = ["feel", "hope", "fear", "love", "worry", "believe", "joy"]
        score = sum(1 for word in emotional_words if word in text.lower())
        return min(score / 5.0, 1.0)

    def analyze_logic(self, text: str) -> float:
        transitions = ["however", "but", "yet", "although", "therefore"]
        score = sum(1 for word in transitions if word in text.lower())
        return min(score / 5.0, 1.0)

    def analyze_pattern(self, submission: Submission) -> float:
        previous = self.history.get(submission.student_id, [])
        if not previous:
            return 0.3
        comparisons = [self.similarity(submission.text, prev.text) for prev in previous[-3:]]
        return round(max(comparisons), 2) if comparisons else 0.3

    def analyze_typing_errors(self, text: str) -> float:
        typo_patterns = [r"\\bi\\s+a\\b", r"\\bteh\\b", r"\\brecieve\\b", r"\\bwich\\b"]
        score = sum(1 for pat in typo_patterns if re.search(pat, text.lower()))
        return min(score / 3.0, 1.0)

    def analyze_originality(self, submission: Submission) -> float:
        previous = self.history.get(submission.student_id, [])
        if not previous:
            return 0.9
        similarities = [self.similarity(submission.text, s.text) for s in previous]
        return round(1.0 - max(similarities), 2)

    def analyze_time(self, submission: Submission) -> float:
        duration = submission.duration_seconds()
        return 1.0 if duration < 60 else random.uniform(0.1, 0.6)

    def weighted_score(self, e, l, p, t, o, time):
        return (e * 0.2 + l * 0.15 + (1 - p) * 0.2 + t * 0.15 + o * 0.2 + (1 - time) * 0.1)

    def similarity(self, a: str, b: str) -> float:
        return difflib.SequenceMatcher(None, a, b).ratio()

