import { useEffect, useState } from 'react'
import { getAllTask } from '../api/task.api'
import TaskCard from './TaskCard';


export interface Task {
  id: number;
  title_2: string;
  description_2: string;
  done_2: boolean;
  prueba: string;
}

const TasksList = () => {

  const [tasks, setTasks] = useState<Task[]>([])

    const load = async () => {
        const response = await getAllTask()
        console.log({response})
        setTasks(response.data)
      }

    useEffect(() => {
      
      load()
    
      return () => {}
    }, [])
    
  return (
    <>
      <div>TasksList</div>
      <div>
        {
          tasks.map((task: Task) => (
            <TaskCard key={task.id} {...task} />
          ))
        }
        </div>
    </>

  )
}

export default TasksList