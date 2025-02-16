import { useForm } from "react-hook-form"
import { createTask, deleteTask, getTask, updateTask } from "../api/task.api"
import { Task } from "../components/TasksList"
import { useNavigate, useParams } from "react-router-dom"
import { useEffect } from "react"
import toast from "react-hot-toast"

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
      toast.success("Task updated successfully",{
        position:'bottom-right',
        style:{
          backgroundColor: '#101010',
          color: 'white'
        }
      })
    } else {
      // Crear
      const resp = await createTask(data)
      console.log({resp})
      // Validar si la respuesta fue exitosa
      if (resp.status === 200 || resp.status === 201) {
        reset()
        toast.success("Task created successfully",{
          position:'bottom-right',
          style:{
            backgroundColor: '#101010',
            color: 'white'
          }
        })
      } else {
        console.error("Error creating task:", resp.statusText)
        toast.error("Error creating task")
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
      toast.success("Task deleted successfully",{
        position:'bottom-right',
        style:{
          backgroundColor: '#101010',
          color: 'white'
        }
      })
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
    <div className="max-w-xl mx-auto p-4">
      <form onSubmit={onSubmit}>
        <input type="text" id="" placeholder="title" {...register("title_2", {required: true})}
        className="bg-zinc-200 p-3 w-full rounded-lg blok mb-3"
        /><br/>
        {errors.title_2 && <span>This field is required</span>}
        <textarea id="" rows={3} placeholder="Description" {...register("description_2", {required:true})}
        className="bg-zinc-200 p-3 w-full rounded-lg blok mb-3"
        ></textarea>
        {errors.description_2 && <span>This field is required</span>}
        <textarea id="" rows={3} placeholder="Prueba" {...register("prueba", {required:true})}
        className="bg-zinc-200 p-3 w-full rounded-lg blok mb-3"
        ></textarea>
        <label htmlFor="">Done</label>
        <input type="checkbox" id="" {...register("done_2")} />
        <br />
        <button className="bg-indigo-500 block w-full mt-3 hover:bg-blue-700 text-white font-bold p-3 rounded-lg">Save</button>
      </form>
      {
        params.id && 
        <div className="flex justify-end">
          <button onClick={eliminarTask} className="bg-red-500 hover:bg-red-700 mt-3 text-white font-bold p-3 rounded">Delete</button>
        </div>
      }
    </div>
  )
}
