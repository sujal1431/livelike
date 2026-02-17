import UsersTable from "../components/UsersTable"

function Users({ users }) {
  return (
    <>
      <h1 className="text-3xl font-bold mb-6">Users</h1>
      <UsersTable users={users} />
    </>
  )
}

export default Users
