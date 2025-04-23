// src/pages/Dashboard.jsx

import { useEffect, useState } from "react";
import SubmissionCard from "@/components/SubmissionCard";

const mockData = [
  {
    assignment: "Week 7: Ethical Dilemmas",
    score: 0.21,
    emotional: 0.12,
    logic: 0.09,
    pattern: 0.95,
    error: 0.03,
    originality: 0.14,
    time: 0.97,
    flagged: true,
  },
  {
    assignment: "Week 6: Social Contracts",
    score: 0.84,
    emotional: 0.71,
    logic: 0.52,
    pattern: 0.35,
    error: 0.21,
    originality: 0.67,
    time: 0.36,
    flagged: false,
  },
];

export default function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Replace this with real API call later
    setData(mockData);
  }, []);

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Human Validator Dashboard</h1>
      {data.map((entry, idx) => (
        <SubmissionCard key={idx} data={entry} />
      ))}
    </div>
  );
}
