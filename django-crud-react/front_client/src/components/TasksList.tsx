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
        // Ordenar por la propiedad 'done_2', con false primero
        const sortedData = response.data.sort((a: { done_2: number; }, b: { done_2: number; }) => a.done_2 - b.done_2);
        console.log({sortedData})
        setTasks(sortedData)
      }

    useEffect(() => {
      
      load()
    
      return () => {}
    }, [])
    
  return (
    <div className="grid grid-cols-3 gap-3">
      <div>TasksList</div>
      <div>
        {
          tasks.map((task: Task) => (
            <TaskCard key={task.id} {...task} />
          ))
        }
        </div>
    </div>

  )
}

export default TasksList