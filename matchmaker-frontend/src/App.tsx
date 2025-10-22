import { useState } from 'react'
import './App.css'
import { Route, Routes, BrowserRouter } from 'react-router-dom'
import { HomePage } from './pages/HomePage.tsx'
import { LoginPage } from './pages/LoginPage.tsx'
import { RegisterPage } from './pages/RegisterPage.tsx'
import { GroupsPage } from './pages/GroupsPage.tsx'
import { Navbar2 } from './components/Navbar2.tsx'
import { NewGroupPage } from './pages/NewGroupPage.tsx'
import { NewSessionPage } from './pages/NewSessionPage.tsx'

function App() {

  return (
    <>
      <div className="container m-auto">
        <BrowserRouter>
          <Navbar2 />
          <Routes>
            <Route
              path="/"
              element={<HomePage />}
            ></Route>
            <Route
              path="/login"
              element={<LoginPage />}
            ></Route>
            <Route
              path="/register"
              element={<RegisterPage />}
            ></Route>
            <Route
              path="/groups"
              element={<GroupsPage />}
            ></Route>
            <Route
              path="/newGroup"
              element={<NewGroupPage />}
            ></Route>
            <Route
              path="/newSession"
              element={<NewSessionPage />}
            ></Route>
          </Routes>
        </BrowserRouter>
      </div>
    </>
  )
}

export default App
