import { useForm } from "react-hook-form"
import { createTask, deleteTask, getTask, updateTask } from "../api/task.api"
import { Task } from "../components/TasksList"
import { useNavigate, useParams } from "react-router-dom"
import { useEffect } from "react"

export const TaskFormPage = () => {

  const navigate = useNavigate()
  const params = useParams()
  console.log({params})

  const {register, handleSubmit,
    formState: {errors}, reset
  } = useForm<Task>()

  const onSubmit = handleSubmit(async (data: Task) => {
    console.log(data)
    if (params.id) {
      // Editar
      const respUpdate = await updateTask(Number(params.id), data)
      console.log({respUpdate})
    } else {
      // Crear
      const resp = await createTask(data)
      console.log({resp})
      // Validar si la respuesta fue exitosa
      if (resp.status === 200 || resp.status === 201) {
        reset()
      } else {
        console.error("Error creating task:", resp.statusText)
        // Puedes mostrar un mensaje de error al usuario aquí
      }
    }
    navigate('/tasks')

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

  useEffect(() => {
    if (params.id) {
      const load = async () => {
        const response = await getTask(Number(params.id))
        console.log({response})
        reset(response.data)
      }
      load()
    }
    return () => {}
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [params.id])
  

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
