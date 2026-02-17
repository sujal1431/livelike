const BASE_URL = "http://127.0.0.1:8000/api"

export const fetchUsers = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/users/")
  return res.json()
}

export const fetchSummary = async () => {
  const res = await fetch(`${BASE_URL}/summary/`)
  return res.json()
}

export const fetchInsights = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/insights/")
  return res.json()
}
export const fetchModelMetrics = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/model-metrics/")
  return res.json()
}

export const fetchConfusionMatrix = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/confusion-matrix/")
  return res.json()
}
export const retrainModel = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/train-model/", {
    method: "POST"
  })
  return res.json()
}
