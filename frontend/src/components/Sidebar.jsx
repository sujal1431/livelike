import { NavLink } from "react-router-dom"

function Sidebar() {

  const linkStyle =
    "block py-2 px-3 rounded hover:bg-gray-700"

  const activeStyle =
    "bg-blue-600 text-white"

  return (
    <div className="w-64 bg-gray-900 text-white min-h-screen p-6">
      <h2 className="text-2xl font-bold mb-8">AI Analytics</h2>

      <nav className="space-y-3">

        <NavLink
          to="/"
          end
          className={({ isActive }) =>
            linkStyle + " " + (isActive ? activeStyle : "")
          }
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/users"
          className={({ isActive }) =>
            linkStyle + " " + (isActive ? activeStyle : "")
          }
        >
          Users
        </NavLink>

        <NavLink
          to="/model"
          className={({ isActive }) =>
            linkStyle + " " + (isActive ? activeStyle : "")
          }
        >
          Model
        </NavLink>

      </nav>
    </div>
  )
}

export default Sidebar
