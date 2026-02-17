function ConfusionMatrix({ matrix }) {
  if (!matrix) return null

  return (
    <div className="bg-white shadow-md rounded-xl p-6 mt-8">
      <h2 className="text-xl font-semibold mb-4">Confusion Matrix</h2>

      <table className="border text-center">
        <thead>
          <tr>
            <th></th>
            <th className="p-3">Predicted No</th>
            <th className="p-3">Predicted Yes</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <th className="p-3">Actual No</th>
            <td className="p-4 bg-green-100">{matrix[0][0]}</td>
            <td className="p-4 bg-red-100">{matrix[0][1]}</td>
          </tr>
          <tr>
            <th className="p-3">Actual Yes</th>
            <td className="p-4 bg-red-100">{matrix[1][0]}</td>
            <td className="p-4 bg-green-100">{matrix[1][1]}</td>
          </tr>
        </tbody>
      </table>
    </div>
  )
}

export default ConfusionMatrix
