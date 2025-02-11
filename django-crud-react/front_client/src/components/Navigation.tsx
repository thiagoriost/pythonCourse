import { Link } from "react-router-dom"

export const Navigation = () => {
  return (
    <div>
        <h1>-----------Navigation-----------------</h1>
        <Link to={"/tasks"}>
            <h1>Task_App</h1>
        </Link>
        <Link to="/task-create">Create Task</Link>
        <h1>----------------------------</h1>
    </div>
  )
}
