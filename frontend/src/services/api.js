const BASE_URL = "https://livelike.onrender.com/api"


export const fetchUsers = async () => {
  const res = await fetch(`${BASE_URL}/users/`)
  return res.json()
}

export const fetchSummary = async () => {
  const res = await fetch(`${BASE_URL}/summary/`)
  return res.json()
}

export const fetchInsights = async () => {
  const res = await fetch(`${BASE_URL}/insights/`)
  return res.json()
}
export const fetchModelMetrics = async () => {
  const res = await fetch(`${BASE_URL}/model-metrics/`)
  return res.json()
}

export const fetchConfusionMatrix = async () => {
  const res = await fetch(`${BASE_URL}/confusion-matrix/`)
  return res.json()
}
export const retrainModel = async () => {
  const res = await fetch(`${BASE_URL}/train-model/`, {
    method: "POST"
  })
  return res.json()
}
