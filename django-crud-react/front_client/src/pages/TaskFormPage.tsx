import { useForm } from "react-hook-form"
import { createTask, deleteTask } from "../api/task.api"
import { Task } from "../components/TasksList"
import { useNavigate, useParams } from "react-router-dom"

export const TaskFormPage = () => {

  const navigate = useNavigate()
  const params = useParams()
  console.log({params})

  const {register, handleSubmit,
    formState: {errors}, reset
  } = useForm<Task>()

  const onSubmit = handleSubmit(async (data: Task) => {
    console.log(data)
    const resp = await createTask(data)
    console.log({resp})
    // Validar si la respuesta fue exitosa
    if (resp.status === 200 || resp.status === 201) {
      reset()
      navigate('/tasks')
    } else {
      console.error("Error creating task:", resp.statusText)
      // Puedes mostrar un mensaje de error al usuario aquí
    }
  })

  const eliminarTask = async () => {    
    const accept = window.confirm("Are you sure you want to delete this task?")
    if (!accept) return
    
    const resp = await deleteTask(Number(params.id))
    console.log({resp})
    if (resp.status === 204) {
      navigate('/tasks')
    } else {
      console.error("Error deleting task:", resp.statusText)
    }
  }

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input type="text" id="" placeholder="title" {...register("title_2", {required: true})}/><br/>
        {errors.title_2 && <span>This field is required</span>}
        <br/>
        <textarea id="" rows={3} placeholder="Description" {...register("description_2", {required:true})}></textarea>
        <br/>
        {errors.description_2 && <span>This field is required</span>}
        <br/>
        <textarea id="" rows={3} placeholder="Prueba" {...register("prueba", {required:true})}></textarea>
        <br/>
        <label htmlFor="">Done</label>
        <input type="checkbox" id="" {...register("done_2")} />
        <br/>
        <button>Save</button>
      </form>
      {
        params.id && <button onClick={eliminarTask}>Delete</button>
      }
    </div>
  )
}
