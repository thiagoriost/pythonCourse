import { useNavigate } from "react-router-dom"
import { Task } from "./TasksList"

const TaskCard = (task:Task) => {

  const navigate = useNavigate()
  
  const goEdit = (task:Task) => {
    navigate(`/tasks/${task.id}`)
  }


  return (
    <div onClick={() => goEdit(task)} style={{cursor:'pointer', background: task.done_2 ?'#0b270b':'', color:'white', padding:'10px', margin:'10px'}}>
        <h1>{task.id} - {task.title_2}</h1>
        <p>{task.description_2}</p>
        <h2>Done</h2>
        <input type="checkbox" checked={task.done_2} disabled={true} style={{color:'green'}} name="" id="" />
        <hr />
    </div>
  )
}

export default TaskCard