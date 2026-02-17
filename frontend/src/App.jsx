import { BrowserRouter, Routes, Route } from "react-router-dom"
import { useEffect, useState } from "react"

import Layout from "./components/Layout"
import Dashboard from "./pages/Dashboard"
import Users from "./pages/Users"
import Model from "./pages/Model"

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

  const refreshMetrics = () => {
    fetchModelMetrics().then(setMetrics)
    fetchConfusionMatrix().then(data => setCm(data.matrix))
  }

  useEffect(() => {
    fetchSummary().then(setSummary)
    fetchUsers().then(setUsers)
    fetchInsights().then(setInsights)
    refreshMetrics()
  }, [])

  if (!summary) return <div className="p-6">Loading...</div>

  return (
    <BrowserRouter>
      <Layout>

        <Routes>

          <Route
            path="/"
            element={
              <Dashboard
                summary={summary}
                metrics={metrics}
                cm={cm}
                insights={insights}
                refreshMetrics={refreshMetrics}
              />
            }
          />

          <Route
            path="/users"
            element={<Users users={users} />}
          />

          <Route
            path="/model"
            element={<Model metrics={metrics} cm={cm} />}
          />

        </Routes>

      </Layout>
    </BrowserRouter>
  )
}

export default App
