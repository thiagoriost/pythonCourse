import { useNavigate } from "react-router-dom"
import { Task } from "./TasksList"

const TaskCard = (task:Task) => {

  const navigate = useNavigate()
  
  const goEdit = (task:Task) => {
    navigate(`/tasks/${task.id}`)
  }


  return (
    <div onClick={() => goEdit(task)}>
        <h1>{task.title_2}</h1>
        <p>{task.description_2}</p>
        <hr />
    </div>
  )
}

export default TaskCard