function InsightsPanel({ insights }) {
  return (
    <div className="bg-white shadow-md rounded-xl p-6 mt-8">
      <h2 className="text-xl font-semibold mb-4">AI Insights</h2>

      <ul className="space-y-2">
        {insights.map((item, index) => (
          <li
            key={index}
            className="bg-blue-50 border border-blue-200 p-3 rounded-lg"
          >
            {item}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default InsightsPanel
