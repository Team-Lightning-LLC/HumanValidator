// src/components/SubmissionCard.jsx

import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";

export default function SubmissionCard({ data }) {
  const {
    assignment,
    score,
    emotional,
    logic,
    pattern,
    error,
    originality,
    time,
    flagged,
  } = data;

  return (
    <Card className={`border ${flagged ? "border-red-500" : "border-green-500"}`}>
      <CardContent className="p-4 space-y-3">
        <h2 className="text-xl font-semibold">{assignment}</h2>
        <div className="space-y-1">
          <p>Overall Humanity Score: <strong>{score}</strong></p>
          <Progress value={score * 100} />
          <p>Emotional Variance: {emotional}</p>
          <p>Logical Fluctuation: {logic}</p>
          <p>Pattern Consistency: {pattern}</p>
          <p>Typing Errors: {error}</p>
          <p>Originality: {originality}</p>
          <p>Time Anomaly: {time}</p>
          {flagged && <p className="text-red-500">⚠️ Flagged for Review</p>}
        </div>
      </CardContent>
    </Card>
  );
}
