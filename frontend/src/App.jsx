import { useEffect, useState } from "react"

import SummaryCard from "./components/SummaryCard"
import UsersTable from "./components/UsersTable"
import InsightsPanel from "./components/InsightsPanel"
import EngagementChart from "./components/EngagementChart"
import ConfusionMatrix from "./components/ConfusionMatrix"
import ModelPerformance from "./components/ModelPerformance"
import Layout from "./components/Layout"
import RetrainButton from "./components/RetrainButton"

import {
  fetchSummary,
  fetchUsers,
  fetchInsights,
  fetchModelMetrics,
  fetchConfusionMatrix
} from "./services/api"


function App() {

  const [summary, setSummary] = useState(null)
  const [users, setUsers] = useState([])
  const [insights, setInsights] = useState([])
  const [cm, setCm] = useState(null)
  const [metrics, setMetrics] = useState(null)

  // ---------- refresh model results after retraining ----------
  const refreshMetrics = () => {
    fetchModelMetrics().then(setMetrics)
    fetchConfusionMatrix().then(data => setCm(data.matrix))
  }

  // ---------- initial data load ----------
  useEffect(() => {
    fetchSummary().then(setSummary)
    fetchUsers().then(setUsers)
    fetchInsights().then(setInsights)
    refreshMetrics()
  }, [])


  if (!summary) return <div className="p-6">Loading...</div>

  return (
    <Layout>

      {/* ---------- header + retrain button ---------- */}
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">
          Engagement Analytics Dashboard
        </h1>

        <RetrainButton onComplete={refreshMetrics} />
      </div>


      {/* ---------- summary cards ---------- */}
      <div className="grid grid-cols-4 gap-6">
        <SummaryCard title="Total Users" value={summary.total_users} />
        <SummaryCard title="High Churn Risk" value={summary.high_churn_risk} />
        <SummaryCard title="Low Engagement Users" value={summary.low_engagement_users} />

        <SummaryCard
          title="Model Accuracy"
          value={metrics ? (metrics.accuracy * 100).toFixed(1) + "%" : "Loading"}
        />
      </div>


      {/* ---------- analytics sections ---------- */}
      <EngagementChart summary={summary} />
      <ModelPerformance metrics={metrics} />
      <ConfusionMatrix matrix={cm} />
      <UsersTable users={users} />
      <InsightsPanel insights={insights} />

    </Layout>
  )
}

export default App
