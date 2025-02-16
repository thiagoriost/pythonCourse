import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom"
import { TasksPage } from "./pages/TasksPage"
import { TaskFormPage } from "./pages/TaskFormPage"
import { Navigation } from "./components/Navigation"
import { Toaster } from "react-hot-toast"

const App = () => {
  return (
    <BrowserRouter>      
      <div className="container mx-auto p-4">
        <Navigation />
        <Routes>
          <Route path="/" element={<Navigate to="/tasks" />} />
          <Route path="/tasks" element={<TasksPage />} />
          <Route path="/tasks/:id" element={<TaskFormPage />} />
          <Route path="/task-create" element={<TaskFormPage />} />
          {/* <Route path="/task/:id" element={<TaskFormPage />} /> */}
        </Routes>
        <Toaster />      
      </div>  
    </BrowserRouter>
  )
}

export default App

