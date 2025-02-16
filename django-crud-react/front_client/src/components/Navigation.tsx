import { Link } from "react-router-dom"

export const Navigation = () => {
  return (
    <div className="flex justify-between py-3">
        <Link to={"/tasks"}>
            <h1 className="font-bold text-3x1 mb-4">Task_App</h1>
        </Link>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          <Link to="/task-create">Create Task</Link>
        </button>
    </div>
  )
}
