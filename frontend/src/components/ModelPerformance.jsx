function MetricCard({ title, value }) {
  return (
    <div className="bg-gray-50 border rounded-lg p-4">
      <p className="text-sm text-gray-500">{title}</p>
      <p className="text-2xl font-bold">{value}</p>
    </div>
  )
}

function ModelPerformance({ metrics }) {

  if (!metrics) return null

  const report = metrics.classification_report

  return (
    <div className="bg-white shadow-md rounded-xl p-6 mt-8">
      <h2 className="text-xl font-semibold mb-4">Model Performance</h2>

      <div className="grid grid-cols-4 gap-4">
        <MetricCard
          title="Accuracy"
          value={(metrics.accuracy * 100).toFixed(1) + "%"}
        />
        <MetricCard
          title="Precision"
          value={(report["1"].precision * 100).toFixed(1) + "%"}
        />
        <MetricCard
          title="Recall"
          value={(report["1"].recall * 100).toFixed(1) + "%"}
        />
        <MetricCard
          title="F1 Score"
          value={(report["1"]["f1-score"] * 100).toFixed(1) + "%"}
        />
      </div>
    </div>
  )
}

export default ModelPerformance
