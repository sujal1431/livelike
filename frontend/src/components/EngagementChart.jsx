import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend
} from "recharts"

function EngagementChart({ summary }) {

  const data = [
    { name: "Low Engagement", value: summary.low_engagement_users },
    { name: "High Churn Risk", value: summary.high_churn_risk },
  ]

  const COLORS = ["#ef4444", "#f59e0b"]

  return (
    <div className="bg-white shadow-md rounded-xl p-6 mt-8">
      <h2 className="text-xl font-semibold mb-4">Engagement Distribution</h2>

      <PieChart width={400} height={300}>
        <Pie
          data={data}
          cx="50%"
          cy="50%"
          outerRadius={100}
          dataKey="value"
          label
        >
          {data.map((entry, index) => (
            <Cell key={index} fill={COLORS[index % COLORS.length]} />
          ))}
        </Pie>

        <Tooltip />
        <Legend />
      </PieChart>
    </div>
  )
}

export default EngagementChart
