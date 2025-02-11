import { Task } from "./TasksList"

const TaskCard = (task:Task) => {
  return (
    <>
        <h1>{task.title_2}</h1>
        <p>{task.description_2}</p>
        <hr />
    </>
  )
}

export default TaskCard