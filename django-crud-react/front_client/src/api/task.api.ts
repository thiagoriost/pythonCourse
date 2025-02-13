import axios from "axios"
import { Task } from "../components/TasksList"

const taskApi = axios.create({
    baseURL: 'http://localhost:8000/task/api/v1/tareas_2/'
})

export const getAllTask = () => taskApi.get('/')
export const createTask = (task: Task) => taskApi.post('/', task)
export const deleteTask = (id: number) => taskApi.delete(`/${id}/`)