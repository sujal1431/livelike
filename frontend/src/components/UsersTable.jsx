import { useState } from "react"

function UsersTable({ users }) {

  const [page, setPage] = useState(1)
  const rowsPerPage = 20

  const start = (page - 1) * rowsPerPage
  const currentRows = users.slice(start, start + rowsPerPage)
  const totalPages = Math.ceil(users.length / rowsPerPage)

  return (
    <div className="bg-white shadow-md rounded-xl p-6 mt-8">
      <h2 className="text-xl font-semibold mb-4">User Analytics</h2>

      <table className="w-full">
        <thead>
          <tr className="bg-gray-100 text-left">
            <th className="p-3">Session</th>
            <th className="p-3">Pages</th>
            <th className="p-3">Clicks</th>
            <th className="p-3">Engagement</th>
            <th className="p-3">Churn %</th>
          </tr>
        </thead>

        <tbody>
          {currentRows.map(user => (
            <tr key={user.id} className="border-t">
              <td className="p-3">{user.session_time}</td>
              <td className="p-3">{user.pages_visited}</td>
              <td className="p-3">{user.clicks}</td>
              <td className="p-3">{user.engagement_score?.toFixed(2)}</td>
              <td className="p-3">
                {(user.churn_probability * 100).toFixed(1)}%
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="flex justify-between mt-4">
        <button
          onClick={() => setPage(p => Math.max(p - 1, 1))}
          className="px-4 py-2 bg-gray-200 rounded"
        >
          Prev
        </button>

        <span>Page {page} / {totalPages}</span>

        <button
          onClick={() => setPage(p => Math.min(p + 1, totalPages))}
          className="px-4 py-2 bg-gray-200 rounded"
        >
          Next
        </button>
      </div>
    </div>
  )
}

export default UsersTable
