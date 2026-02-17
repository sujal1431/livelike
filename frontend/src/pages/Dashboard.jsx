import SummaryCard from "../components/SummaryCard"
import EngagementChart from "../components/EngagementChart"
import ModelPerformance from "../components/ModelPerformance"
import ConfusionMatrix from "../components/ConfusionMatrix"
import InsightsPanel from "../components/InsightsPanel"
import RetrainButton from "../components/RetrainButton"

function Dashboard({ summary, metrics, cm, insights, refreshMetrics }) {

  return (
    <>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <RetrainButton onComplete={refreshMetrics} />
      </div>

      <div className="grid grid-cols-4 gap-6">
        <SummaryCard title="Total Users" value={summary.total_users} />
        <SummaryCard title="High Churn Risk" value={summary.high_churn_risk} />
        <SummaryCard title="Low Engagement Users" value={summary.low_engagement_users} />
        <SummaryCard
          title="Model Accuracy"
          value={metrics ? (metrics.accuracy * 100).toFixed(1) + "%" : "Loading"}
        />
      </div>

      <EngagementChart summary={summary} />
      <ModelPerformance metrics={metrics} />
      <ConfusionMatrix matrix={cm} />
      <InsightsPanel insights={insights} />
    </>
  )
}

export default Dashboard
