import { useState } from "react"
import { retrainModel } from "../services/api"

function RetrainButton({ onComplete }) {

  const [loading, setLoading] = useState(false)

  const handleRetrain = async () => {
    setLoading(true)

    try {
      const result = await retrainModel()
      alert("Model retrained! Accuracy: " +
            (result.accuracy * 100).toFixed(1) + "%")

      if (onComplete) onComplete()

    } catch (err) {
      alert("Training failed")
    }

    setLoading(false)
  }

  return (
    <button
      onClick={handleRetrain}
      disabled={loading}
      className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700"
    >
      {loading ? "Training..." : "Retrain Model"}
    </button>
  )
}

export default RetrainButton
