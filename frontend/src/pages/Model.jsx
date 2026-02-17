import ModelPerformance from "../components/ModelPerformance"
import ConfusionMatrix from "../components/ConfusionMatrix"

function Model({ metrics, cm }) {
  return (
    <>
      <h1 className="text-3xl font-bold mb-6">Model Performance</h1>
      <ModelPerformance metrics={metrics} />
      <ConfusionMatrix matrix={cm} />
    </>
  )
}

export default Model
