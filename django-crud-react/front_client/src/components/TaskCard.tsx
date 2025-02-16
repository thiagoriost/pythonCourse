import { useNavigate } from "react-router-dom"
import { Task } from "./TasksList"

const TaskCard = (task:Task) => {

  const navigate = useNavigate()
  
  const goEdit = (task:Task) => {
    navigate(`/tasks/${task.id}`)
  }


  return (
    <div onClick={() => goEdit(task)} className="bg-zinc-800 p-3 hover:bg-zinc-700 cursor-pointer">
        <h1 className="font-bold uppercase">{task.id} - {task.title_2}</h1>
        <p className="text-slate-400">{task.description_2}</p>
        <h2>Done</h2>
        <input type="checkbox" checked={task.done_2} disabled={true} style={{color:'green'}} name="" id="" />
    </div>
  )
}

export default TaskCard