function Sidebar() {
  return (
    <div className="w-64 bg-gray-900 text-white min-h-screen p-6">
      <h2 className="text-2xl font-bold mb-8">AI Analytics</h2>

      <nav className="space-y-4">
        <div className="hover:text-blue-400 cursor-pointer">
          Dashboard
        </div>
        <div className="hover:text-blue-400 cursor-pointer">
          Users
        </div>
        <div className="hover:text-blue-400 cursor-pointer">
          Model
        </div>
      </nav>
    </div>
  )
}

export default Sidebar
